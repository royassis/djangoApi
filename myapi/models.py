from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=120)
    alias = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=120)
    model = models.BinaryField()
    upload = models.FileField(upload_to='message/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.name


