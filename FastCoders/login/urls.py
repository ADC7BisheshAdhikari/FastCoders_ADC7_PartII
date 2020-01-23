from django.urls import path  
from . import views


urlpatterns = [

    path("register/",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("index/logout/",views.logout, name="logout"),
    path("login/logout/",views.logout, name="logout")
]


