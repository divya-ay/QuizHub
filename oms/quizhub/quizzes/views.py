from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from django.urls import reverse_lazy
from .models import Quiz, Category
from .forms import CategoryForm

class RequestExplorerView(View):
    def get(self, request):
    # query params: /shop/products/request -info/?page=2&order=desc
        query_params = dict(request.GET)
        page = request.GET.get("page")
        method = request.method
        path = request.path
        user = request.user.username if request.user.is_authenticated else "anonymous"
        client_ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT","")

        lines = [
            f"Method: {method}",
            f"Path: {path}",
            f"User: {user}",
            f"Query params: {query_params}",
            f"Page param: {page}",
            f"Client IP: {client_ip}",
            f"User-Agent: {user_agent}",
        ]
        return HttpResponse("\n".join(lines), content_type="text/plain")
    
class QuizListView(View):
    def get(self, request):
        quizzes = [
            {"id": 1, "title": "General Knowledge Quiz", "category": "General"},
            {"id": 2, "title": "Science Quiz", "category": "Science"},
            {"id": 3, "title": "History Quiz", "category": "History"},
        ]
        context = {"quizzes": quizzes}
        return render(request, "quizzes/list.html", context)
    
class CategoryAdminListView(ListView):
    model = Category

    template_name = "quizzes/categories/admin_list.html"

    context_object_name = "categories"
    paginate_by = 10

class CategoryAdminCreateView(CreateView):
    form_class = CategoryForm
    template_name = "quizzes/categories/admin_form.html"
    success_url = reverse_lazy("quizhub:quizzes:categories_admin")

class CategoryAdminUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "quizzes/categories/admin_form.html"
    success_url = reverse_lazy("quizhub:quizzes:categories_admin")

class CategoryAdminDeleteView(DeleteView):
    model = Category
    template_name = "quizzes/categories/admin_confirm_delete.html"
    success_url = reverse_lazy("quizhub:quizzes:categories_admin")