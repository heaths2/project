# Generated by Django 2.1.15 on 2020-05-28 05:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, db_column='content', null=True, verbose_name='내용'),
        ),
    ]
