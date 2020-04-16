# Generated by Django 2.1.15 on 2020-04-08 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='이메일 주소를 입력하시오.', regex='@4anytech.co.kr$')], verbose_name='이메일')),
                ('username', models.CharField(db_column='username', max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='이름을 입력하시오.', regex='^[가-힣]+$')], verbose_name='이름')),
                ('mobile_number', models.CharField(db_column='mobile_number', error_messages={'unique': 'A user with that username already exists.'}, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='휴대전화 번호를 입력하시오.', regex='^[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$')], verbose_name='연락처')),
                ('date_of_birth', models.DateTimeField(db_column='date_of_birth', default='1999-01-01 00:00:00', verbose_name='생년월일')),
                ('gender', models.SmallIntegerField(choices=[(0, 'Not to selected'), (1, 'Male'), (2, 'Female')], default=0)),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_column='date_joined', verbose_name='가입일')),
                ('last_login', models.DateTimeField(auto_now=True, db_column='last_login', verbose_name='마지막 로그인')),
                ('is_active', models.BooleanField(default=False, verbose_name='활성화')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
                ('is_staff', models.BooleanField(default=False, verbose_name='직원')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='슈퍼유저')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'db_table': 'account_custom_user',
            },
        ),
    ]
