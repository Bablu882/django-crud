from django.shortcuts import render

# Create your views here.
def my_view(request):
    resp=render(request,'home.html')
    return resp