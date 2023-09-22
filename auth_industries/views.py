from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address, STATES_CHOICES
from django.shortcuts import redirect



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

@login_required(login_url='/login')
def address_create(request):
    if request.method == 'GET':
        states = STATES_CHOICES
        return render(request, 'address/create.html', {'states':states})
    
    Address.objects.create(
        address = request.POST.get('address'),
        address_complement = request.POST.get('address_complement'),
        city = request.POST.get('city'),
        state = request.POST.get('state'),
        country = request.POST.get('country'),
        user = request.user
    )

    return HttpResponseRedirect('/addresses/')

@login_required(login_url='/login')
def address_update(request, id):
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        states = STATES_CHOICES
        return render(request, 'address/update.html', {'states':states, 'address':address})
    
    address.address = request.POST.get('address'),
    address.address_complement = request.POST.get('address_complement'),
    address.city = request.POST.get('city'),
    address.state = request.POST.get('state'),
    address.country = request.POST.get('country'),
    address.user = request.user
    
    address.save()

    return HttpResponseRedirect('/addresses/')

def re_direct_login(request):
    return redirect('/login/')


