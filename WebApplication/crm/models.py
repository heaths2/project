from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from support.models import BaseModel


# 고객사 정보
class Company(BaseModel):
    company = models.CharField(_('회사명'), unique=True, blank=False, null=False, db_column='company', max_length=64)
    address = models.CharField(_('주소'), blank=True, null=True, db_column='address', max_length=255)    
    corporate_registration_number = models.CharField(_('사업자등록번호'), unique=True, blank=True, null=True, db_column='corporate_registration_number', max_length=12)
    BUSINESS_CONDITIONS_CHOICES = (
        (None, '업태 선택'),
        (0, '완료'),
        (1, '처리'),
        (2, '보류'),
    )
    business_conditions = models.SmallIntegerField(_('업태'), choices=BUSINESS_CONDITIONS_CHOICES, default=None, blank=True, null=True)
    CATEGORY_OF_BUSINESS_CHOICES = (
        (None, '업종 선택'),
        (0, '완료'),
        (1, '처리'),
        (2, '보류'),
    )
    category_of_business = models.SmallIntegerField(_('업종'), choices=CATEGORY_OF_BUSINESS_CHOICES, default=None, blank=True, null=True)

    def __str__(self):
        return f'{ self.company }  { self.address } { self.corporate_registration_number } { self.business_conditions } { self.category_of_business }'

    class Meta:
        db_table = 'g_company'
        verbose_name = '고객사 정보'
        verbose_name_plural = '고객사 정보'


class Address(BaseModel):
    address = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='Address', verbose_name='주소', db_column='address')

    def __str__(self):
        return f'{ self.address }'

    class Meta:
        db_table = 'g_address'
        verbose_name = '주소'
        verbose_name_plural = '주소'


# 고객 정보
class Customer(BaseModel):
    classification = models.CharField(_('구분'), blank=True, null=True, db_column='classification', max_length=32)
    customer = models.CharField(_('담당자'), unique=True, blank=True, null=True, db_column='customer', max_length=16)
    telephone = models.CharField(_('전화번호'), blank=True, null=True, db_column='telephone', max_length=13)
    cellphone = models.CharField(_('휴대폰'), unique=True, blank=True, null=True, db_column='cellphone', max_length=13)
    email = models.EmailField(_('이메일'), unique=True, blank=True, null=True, db_column='email', max_length=64)
    note = models.CharField(_('비  고'), blank=True, null=True, db_column='note', max_length=255)

    def __str__(self):
        return f'{ self.classification }  { self.customer } { self.telephone } { self.cellphone } { self.email }'

    class Meta:
        db_table = 'g_customer'
        verbose_name = '고객 정보'
        verbose_name_plural = '고객 정보'


# 제품 정보
class Product(BaseModel):
    hostname = models.CharField(_('호스트명'), blank=True, null=True, db_column='hostname', max_length=32)
    ip_address = models.GenericIPAddressField(_('IP'), unique=True, blank=True, null=True, db_column='IP')
    product = models.CharField(_('제품명'), blank=True, null=True, db_column='product', max_length=32)
    product_version = models.CharField(_('제품버전'), blank=True, null=True, db_column='product_version', max_length=16)
    minor_version = models.CharField(_('제품상세버전'), blank=True, null=True, db_column='minor_version', max_length=16)
    operating_system = models.CharField(_('운영체제'), blank=True, null=True, db_column='operating_system', max_length=32)
    operating_system_version = models.CharField(_('운영체제 버전'), blank=True, null=True, db_column='operating_system_version', max_length=32)
    webserver = models.CharField(_('웹서버'), blank=True, null=True, db_column='webserver', max_length=32)
    webserver_version = models.CharField(_('웹서버 버전'), blank=True, null=True, db_column='webserver_version', max_length=32)
    webapplicationserver = models.CharField(_('웹 애플리케이션 서버'), blank=True, null=True, db_column='webapplicationserver', max_length=32)
    webapplicationserver_version = models.CharField(_('웹 애플리케이션 서버 버전'), blank=True, null=True, db_column='webapplicationserver_version', max_length=32)
    DBMS = models.CharField(_('데이터베이스 관리 시스템'), blank=True, null=True, db_column='DBMS', max_length=32)
    DBMS_version = models.CharField(_('데이터베이스 관리 시스템 버전'), blank=True, null=True, db_column='DBMS_version', max_length=32)
    note = models.CharField(_('비  고'), blank=True, null=True, db_column='note', max_length=255)

    def __str__(self):
        return f'{ self.hostname }  { self.ip_address } { self.product }'

    class Meta:
        db_table = 'g_product'
        verbose_name = '제품 정보'
        verbose_name_plural = '제품 정보'


# 계약 정보  
class Contract(BaseModel):
    contract_date = models.DateField(_('계약 일자'), db_column='contract_date', blank=True, null=True, default=timezone.now)
    salesman = models.CharField(_('담당영업'), db_column='salesman', blank=True, null=True, max_length=32)
    LICENSE_TYPE_CHOICES = (
        (None, '라이선스 구분'),
        (0, '영구'),
        (1, '기간'),
        (2, '임시'),
    )
    license_type = models.SmallIntegerField(_('라이선스 구분'), choices=LICENSE_TYPE_CHOICES, default=None, blank=True, null=True)
    licenses = models.SmallIntegerField(_('라이선스'), db_column='license', blank=True, null=True)
    license_period_start = models.DateField(_('라이선스 시작 기간'), db_column='license_period_start', blank=True, null=True, default=timezone.now)
    license_period_end = models.DateField(_('라이선스 종료 기간'), db_column='license_period_end', blank=True, null=True, default=timezone.now)
    CONTRACT_TYPE_CHOICES = (
        (None, '계약 구분'),
        (0, '유상'),
        (1, '무상'),
        (2, '장애'),
    )
    contract_type = models.SmallIntegerField(_('유지보수 구분'), choices=CONTRACT_TYPE_CHOICES, default=None, blank=True, null=True)
    contract_period_start = models.DateField(_('유지보수 시작 기간'), db_column='contract_period_start', blank=True, null=True, default=timezone.now)
    contract_period_end = models.DateField(_('유지보수 종료 기간'), db_column='contract_period_end', blank=True, null=True, default=timezone.now)
    note = models.CharField(_('비  고'), blank=True, null=True, db_column='note', max_length=255)

    def __str__(self):
        return f'{ self.contract_date }  { self.license_type } { self.licenses } { self.license_period_start } { self.license_period_end }'

    class Meta:
        db_table = 'g_contract'
        verbose_name = '계약 정보'
        verbose_name_plural = '계약 정보'