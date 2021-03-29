# serializers.py
from rest_framework import serializers

from .models import MlModel


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MlModel
        fields = ('id','name', 'model', 'upload')