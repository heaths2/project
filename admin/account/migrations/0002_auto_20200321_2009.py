# Generated by Django 2.1.15 on 2020-03-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, 'Not to selected'), (1, 'Male'), (2, 'Female')], default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True, verbose_name='관리자'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='직원'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True, verbose_name='슈퍼유저'),
        ),
    ]
