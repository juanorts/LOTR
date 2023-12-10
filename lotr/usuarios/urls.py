from . import views
from django.urls import include, path

urlpatterns = [
    path('login_usuario', views.login_usuario, name="login"),
    path('logout_usuario', views.logout_usuario, name="logout"),
    path('registrar_usuario', views.registrar_usuario, name="registrar_usuario")
]
