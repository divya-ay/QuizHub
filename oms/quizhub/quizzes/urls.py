from django.urls import path
from .views import QuizAdminCreateView, QuizAdminUpdateView, QuizAdminDeleteView, QuizAdminListView, RequestExplorerView, CategoryAdminListView, CategoryAdminCreateView, CategoryAdminUpdateView, CategoryAdminDeleteView

app_name = "quizzes"

urlpatterns = [
    path("request-info/", RequestExplorerView.as_view(), name="request_info"),
    path("admin/categories/", CategoryAdminListView.as_view(), name="categories_admin"),
    path("admin/categories/add/", CategoryAdminCreateView.as_view(), name="category_add"),
    path("admin/categories/<int:pk>/edit/", CategoryAdminUpdateView.as_view(), name="category_edit"), 
    path("admin/categories/<int:pk>/delete/", CategoryAdminDeleteView.as_view(), name="category_delete"),

    path("admin/quizzes/", QuizAdminListView.as_view(), name="quiz_admin_list"),
    path("admin/quizzes/add/", QuizAdminCreateView.as_view(), name="quiz_add"),
    path("admin/quizzes/<int:pk>/edit/", QuizAdminUpdateView.as_view(), name="quiz_edit"), 
    path("admin/quizzes/<int:pk>/delete/", QuizAdminDeleteView.as_view(), name="quiz_delete"),

]