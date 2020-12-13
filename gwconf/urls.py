from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('<int:gatewayconfig_id>', views.generate_config, name='generate_config'),
            ]
