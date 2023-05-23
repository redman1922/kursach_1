from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginAuthView.as_view(), name="login"),
    path("", views.UserProfile.as_view(), name="home"),
]
