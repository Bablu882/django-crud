from django.shortcuts import render

# Create your views here.
def my_view(request):
    resp=render(request,'home.html')
    return  resp  

def test1_view(request):
    resp=render(request,'index.html')
    return resp


def test2_view(request):
    resp=render(request,'home2.html')
    return resp
