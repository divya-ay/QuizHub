from django.urls import path
from .views import RequestExplorerView

app_name = "quizzes"

urlpatterns = [
    path("request-info/", RequestExplorerView.as_view(), name="request_info"),
]