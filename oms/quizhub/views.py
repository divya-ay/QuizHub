from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

def hello_world(request):
    return HttpResponse("Hello, world!")

class HomePageView(View):
    def get(self, request):
        return render(request, 'quizhub/home.html')