from django.http import HttpResponse
from django.shortcuts import render

#methode view
def index(request):
    return render(request, 'index.html')

def index2(request):
    str_output = "<h1>oke</h1>"
    return HttpResponse(str_output)