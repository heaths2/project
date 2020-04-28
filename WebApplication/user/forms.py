from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from .models import User


class RegisterForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='생년월일',
        # input_formats=['%Y/%m/%d %h:%m'],
        widget=forms.DateInput(attrs={
            'class': 'form-control', 'name': 'date_of_birth', 'placeholder': 'Date Of Birth', 'type': 'date', 'value': '1990-01-01'
        }),
        required=True,
        error_messages={
            'required' : '생년월일을 입력하시오.'
        },
    )
    password2 = forms.CharField(label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name': 'password2', 'placeholder': 'Password Confirm', 'type': 'password',
        }),
        required=True,
        error_messages={
            'required' : '패스워드를 확인 하시오.'
        },
    )

    class Meta:
        model = User
        fields = [
            'email', 'username', 'phone', 'date_of_birth', 'gender', 'password',
        ]
        labels = {
            'email': '이메일',
            'username': '이름',
            'phone': '휴대폰',
            'gender': '성별',
            'password': '비밀번호',
        }
        error_messages = {
            'email': {
                'required': _('이메일 주소를 입력하시오.'),
            },
            'username': {
                'required': _('이름을 입력하시오.'),
            },
            'phone': {
                'required': _('연락처를 입력하시오.'),
            },
            'gender': {
                'required': _('성별을 입력하시오.'),
            },
            'password': {
                'required': _('비밀번호를 입력하시오.'),
            },
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'name': 'email', 'placeholder': 'Email',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'username', 'placeholder': 'Username',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'phone', 'placeholder': '연락처 : 010-1234-5678', 'type': 'tel',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control', 'name': 'gender', 'placeholder': 'Gender',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 'name': 'password', 'placeholder': 'Password',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        queryset = User.objects.filter(email=email)
        if queryset.exists():
	        raise forms.ValidationError('다른 이메일 주소를 입력하시오.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        queryset = User.objects.filter(username=username)
        if queryset.exists():
	        raise forms.ValidationError('다른 이름를 입력하시오.')
        return username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        queryset = User.objects.filter(phone=phone)
        if queryset.exists():
	        raise forms.ValidationError('다른 연락처를 입력하시오.')
        return phone

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('패스워드가 일치하지 않습니다.')
        return password2

    # forms.ModelForm 자동 save() ※중복 저장 주의
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': '이메일',
            'password': '비밀번호',
        }
        error_messages = {
            'email': {
                'required': _('이메일 주소를 입력하시오.'),
            },
            'password': {
                'required': _('비밀번호를 입력하시오.'),
            },
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'name': 'email',
                'placeholder': 'Email',
                'required': 'True',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'name': 'password',
                'placeholder': 'Password',
                'required': 'True',
            }),
        }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.auth_login = authenticate(self.request, email=email, password=password)
            if self.auth_login is None:
                raise forms.ValidationError('다른 이름를 입력하시오.')

        return self.cleaned_data

    # def clean(self, *args, **kwargs):
    #     query = self.cleaned_data.get('query')
    #     password = self.cleaned_data.get('password')
    #     e_qs = User.objects.filter(
    #         Q(email__iexact=query)
    #     ).distinct()
    #     if not e_qs.exists() and e_qs.count != 1:
    #         raise forms.ValidationError('입력 값이 옳바르지 않습니다.')
    #     e_q = e_qs.firse()
    #     if not e_q.check_password(password):
    #         raise forms.ValidationError('입력 값이 옳바르지 않습니다.')
    #     self.cleaned_data['e_q'] = e_q
    #     return supuer(LoginForm, self).clean(*args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super().__init__(*args, **kwargs)

    # def save(self, commit=False):
    #     self.instance = User(**self.cleaned_data)
    #     if commit:
    #         self.instance.save()
    #     return self.instance
