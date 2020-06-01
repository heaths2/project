from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget
from django_summernote import fields as SFields

from .models import Post, Comment


class PostForm(forms.ModelForm):
    # author = forms.CharField(
    #     label='작성자',
    #     widget=forms.Select(attrs={'class': 'form-control', 'name': 'author', 'placeholder': '작성자', 'type': 'text'}),
    #     required=True,
    #     error_messages={'required': '작성자를 입력하시오.'},
    # )

    # DEPARTMENT_CHOICES = (
    #     (None, '부서 선택'),
    #     (0, '경영지원'),
    #     (1, '영업'),
    #     (2, '1팀'),
    #     (3, '2팀'),
    # )    
    # department = forms.ChoiceField(
    #     choices=DEPARTMENT_CHOICES,
    #     initial={'department': '부서 선택'},
    #     label='부서',
    #     widget=forms.Select(attrs={'class': 'form-control', 'name': 'department', 'placeholder': '부서', 'type': 'text'}),
    #     required=False,
    #     error_messages={'required': '부서를 선택하시오.'},
    # )    

    class Meta:
        model = Post
        fields = ['author', 'department', 'status', 'title', 'content', 'image', 'files']


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
        
