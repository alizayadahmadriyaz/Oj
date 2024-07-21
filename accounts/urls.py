from django.contrib import admin
from django.urls import path,include
from accounts.views import register_user,login_user,log_out

urlpatterns = [
    path('register/',register_user,name="register_user"),
    path('login/',login_user,name="login_user"),
    path('logout/',log_out,name="logout_user")
]