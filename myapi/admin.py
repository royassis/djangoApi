from django.contrib import admin
from .models import MlModel, MlProject

admin.site.register(MlModel)
admin.site.register(MlProject)