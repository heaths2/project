from django import forms
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget
from django_summernote import fields as SFields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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
    image = forms.ImageField(
        label='이미지',
        initial=None,
        widget=forms.FileInput(attrs={'class': 'form-control-file', 'name': 'image', 'placeholder': '이미지', 'type': 'file'}),
        required=True,
        error_messages={'required': '이미지를 업로드하시오.'},
    )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        # self.fields['image'].widget.attrs.update({'class': 'form-control', 'type': 'file'})
        # self.fields['files'].widget.attrs.update({'class': 'form-control'})
        # self.helper = FormHelper()
        # self.helper.form_tag = False
        # self.helper.disable_csrf = True
        # self.helper.layout = Layout(
        #     'title',
        #     'content',
        #     'image',
        #     HTML("""{% if form.image.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.image.value }}">{% endif %}""",),
        #     'flag_featured',
        # )        

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'image', 'files']

