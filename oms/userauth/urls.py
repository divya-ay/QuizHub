from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, SignUpView

app_name = "userauth"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="quizhub:home"), name="logout"),
]