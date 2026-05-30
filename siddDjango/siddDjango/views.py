from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world , you are in home page")

def about(request):
    return HttpResponse("hello world , you are in about page")

def contact(request):
    return HttpResponse("hello world , you are in contact page")
