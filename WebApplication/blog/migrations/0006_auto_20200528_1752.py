# Generated by Django 2.1.15 on 2020-05-28 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200528_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, related_name='작성자', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.ForeignKey(db_column='department', on_delete=django.db.models.deletion.CASCADE, related_name='부서', to=settings.AUTH_USER_MODEL, verbose_name='부서'),
        ),
    ]
