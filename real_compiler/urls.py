from django.contrib import admin
from django.urls import path,include
from real_compiler.views import submit

urlpatterns = [
    path(" ",submit,name="submit"),
]