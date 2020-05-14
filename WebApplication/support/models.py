from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.AutoField(
        _('#'),
        db_column='#',
        primary_key=True,
        null=False,
        blank=False,
        unique=True,
        # verbose_name='#',
    )
    created_at = models.DateTimeField(
        _('등록일'),
        db_column='created_at',
        auto_now_add=True,
        null=False,
        blank=False,
        # verbose_name='등록일',
    )
    modified_at = models.DateTimeField(
        _('수정일'),
        db_column='modified_at',
        auto_now=True,
        null=False,
        blank=False,
        # verbose_name='수정일',
    )

    class Meta:
        abstract = True
        # db_table = 'g_support'
        # verbose_name = '필수값'
        # verbose_name_plural = '필수값'
