from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string_response(request):
    return HttpResponse("<h1>THIS IS STRING RESPONSE</h1>") 
def sample(request):
    return render(request,'sample.html')