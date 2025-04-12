from django.shortcuts import render, HttpResponse, redirect
#from django.contrib.auth.forms import UserCreationForm as user_form 
from .forms import CustomUserCreationForm as user_form
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html', context = {})

@login_required
def home(request):
    #user = request.user
    #return HttpResponse('This is Home Page.')
    return render(request, 'home.html', context = {})
'''
#Default Form, no need to create forms.py 
def signup(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('something went wrong.')
    else:
        form = user_form()
    return render(request, 'registration/signup.html', context = {'form': form})
    '''

#Custom Form, need to be created forms.py
def signup(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('something went wrong.')
    else:
        form = user_form()
    return render(request, 'registration/signup.html', context = {'form': form})


