from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_summernote import fields as SFields
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from support.models import BaseModel
from user.models import User


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자',
                               db_column='author', blank=False, null=False)
    title = models.CharField(
        db_column='title', verbose_name='제목', max_length=255, blank=False, null=False)
    # content = models.TextField(
    #     db_column='content', verbose_name='내용', blank=True, null=True)
    content = SFields.SummernoteTextField(
        db_column='content', verbose_name='내용', blank=True, null=True)
    # content = RichTextField(
    #     db_column='content', verbose_name='내용', blank=True, null=True)
    # content = RichTextUploadingField(
    #     db_column='content', verbose_name='내용', blank=True, null=True)        
    # 저장경로, MEDIA_ROOT/blog/2017/05/10/xxxx.jpg 경로에 저장
    # DB필드, 'MEDIA_URL/blog/2017/05/10/xxxx.jpg' 문자열 저장
    # image = models.ImageField(db_column='image', verbose_name='이미지', blank=True, null=True, upload_to='blog/image/%Y%m%d/%H%M%S')
    image = models.ImageField(db_column='image', verbose_name='이미지',
                              blank=True, null=True, upload_to='blog/image/%Y%m%d/')
    # files = models.FileField(db_column='files', verbose_name='첨부파일', blank=True, null=True, upload_to='blog/files/%Y%m%d/%H%M%S')
    files = models.FileField(db_column='files', verbose_name='첨부파일',
                             blank=True, null=True, upload_to='blog/file/%Y%m%d/')

    def __str__(self):
        return "{0}".format(self.title)

    def get_absolute_url(self):
        return reverse('notice:list', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'g_notice'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'
