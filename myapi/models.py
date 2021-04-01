import shutil

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from pathlib import Path

class MlProject(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

def project_path(instance, filename):
    # Get appname
    #instance._meta.app_label

    # file will be uploaded to MEDIA_ROOT/settings.MLPROJECTS_DIR/instance.project.name/filename
    return f"{settings.MLPROJECTS_DIR}/{instance.project.name}/{filename}"

class MlModel(models.Model):
    project = models.ForeignKey(MlProject, on_delete=models.CASCADE, related_name="mlmodels")
    name = models.CharField(max_length=120)
    model = models.BinaryField(null=True)
    upload = models.FileField(upload_to=project_path, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


