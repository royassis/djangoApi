# serializers.py
from rest_framework import serializers

from .models import MlModel


class MlModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlModel
        fields = ('id','name', 'model', 'upload')

class MlProjectSerializer(serializers.ModelSerializer):
    mlmodels = MlModelSerializer(many=True)

    class Meta:
        model = MlModel
        fields = ('name')

    def create(self, validated_data):
        pass