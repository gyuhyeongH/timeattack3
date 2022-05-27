from django.http import HttpResponse
from django.shortcuts import render


def first_view(request):
    return render(request, 'index.html')

class User:
    email = ''
    password = ''


def sign_in_view(request):
    if request.method == 'POST':
        user=User()
        user.email=request.POST.get('email', None)
        user.password=request.POST.get('password', None)
        return render(request, 'index.html')
