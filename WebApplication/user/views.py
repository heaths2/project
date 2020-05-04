from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView, CreateView
from django.contrib import messages
from django.conf import settings
from rest_framework import viewsets, permissions

from .serializers import AccountSerializer
from .forms import RegisterForm, LoginForm
from .models import User


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/Register.html'
    success_url = '/account/Login'

# def AccountLoginView(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request, request.POST)
#         if login_form.is_valid():
#             auth_login(request, login_form.get_user())
#         return redirect('/admin')
    
#     else:
#         login_form = LoginForm()
    
#     return render(request, 'account/Login.html', {'login_form' : login_form})


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/blog/list'
    template_name = 'account/Login.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(auth_views.LogoutView):
    url = '/account/login'

    def get(self, request, *args, **kwargs):
        if request.session['user']:
            logout(request)
            del (request.session['user'])

        return super(LogoutView, self).get(request, *args, **kwargs)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
