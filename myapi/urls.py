from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('mlmodels', views.ModelViewSet)
router.register('mlproject', views.MlProjectViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'models_api'

urlpatterns = [
    path('', include(router.urls)),
    path('mlproject/<int:id>/predict', views.Predict.as_view(), name='predict'),
    path('upload/', views.upload_file, name='upload'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]