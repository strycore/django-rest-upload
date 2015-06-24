from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class FileUploadInit(views.APIView):
    renderer_classes = (JSONRenderer, )

    def post(self, request):
        print("init upload")
        print(request.data)
        response = Response()
        response['Location'] = "/api/upload/bliblu"
        return response


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    renderer_classes = (JSONRenderer, )

    def put(self, request, filename):
        file_obj = request.data['file']
        with open('/home/strider/uploads/bliblu', 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        return Response(status=204)
