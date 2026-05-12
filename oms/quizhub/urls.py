from django.urls import path, include
urlpatterns = [
    path(
        "quizzes/",
        include(("quizhub.quizzes.urls"), namespace="quizzes"),
    ),
]