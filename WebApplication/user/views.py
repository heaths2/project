from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView, CreateView
from django.conf import settings
from rest_framework import viewsets, permissions

from .serializers import AccountSerializer
from .forms import RegisterForm, LoginForm
from .models import User


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/Register.html'
    success_url = '/account/Login'

    # forms.Form 경우 유효성 검사 후 save()사용
    # def form_valid(self, form):
    #     customuser = User(
    #         email=form.data.get('email'),
    #         username=form.data.get('username'),
    #         mobile_phone=form.data.get('mobile_phone'),
    #         date_of_birth=form.data.get('date_of_birth'),
    #         gender=form.data.get('gender'),
    #         password=make_password(form.data.get('password')),
    #         is_active=False,
    #         is_admin=False,
    #         is_staff=False,
    #         is_superuser=False
    #     )
    #     customuser.save()

    #     return super(RegisterView, self).form_valid(form)

# def AccountLoginView(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request, request.POST)
#         if login_form.is_valid():
#             auth_login(request, login_form.get_user())
#         return redirect('/admin')
    
#     else:
#         login_form = LoginForm()
    
#     return render(request, 'account/Login.html', {'login_form' : login_form})


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'account/Login.html'

    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.get('email')

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)


class LogoutView(auth_views.LogoutView):
    url = '/account/login'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
