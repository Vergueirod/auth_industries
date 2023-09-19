from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address

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

@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address/list.html', {'addresses':addresses})