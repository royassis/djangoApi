# serializers.py
from rest_framework import serializers

from .models import MlModel, MlProject


class MlModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlModel
        fields = ('id','name', 'upload')

class MlProjectSerializer(serializers.ModelSerializer):
    mlmodels = MlModelSerializer(many=True)

    class Meta:
        model = MlProject
        fields = ("id","name",'mlmodels')

    def create(self, validated_data):
        print("--"*20)
        mlmodels_data = validated_data.pop("mlmodels")
        mlproj = MlProject(**validated_data)
        mlproj.save()
        for mlmodel_data in mlmodels_data:
            mm = mlproj.mlmodels.create(**mlmodel_data)
            mm.save()

        return mlproj