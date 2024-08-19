import random
from django.shortcuts import render

def generate_password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+-=[]{}|;:,.<>?')
    if request.GET.get('numbers'):
        characters.extend('0123456789')

    length = int(request.GET.get('length', 12))
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return render(request, 'password.html', {'password': password})

def home(request):
    return render(request, 'home.html')