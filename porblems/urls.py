from django.contrib import admin
from django.urls import path,include
from porblems.views import all_problems,problems_description
# from real_compiler.views import submit
urlpatterns = [
    path('all/',all_problems,name="all problems"),
    # all/{{p.id}}
    path('all/<int:id>/',problems_description,name="problems_description"),
]
