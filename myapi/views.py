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
