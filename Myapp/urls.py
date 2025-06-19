from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("loginuser",views.loginuser,name="loginuser"),
    path("logoutuser",views.logoutuser,name="logoutuser"),
]
