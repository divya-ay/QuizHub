from django.views import View
from django.http import HttpResponse

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
            {"id": 1, "title": "General Knowledge Quiz"},
            {"id": 2, "title": "Science Quiz"},
            {"id": 3, "title": "History Quiz"},
        ]
        context = {"quizzes": quizzes}
        return render(request, "quizzes/quiz_list.html", context)