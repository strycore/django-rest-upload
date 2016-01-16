from django.db import models


class FileRepository(models.Model):
    name = models.CharField(max_length=255)
    fileobj = models.FileField()

    class Meta(object):
        pass

    def __unicode__(self):
        return self.name
