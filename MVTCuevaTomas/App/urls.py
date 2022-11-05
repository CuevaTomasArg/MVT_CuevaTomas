# from django.contrib import path
from django.contrib import admin
from django.urls import path, re_path, include
from App.views import mostrar_familiar
urlpatterns = [
    path('familiares/',mostrar_familiar)
]
