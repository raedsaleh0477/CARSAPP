from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),

    # تسجيل الخروج (جاهز من Django)
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
