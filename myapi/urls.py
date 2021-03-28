from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('heroes', views.HeroViewSet)
router.register('models', views.ModelViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("predict/",views.PredictView.as_view()),
    path('upload/', views.upload_file, name='upload'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]