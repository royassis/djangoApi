# serializers.py
from rest_framework import serializers

from .models import MlModel, MlProject

from pathlib import Path
import os

import logging
logging.basicConfig(level=logging.DEBUG)



class MlModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlModel
        fields = ('id', 'project', 'name', 'upload', 'created')

    def update(self, instance, validated_data):
        for f in Path(r'C:\Users\User\PycharmProjects\djangoApi\uploads').rglob("*.*"):
            os.remove(f)
            logging.debug(f"file remove: {f}")
        logging.debug(dir(instance.upload))
        print(instance.upload.save())
        instance.save()
        return instance


class MlProjectSerializer(serializers.ModelSerializer):
    mlmodels = MlModelSerializer(many=True, read_only=True)

    class Meta:
        model = MlProject
        fields = ("id", "name", "mlmodels", 'created')

