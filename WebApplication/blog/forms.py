from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_summernote import fields as SFields

from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = SFields.SummernoteTextFormField(label='내용',
                                    # input_formats=['%Y/%m/%d %h:%m'],
                                    required=True,
                                    error_messages={
                                        'required': '내용을 입력하시오.'
                                    },
                                    )

    class Meta:
        model = Post
        fields = [
            'author', 'title', 'content', 'image', 'files'
        ]
        labels = {
            'author': '작성자',
            'title': '제목',
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
            # 'content': {
            #     'required': _('내용를 입력하시오.'),
            # },
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
            'content': forms.Textarea(attrs={
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
            'post': '제목',
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
