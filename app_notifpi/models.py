from django.conf import settings
from django.db import models
from django.utils import timezone
from gdstorage.storage import GoogleDriveStorage

gd_storage=GoogleDriveStorage()

class Aviso(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    audio_aviso = models.FileField(blank=True, null=True,storage=gd_storage,upload_to="audio/")

    class Meta:

        db_table = 'audio_aviso'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title