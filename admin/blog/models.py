from django.db import models
from django.utils.translation import gettext_lazy as _

from support.models import BaseModel
from account.models import User


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', db_column='author')
    title = models.CharField(db_column='title', verbose_name='제목', max_length=255, blank=False, null=False)
    content = models.TextField(db_column='content', verbose_name='내용', blank=True, null=True)
    # 저장경로, MEDIA_ROOT/blog/2017/05/10/xxxx.jpg 경로에 저장
	# DB필드, 'MEDIA_URL/blog/2017/05/10/xxxx.jpg' 문자열 저장
    # image = models.ImageField(db_column='image', verbose_name='이미지', blank=True, null=True, upload_to='blog/image/%Y%m%d/%H%M%S')
    image = models.ImageField(db_column='image', verbose_name='이미지', blank=True, null=True, upload_to='blog/image/%Y%m%d/')
    # files = models.FileField(db_column='files', verbose_name='첨부파일', blank=True, null=True, upload_to='blog/files/%Y%m%d/%H%M%S')
    files = models.FileField(db_column='files', verbose_name='첨부파일', blank=True, null=True, upload_to='blog/file/%Y%m%d/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project_blog'
        verbose_name = '블로그'
        verbose_name_plural = '블로그'


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글', db_column='post')
    content = models.TextField(db_column='content', verbose_name='내용', blank=True, null=True)

    class Meta:
        db_table = 'project_blog_comment'
        verbose_name = '덧글'
        verbose_name_plural = '덧글'