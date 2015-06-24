from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import FileUploadInit, FileUploadView

urlpatterns = [
    url(r'^/token$', obtain_auth_token),
    url(r'^/upload$', FileUploadInit.as_view()),
    url(r'^/upload/(?P<filename>[\w\-]+)', FileUploadView.as_view()),
]
