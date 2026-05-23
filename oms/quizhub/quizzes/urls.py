from django.urls import path
from .views import QuizListView, RequestExplorerView, CategoryAdminListView, CategoryAdminCreateView, CategoryAdminUpdateView, CategoryAdminDeleteView

app_name = "quizzes"

urlpatterns = [
    path("request-info/", RequestExplorerView.as_view(), name="request_info"),
    path("", QuizListView.as_view(), name="quiz_list"),
    path("admin/categories/", CategoryAdminListView.as_view(), name="categories_admin"),
    path("admin/categories/add/", CategoryAdminCreateView.as_view(), name="category_add"),
    path("admin/categories/<int:pk>/edit/", CategoryAdminUpdateView.as_view(), name="category_edit"), 
    path("admin/categories/<int:pk>/delete/", CategoryAdminDeleteView.as_view(), name="category_delete"),


]