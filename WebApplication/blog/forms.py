from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import Post, Comment


class PostForm(forms.ModelForm):
    # date_of_birth = forms.DateField(label='생년월일',
    #                                 # input_formats=['%Y/%m/%d %h:%m'],
    #                                 widget=forms.DateInput(attrs={
    #                                     'class': 'form-control', 'name': 'date_of_birth', 'placeholder': 'Date Of Birth', 'type': 'date', 'value': '1990-01-01'
    #                                 }),
    #                                 required=True,
    #                                 error_messages={
    #                                     'required': '생년월일을 입력하시오.'
    #                                 },
    #                                 )
    # password2 = forms.CharField(label='비밀번호 확인',
    #                             widget=forms.PasswordInput(attrs={
    #                                 'class': 'form-control', 'name': 'password2', 'placeholder': 'Password Confirm', 'type': 'password',
    #                             }),
    #                             required=True,
    #                             error_messages={
    #                                 'required': '패스워드를 확인 하시오.'
    #                             },
    #                             )

    class Meta:
        model = User
        fields = [
            'author', 'title', 'content', 'image', 'files'
        ]
        labels = {
            'author': '작성자',
            'title': '제목'',
            'content': '내용',
            'image': '이미지',
            'files': '파일',
        }
        error_messages = {
            'author': {
                'required': _('작성자를 입력하시오.'),
            },
            'title': {
                'required': _('이름을 입력하시오.'),
            },
            'content': {
                'required': _('연락처를 입력하시오.'),
            },
            'image': {
                'required': _('성별을 입력하시오.'),
            },
            'files': {
                'required': _('비밀번호를 입력하시오.'),
            },
        }
        widgets = {
            'author': forms.EmailInput(attrs={
                'class': 'form-control', 'name': 'author', 'placeholder': 'Author',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'title', 'placeholder': 'Title',
            }),
            'content': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'content', 'placeholder': 'content',
            }),
            'image': forms.Select(attrs={
                'class': 'form-control', 'name': 'image', 'placeholder': 'Image',
            }),
            'files': forms.PasswordInput(attrs={
                'class': 'form-control', 'name': 'files', 'placeholder': 'Files',
            }),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'author', 'post', 'content',
        ]
        labels = {
            'author': '작성자',
            'post': '제목'',
            'content': '내용',
        }
        error_messages = {
            'author': {
                'required': _('작성자를 입력하시오.'),
            },
            'post': {
                'required': _('이름을 입력하시오.'),
            },
            'content': {
                'required': _('덧글을 입력하시오.'),
            },
        }
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control', 'name': 'content', 'placeholder': 'content', 'required': 'True',
            }),
        }
