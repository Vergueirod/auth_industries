from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login

# Create your views here.

def indexAuth(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    #Se não o metodo é POST
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    
    if user:
        django_login(request, user)
        return HttpResponseRedirect('/home/')
    
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')