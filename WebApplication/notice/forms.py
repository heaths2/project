from django import forms
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget
from django_summernote import fields as SFields

from .models import Post


class PostForm(forms.ModelForm):
    # title = forms.TextInput(
    #     label='제목',
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title', 'placeholder': '제목', 'type': 'text'}),
    #     # input_formats=['%Y/%m/%d %h:%m'],
    #     required=True,
    #     error_messages={'required': '제목을 입력하시오.'},
    # )    
    content = SFields.SummernoteTextFormField(
        label='내용',
        widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'content', 'placeholder': '내용'}),
        # input_formats=['%Y/%m/%d %h:%m'],
        required=True,
        error_messages={'required': '내용을 입력하시오.'},
    )
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
        fields = ['author', 'title', 'content', 'image', 'files']

