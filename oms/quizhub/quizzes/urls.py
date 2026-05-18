from django.urls import path
from .views import QuizListView, RequestExplorerView

app_name = "quizzes"

urlpatterns = [
    path("request-info/", RequestExplorerView.as_view(), name="request_info"),
    path("", QuizListView.as_view(), name="quiz_list"),
]