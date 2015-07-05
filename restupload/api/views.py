import os
import uuid
import json
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.cache import cache
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import permissions


class FileUploadInit(views.APIView):
    renderer_classes = (JSONRenderer, )
    # permission_classes = (permissions.IsAuthenticated)

    def post(self, request):
        upload_id = uuid.uuid4()
        cache.set(upload_id, {'filename': request.data['title']}, 60)
        upload_url = reverse('upload_file', kwargs={'filename': upload_id})
        response = Response()
        response['Location'] = upload_url
        return response


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    renderer_classes = (JSONRenderer, )

    def put(self, request, filename):
        upload_data = cache.get(filename)
        print upload_data
        if not upload_data:
            return Response(404)

        upload_path = os.path.join(settings.MEDIA_ROOT, upload_data['filename'])
        if 'file' not in request.data:
            return Response(json.dumps({'error': 'No file in request'}))
        file_obj = request.data['file']
        with open(upload_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        file_data = {
            'url': settings.MEDIA_URL + upload_data['filename']
        }
        return Response(json.dumps(file_data))
