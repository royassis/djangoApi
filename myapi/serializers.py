# serializers.py
from rest_framework import serializers

from .models import MlModel, MlProject


class MlModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlModel
        fields = ('id', 'project', 'name', 'upload', 'created')


class MlProjectSerializer(serializers.ModelSerializer):
    mlmodels = MlModelSerializer(many=True, read_only=True)

    class Meta:
        model = MlProject
        fields = ("id", "name", "mlmodels", 'created')
