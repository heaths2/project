from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_summernote import models as SModels
from django_summernote import fields as SFields
from ckeditor.fields import RichTextField

from support.models import BaseModel
from user.models import User


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', related_name='authors', db_column='author', blank=False, null=False)
    department = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='부서', related_name='departments', db_column='department', blank=False, null=False)
    STATUS_CHOICES = (
        (None, '처리 상태'),
        (0, '완료'),
        (1, '처리'),
        (2, '보류'),
    )
    status = models.SmallIntegerField(_('status'), choices=STATUS_CHOICES, default=None, blank=False, null=False)
    title = models.CharField(
        db_column='title', verbose_name='제목', max_length=255, blank=False, null=False)
    # content = models.TextField(
    #     db_column='content', verbose_name='내용', blank=True, null=True)
    content = SFields.SummernoteTextField(
        db_column='content', verbose_name='내용', blank=True, null=True)
    # content = RichTextField(
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
        return reverse('blog:list', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'g_blog'
        verbose_name = '블로그'
        verbose_name_plural = '블로그'


class Comment(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='작성자', db_column='author', blank=False, null=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='게시글', db_column='post')
    content = models.TextField(
        db_column='content', verbose_name='내용', blank=True, null=True)

    # def __str__(self):
    #     return '%s. %s' % (self.id, self.post)

    def __str__(self):
        return f'{ self.id }, { self.post }'

    class Meta:
        db_table = 'g_comment'
        verbose_name = '덧글'
        verbose_name_plural = '덧글'
