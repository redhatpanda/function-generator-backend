from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('handlegendata', csrf_exempt(views.handleGenFunction), name='handleGenFunction'),
    path('handlegenfourier', csrf_exempt(views.handleGenFourier), name='handleGenFourier'),
]