from django.db import models


class MlProject(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class MlModel(models.Model):
    project = models.ForeignKey(MlProject, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=120)
    model = models.BinaryField()
    upload = models.FileField(upload_to='message/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.name
