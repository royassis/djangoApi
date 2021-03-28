from rest_framework import viewsets, mixins
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
import pickle

from .forms import UploadFileForm

from .serializers import HeroSerializer, ModelSerializer
from .models import Hero, Model

import logging

logger = logging.getLogger(__name__)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by(r'name')
    serializer_class = HeroSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by(r'name')
    serializer_class = ModelSerializer

    def create(self,request):
        f = request.FILES['file']
        name = request.data["name"]
        model = request.data["model"].encode("utf8")[3:]
        logger.error(f"obj : {model}, type : {type(model)}")

        new_model = Model(name=name, model=model)
        new_model.save()
        return HttpResponseRedirect('')

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        logger.error(user.model)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            new_model = Model(name=form.cleaned_data['title'], model=f.read())
            new_model.save()
            logger.debug(f"model saved")
            return HttpResponseRedirect('')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
