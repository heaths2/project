from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, username, password=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_acitive', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='이메일', db_column='email', max_length=254, unique=True, blank=False, null=False,
        validators=[
            RegexValidator(
                # r'@4anytech.co.kr$',
                regex=r'@4anytech.co.kr$',
                message=_('이메일 주소를 입력하시오.'),
            ),
        ]
    )

    username = models.CharField(verbose_name='이름', db_column='username', max_length=8, unique=True, blank=False, null=False,
        validators=[
            RegexValidator(
                regex=r'^[가-힣]+$',
                message=_('이름을 입력하시오.'),
            ),
        ]
    )

    mobile_number = models.CharField(verbose_name='연락처', db_column='mobile_number', max_length=13, unique=True, blank=False, null=False,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$',
                message=_('휴대전화 번호를 입력하시오.'),
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    date_of_birth = models.DateTimeField(verbose_name='생년월일', db_column='date_of_birth', default='1999-01-01 00:00:00', blank=False, null=False)

    GENDER_CHOICES = (
        (0, 'Not to selected'),
        (1, 'Male'),
        (2, 'Female')
    )

    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)

    date_joined = models.DateTimeField(verbose_name='가입일', db_column='date_joined', auto_now_add=True, blank=False, null=False)
    last_login = models.DateTimeField(verbose_name='마지막 로그인', db_column='last_login', auto_now=True, blank=False, null=False)

    is_active = models.BooleanField(default=False, null=False, blank=False, verbose_name='활성화')
    is_admin = models.BooleanField(default=False, null=False, blank=False, verbose_name='관리자')
    is_staff = models.BooleanField(default=False, null=False, blank=False, verbose_name='직원')
    is_superuser = models.BooleanField(default=False, null=False, blank=False, verbose_name='슈퍼유저')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')
        db_table = 'g_account_custom_user'