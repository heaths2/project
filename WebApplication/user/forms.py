from django import forms
from django.utils.translation import gettext_lazy as _

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
            'email', 'username', 'mobile_phone', 'date_of_birth', 'gender', 'password',
        ]
        labels = {
            'email': '이메일',
            'username': '이름',
            'mobile_phone': '휴대폰',
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
            'mobile_phone': {
                'required': _('휴대폰번호를 입력하시오.'),
                'ValidationError': _('다른 연락처를 입력하시오.'),
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
            'mobile_phone': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'mobile_phone', 'placeholder': '연락처 : 010-1234-5678', 'type': 'tel',
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
        # cleaned_data = super().clean()
        phone = self.cleaned_data.get('mobile_phone')
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

    def save(self, request):
        user = super(RegisterForm, self).save(commit=False)
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.mobile_phone = request.POST.get('mobile_phone')
        user.date_of_birth = request.POST.get('date_of_birth')
        user.gender = request.POST.get('gender')
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

    def clean_login(self):
        email = self.cleand_data.get('email')
        password = self.cleand_data.get('password')

        if email and password:
            try:
                customuser = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', '입력 값이 옳바르지 않습니다.')
            if not password(password, customuser.password):
                self.add_error('password', '입력 값이 옳바르지 않습니다.')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
