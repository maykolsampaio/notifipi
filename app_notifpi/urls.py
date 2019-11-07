from django.urls import path
from .views import FileUploadView
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', FileUploadView.as_view()),
    url(r'^aviso/$', views.AvisoList.as_view(), name='Aviso-list'),
]

