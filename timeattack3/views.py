from django.http import HttpResponse
from django.shortcuts import render
import hashlib

def first_view(request):
    return render(request, 'index.html')

class User:
    email = ''
    password = ''


def sign_in_view(request):
    if request.method == 'POST':
        user=User()
        user.email=request.POST.get('email', None)
        password=request.POST.get('password', None)
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user.password=hashed_pw
        if len(user.password) <8:
            return HttpResponse("비밀번호 형식 에러")
        if '@' not in user.email:
            return HttpResponse("이메일 형식 에러")
        return render(request, 'register.html')
