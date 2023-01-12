from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# in the app we will first create a function with home name.


def home(request):
    return(HttpResponse("Hello welcome to the chef's table")
           )

# then create url.py file in the chefsApp
