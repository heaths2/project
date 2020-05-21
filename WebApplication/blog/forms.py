from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_summernote import fields as SFields
from django_summernote.widgets import SummernoteWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):
    # content = SFields.SummernoteTextFormField(label='내용',
    #                                 # input_formats=['%Y/%m/%d %h:%m'],
    #                                 required=True,
    #                                 error_messages={
    #                                     'required': '내용을 입력하시오.'
    #                                 },
    #                                 )

    # def __init__(self, Post, *args, **kwargs):
    #     self.post = Post
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['author'] = forms.CharField(label='작성자', initial=post.author, required=True)
    #     self.fields['status'] = forms.SmallIntegerField(label='처리상태', initial=post.status, required=True)
    #     self.fields['title'] = forms.CharField(label='제목', initial=post.title, required=True)
    #     self.fields['content'] = forms.CharField(label='내용', initial=post.content, required=True)
    #     self.fields['image'] = forms.ImageField(label='이미지', initial=post.image, required=True)
    #     self.fields['files'] = forms.FileField(label='파일', initial=post.files, required=True)
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['author', 'status', 'title', 'content', 'image', 'files']


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
        
