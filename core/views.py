from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'كلمتا المرور غير متطابقتين')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم موجود مسبقًا')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        messages.success(request, 'تم إنشاء الحساب بنجاح')
        return redirect('login')

    return render(request, 'core-app/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'بيانات الدخول غير صحيحة')

    return render(request, 'core-app/login.html')
