from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from rest_framework import viewsets, permissions

from .serializers import AccountSerializer
from .forms import RegisterForm, LoginForm
from .models import User


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/Register.html'
    success_url = '/Login'
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        customuser = User(
            email=form.data.get('email'),
            username=form.data.get('username'),
            mobile_number=form.data.get('mobile_number'),
            date_of_birth=form.data.get('date_of_birth'),
            gender=form.data.get('gender'),
            password=make_password(form.data.get('password')),
            is_active=False,
            is_admin=False,
            is_staff=False,
            is_superuser=False
        )
        customuser.save()

        return super(RegisterView, self).form_valid(form)


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/Login.html'
    # context_object_name = 'forms'


class LogoutView(LogoutView):
    pass


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
