# Generated by Django 2.1.15 on 2020-05-26 02:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(db_column='#', primary_key=True, serialize=False, unique=True, verbose_name='#')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='등록일')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='수정일')),
            ],
            options={
                'verbose_name': '주소',
                'verbose_name_plural': '주소',
                'db_table': 'g_address',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(db_column='#', primary_key=True, serialize=False, unique=True, verbose_name='#')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='등록일')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='수정일')),
                ('company', models.CharField(db_column='company', max_length=64, unique=True, verbose_name='회사명')),
                ('address', models.CharField(blank=True, db_column='address', max_length=255, null=True, verbose_name='주소')),
                ('corporate_registration_number', models.CharField(blank=True, db_column='corporate_registration_number', max_length=12, null=True, unique=True, verbose_name='사업자등록번호')),
                ('business_conditions', models.SmallIntegerField(blank=True, choices=[(None, '업태 선택'), (0, '완료'), (1, '처리'), (2, '보류')], default=None, null=True, verbose_name='업태')),
                ('category_of_business', models.SmallIntegerField(blank=True, choices=[(None, '업종 선택'), (0, '완료'), (1, '처리'), (2, '보류')], default=None, null=True, verbose_name='업종')),
            ],
            options={
                'verbose_name': '고객사 정보',
                'verbose_name_plural': '고객사 정보',
                'db_table': 'g_company',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(db_column='#', primary_key=True, serialize=False, unique=True, verbose_name='#')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='등록일')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='수정일')),
                ('contract_date', models.DateField(blank=True, db_column='contract_date', default=django.utils.timezone.now, null=True, verbose_name='계약 일자')),
                ('salesman', models.CharField(blank=True, db_column='salesman', max_length=32, null=True, verbose_name='담당영업')),
                ('license_type', models.SmallIntegerField(blank=True, choices=[(None, '라이선스 구분'), (0, '영구'), (1, '기간'), (2, '임시')], default=None, null=True, verbose_name='라이선스 구분')),
                ('licenses', models.SmallIntegerField(blank=True, db_column='license', null=True, verbose_name='라이선스')),
                ('license_period_start', models.DateField(blank=True, db_column='license_period_start', default=django.utils.timezone.now, null=True, verbose_name='라이선스 시작 기간')),
                ('license_period_end', models.DateField(blank=True, db_column='license_period_end', default=django.utils.timezone.now, null=True, verbose_name='라이선스 종료 기간')),
                ('contract_type', models.SmallIntegerField(blank=True, choices=[(None, '계약 구분'), (0, '유상'), (1, '무상'), (2, '장애')], default=None, null=True, verbose_name='유지보수 구분')),
                ('contract_period_start', models.DateField(blank=True, db_column='contract_period_start', default=django.utils.timezone.now, null=True, verbose_name='유지보수 시작 기간')),
                ('contract_period_end', models.DateField(blank=True, db_column='contract_period_end', default=django.utils.timezone.now, null=True, verbose_name='유지보수 종료 기간')),
                ('note', models.CharField(blank=True, db_column='note', max_length=255, null=True, verbose_name='비  고')),
            ],
            options={
                'verbose_name': '계약 정보',
                'verbose_name_plural': '계약 정보',
                'db_table': 'g_contract',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(db_column='#', primary_key=True, serialize=False, unique=True, verbose_name='#')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='등록일')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='수정일')),
                ('classification', models.CharField(blank=True, db_column='classification', max_length=32, null=True, verbose_name='구분')),
                ('customer', models.CharField(blank=True, db_column='customer', max_length=16, null=True, unique=True, verbose_name='담당자')),
                ('telephone', models.CharField(blank=True, db_column='telephone', max_length=13, null=True, verbose_name='전화번호')),
                ('cellphone', models.CharField(blank=True, db_column='cellphone', max_length=13, null=True, unique=True, verbose_name='휴대폰')),
                ('email', models.EmailField(blank=True, db_column='email', max_length=64, null=True, unique=True, verbose_name='이메일')),
                ('note', models.CharField(blank=True, db_column='note', max_length=255, null=True, verbose_name='비  고')),
            ],
            options={
                'verbose_name': '고객 정보',
                'verbose_name_plural': '고객 정보',
                'db_table': 'g_customer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='#', primary_key=True, serialize=False, unique=True, verbose_name='#')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='등록일')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='수정일')),
                ('hostname', models.CharField(blank=True, db_column='hostname', max_length=32, null=True, verbose_name='호스트명')),
                ('ip_address', models.GenericIPAddressField(blank=True, db_column='IP', null=True, unique=True, verbose_name='IP')),
                ('product', models.CharField(blank=True, db_column='product', max_length=32, null=True, verbose_name='제품명')),
                ('product_version', models.CharField(blank=True, db_column='product_version', max_length=16, null=True, verbose_name='제품버전')),
                ('minor_version', models.CharField(blank=True, db_column='minor_version', max_length=16, null=True, verbose_name='제품상세버전')),
                ('operating_system', models.CharField(blank=True, db_column='operating_system', max_length=32, null=True, verbose_name='운영체제')),
                ('operating_system_version', models.CharField(blank=True, db_column='operating_system_version', max_length=32, null=True, verbose_name='운영체제 버전')),
                ('webserver', models.CharField(blank=True, db_column='webserver', max_length=32, null=True, verbose_name='웹서버')),
                ('webserver_version', models.CharField(blank=True, db_column='webserver_version', max_length=32, null=True, verbose_name='웹서버 버전')),
                ('webapplicationserver', models.CharField(blank=True, db_column='webapplicationserver', max_length=32, null=True, verbose_name='웹 애플리케이션 서버')),
                ('webapplicationserver_version', models.CharField(blank=True, db_column='webapplicationserver_version', max_length=32, null=True, verbose_name='웹 애플리케이션 서버 버전')),
                ('DBMS', models.CharField(blank=True, db_column='DBMS', max_length=32, null=True, verbose_name='데이터베이스 관리 시스템')),
                ('DBMS_version', models.CharField(blank=True, db_column='DBMS_version', max_length=32, null=True, verbose_name='데이터베이스 관리 시스템 버전')),
                ('note', models.CharField(blank=True, db_column='note', max_length=255, null=True, verbose_name='비  고')),
            ],
            options={
                'verbose_name': '제품 정보',
                'verbose_name_plural': '제품 정보',
                'db_table': 'g_product',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.ForeignKey(db_column='address', on_delete=django.db.models.deletion.CASCADE, related_name='Address', to='crm.Company', verbose_name='주소'),
        ),
    ]