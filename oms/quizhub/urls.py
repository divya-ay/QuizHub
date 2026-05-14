from django.urls import path, include

from .views import HomePageView

app_name = "quizhub"

urlpatterns = [
    path(
        "quizzes/",
        include(("quizhub.quizzes.urls"), namespace="quizzes"),
    ),
    path("", HomePageView.as_view(), name="home"),
]