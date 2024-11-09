
from django.urls import path

# . is used since its in the same directory
from . import views

urlpatterns = [
    path('', views.index)
]