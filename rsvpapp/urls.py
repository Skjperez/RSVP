from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirmed/', views.confirmation, name='confirmation'),
]