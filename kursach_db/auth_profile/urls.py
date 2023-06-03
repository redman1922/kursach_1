from django.urls import path
from . import views

app_name = "auth"

urlpatterns = [
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginAuthView.as_view(), name="login"),
    path("update/", views.AboutMeUpdateView.as_view(), name="profile_update"),
    path("", views.AboutMeView.as_view(), name="profile"),
]
