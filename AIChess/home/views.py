from django.shortcuts import render
from django.http import HttpResponse
from requests.api import request

# Create your views here.
def home(request):
	# return HttpResponse("Hello world")
	return render(request, 'home/index.html')

def base(request):
	return render(request, 'home/base.html')