from rest_framework import viewsets

from .serializers import HeroSerializer, ModelSerializer
from .models import Hero, Model


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by(r'name')
    serializer_class = HeroSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by(r'name')
    serializer_class = ModelSerializer