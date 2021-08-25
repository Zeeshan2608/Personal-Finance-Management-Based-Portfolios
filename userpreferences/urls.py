from . import views
from django.urls import path

urlpatterns = [
    path('usertre', views.index, name="preferences")
]
