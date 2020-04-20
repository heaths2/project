from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='이메일', max_length=64,
                             widget=forms.EmailInput,
                             error_messages={
                                 'required': '이메일 주소를 입력하시오.'
                             },
                             )
    username = forms.CharField(label='이름', max_length=8, min_length=2,
                               widget=forms.TextInput,
                               error_messages={
                                   'required': '이름을 입력하시오.'
                               },
                               )
    password1 = forms.CharField(label='비밀번호', max_length=64,
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': '비밀번호를 입력하시오.'
                                },
                                )
    password2 = forms.CharField(label='비밀번호 확인', max_length=64,
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': '비밀번호를 확인하시오.'
                                },
                                )
    mobile_number = forms.CharField(label='연락처', min_length=13, max_length=13,
                                    widget=forms.TextInput,
                                    required=True,
                                    initial=None,
                                    help_text=('ex)010-1234-5678'),
                                    error_messages={
                                        'required': '연락처를 입력하시오.'
                                    },
                                    )
    # date_of_birth = forms.DateField(label='생년월일',
    #     widget=forms.DateInput(),
    #     required=True,
    #     initial= {'date_of_birth':'1970/01/01'},
    #     error_messages={
    #         'required' : '생년월일을 입력하시오.'
    #     },
    # )
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female'))
    )
    gender = forms.ChoiceField(label='성별',
                               choices=GENDER_CHOICES,
                               widget=forms.Select(),
                               required=True,
                               initial=None,
                               error_messages={
                                   'required': '성별을 입력하시오.'
                               },
                               )

    class Meta:
        model = User
        fields = [
            'email', 'username', 'mobile_number', 'gender'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('패스워드가 일치하지 않습니다.')


class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='이메일', max_length=64,
                             error_messages={
                                 'required': '이메일 주소를 입력하시오.'
                             },
                             )
    password = forms.CharField(label='비밀번호',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'wrap-input100 rs1 validate-input', 'placeholder': 'Password', 'data-validate': 'Password is required',
                               }),
                               error_messages={
                                   'required': '비밀번호를 입력하시오.'
                               },
                               )

    class Meta:
        model = User
        fields = [
            'email', 'password'
        ]

    def clean(self):
        cleand_data = super().clean()
        email = cleand_data.get('email')
        password = cleand_data.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoesNotExist:
                self.add_error('email', '입력 값이 옳바르지 않습니다.')
            if not check_password(password, fcuser.password):
                self.add_error('password', '입력 값이 옳바르지 않습니다.')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
