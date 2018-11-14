from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def list_page(request):
    return render(request,'app1/list_page.html')