from django import forms
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from .models import Address, Company, Customer, Product, Contract


class CompanyForm(forms.ModelForm):
    company = forms.CharField(label='회사명',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'company', 'placeholder': '회사명', 'type': 'text'}),
        required=True,
        error_messages={'required': '회사명을 입력하시오.'},
    )
    address = forms.CharField(label='주소',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'address', 'placeholder': '주소', 'type': 'text'}),
        required=True,
        error_messages={'required': '주소을 입력하시오.'},
    )
    corporate_registration_number = forms.CharField(label='사업자등록번호',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'corporate_registration_number', 'placeholder': '사업자등록번호', 'type': 'text'}),
        required=True,
        error_messages={'required': '사업자등록번호을 입력하시오.'},
    )
    business_conditions = forms.CharField(label='업태',
        widget=forms.Select(attrs={'class': 'form-control', 'name': 'category_of_business', 'placeholder': '업태', 'type': 'text'}),
        required=True,
        error_messages={'required': '업태를 선택하시오.'},
    )
    category_of_business = forms.CharField(label='업종',
        widget=forms.Select(attrs={'class': 'form-control', 'name': 'category_of_business', 'placeholder': '업종', 'type': 'text'}),
        required=True,
        error_messages={'required': '업종을 입력하시오.'},
    )

    class Meta:
        model = Company
        fields = ['company', 'address', 'corporate_registration_number', 'business_conditions', 'category_of_business']

    def clean_company(self):
        company = self.cleaned_data.get('company')
        queryset = Company.objects.filter(company=company)
        if queryset.exists():
	        raise forms.ValidationError('다른 회사명을 입력하시오.')
        return company

    def clean_address(self):
        address = self.cleaned_data.get('address')
        queryset = Company.objects.filter(address=address)
        if queryset.exists():
	        raise forms.ValidationError('다른 주소를 입력하시오.')
        return address

    def clean_crn(self):
        crn = self.cleaned_data.get('corporate_registration_number')
        queryset = Company.objects.filter(crn=crn)
        if queryset.exists():
	        raise forms.ValidationError('다른 사업자등록번호를 입력하시오.')
        return crn

    def clean_bc(self):
        bc = self.cleaned_data.get('business_conditions')
        queryset = Company.objects.filter(bc=bc)
        if queryset.exists():
	        raise forms.ValidationError('다른 업태를 입력하시오.')
        return bc

    def clean_cob(self):
        cob = self.cleaned_data.get('category_of_business')
        queryset = Company.objects.filter(cob=cob)
        if queryset.exists():
	        raise forms.ValidationError('다른 업종을 입력하시오.')
        return cob


AddressFormSet = forms.formset_factory(CompanyForm, extra=3, can_delete=True)


class CustomerForm(forms.ModelForm):
    classification = forms.CharField(label='구분',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'classification', 'placeholder': '구분', 'type': 'text', }),
        required=True,
        error_messages={'required': '구분을 입력하시오.'},
    )
    customer = forms.CharField(label='담당자',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'customer', 'placeholder': '담당자', 'type': 'text', }),
        required=True,
        error_messages={'required': '담당자를 입력하시오.'},
    )
    telephone = forms.CharField(label='전화번호',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'telephone', 'placeholder': '전화번호', 'type': 'text', }),
        required=True,
        error_messages={'required': '전화번호를 입력하시오.'},
    )
    cellphone = forms.CharField(label='휴대폰',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'cellphone', 'placeholder': '휴대폰', 'type': 'text', }),
        required=True,
        error_messages={'required': '휴대폰를 선택하시오.'},
    )
    email = forms.EmailField(label='이메일',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': '이메일', 'type': 'email', }),
        required=True,
        error_messages={'required': '이메일을 입력하시오.'},
    )
    note = forms.CharField(label='비  고',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'note', 'placeholder': '비  고', 'type': 'text', }),
        required=True,
        error_messages={'required': '비  고를 선택하시오.'},
    )    

    class Meta:
        model = Customer
        fields = ['classification', 'customer', 'telephone', 'cellphone', 'email', 'note']


class ProductForm(forms.ModelForm):
    hostname = forms.CharField(label='호스트명',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'hostname', 'placeholder': '호스트명', 'type': 'text'}),
        required=True,
        error_messages={'required': '회사명을 입력하시오.'},
    )
    ip_address = forms.GenericIPAddressField(label='IP Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'address', 'placeholder': 'xxx.xxx.xxx.xxx', 'type': 'text'}),
        required=True,
        error_messages={'required': 'IP주소을 입력하시오.'},
    )
    product = forms.CharField(label='제품명',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'product', 'placeholder': '제품명', 'type': 'text'}),
        required=True,
        error_messages={'required': '제품명을 입력하시오.'},
    )
    product_version = forms.CharField(label='제품버전',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'product_version', 'placeholder': '제품버전', 'type': 'text'}),
        required=True,
        error_messages={'required': '제품버전을 선택하시오.'},
    )
    minor_version = forms.CharField(label='제품상세버전',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'minor_version', 'placeholder': '제품상세버전', 'type': 'text'}),
        required=True,
        error_messages={'required': '제품명을 입력하시오.'},
    )
    operating_system = forms.CharField(label='운영체제',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'operating_system', 'placeholder': '운영체제', 'type': 'text'}),
        required=True,
        error_messages={'required': '운영체제를 선택하시오.'},
    )
    operating_system_version = forms.CharField(label='운영체제 버전',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'product', 'placeholder': '운영체제 버전', 'type': 'text'}),
        required=True,
        error_messages={'required': '운영체제 버전을 입력하시오.'},
    )
    webserver = forms.CharField(label='웹서버',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'webserver', 'placeholder': '웹서버', 'type': 'text'}),
        required=True,
        error_messages={'required': '웹서버를 선택하시오.'},
    )
    webserver_version = forms.CharField(label='웹서버 버전',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'webserver', 'placeholder': '웹서버 버전', 'type': 'text'}),
        required=True,
        error_messages={'required': '웹서버 버전을 선택하시오.'},
    )
    webapplicationserver = forms.CharField(label='웹 애플리케이션 서버',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'webapplicationserver', 'placeholder': '웹 애플리케이션 서버', 'type': 'text'}),
        required=True,
        error_messages={'required': '웹서버를 선택하시오.'},
    )
    webapplicationserver_version = forms.CharField(label='웹 애플리케이션 서버 버전',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'webapplicationserver_version', 'placeholder': '웹 애플리케이션 서버 버전', 'type': 'text'}),
        required=True,
        error_messages={'required': '웹서버 버전을 선택하시오.'},
    )            
    DBMS = forms.CharField(label='데이터베이스 관리 시스템',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'DBMS', 'placeholder': '데이터베이스 관리 시스템', 'type': 'text'}),
        required=True,
        error_messages={'required': '데이터베이스 관리 시스템을 선택하시오.'},
    )
    DBMS_version = forms.CharField(label='데이터베이스 관리 시스템 버전',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'DBMS_version', 'placeholder': '데이터베이스 관리 시스템 버전', 'type': 'text'}),
        required=True,
        error_messages={'required': '데이터베이스 관리 시스템 버전을 선택하시오.'},
    )
    note = forms.CharField(label='비  고',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'note', 'placeholder': '비  고', 'type': 'text', }),
        required=True,
        error_messages={'required': '비  고를 선택하시오.'},
    )   

    class Meta:
        model = Company
        fields = ['hostname', 'ip_address', 'product', 'product_version', 'minor_version', 'operating_system', 'operating_system_version', 'webserver', 'webserver_version', 'webapplicationserver', 'webapplicationserver_version', 'DBMS', 'DBMS_version', 'note']

    def clean_hostname(self):
        hostname = self.cleaned_data.get('hostname')
        queryset = Company.objects.filter(hostname=hostname)
        if queryset.exists():
	        raise forms.ValidationError('다른 호스트명을 입력하시오.')
        return hostname

    def clean_ip(self):
        ip_address = self.cleaned_data.get('ip_address')
        queryset = Company.objects.filter(ip=ip_address)
        if queryset.exists():
	        raise forms.ValidationError('다른 IP주소를 입력하시오.')
        return address


class ContractForm(forms.ModelForm):
    contract_date = forms.DateField(label='계약 일자',
        widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'contract_date', 'placeholder': '계약 일자', 'type': 'date'}),
        required=True,
        error_messages={'required': '회사명을 입력하시오.'},
    )
    salesman = forms.CharField(label='담당영업',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'salesman', 'placeholder': '담당영업', 'type': 'text'}),
        required=True,
        error_messages={'required': '제품명을 입력하시오.'},
    )    
    license_type = forms.IntegerField(label='라이선스 구분',
        widget=forms.Select(attrs={'class': 'form-control', 'name': 'license_type', 'placeholder': '라이선스 구분', 'type': 'text'}),
        required=True,
        error_messages={'required': '라이선스 구분을 입력하시오.'},
    )
    licenses = forms.IntegerField(label='라이선스',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'licenses', 'placeholder': '라이선스', 'type': 'number'}),
        required=True,
        error_messages={'required': '라이선스를 입력하시오.'},
    )
    license_period_start = forms.DateField(label='라이선스 시작 기간',
        widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'license_period_start', 'placeholder': '라이선스 시작 기간', 'type': 'date'}),
        required=True,
        error_messages={'required': '라이선스 시작 기간을 선택하시오.'},
    )
    license_period_end = forms.DateField(label='라이선스 종료 기간',
        widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'license_period_end', 'placeholder': '라이선스 종료 기간', 'type': 'date'}),
        required=True,
        error_messages={'required': '라이선스 종료 기간을 입력하시오.'},
    )
    contract_type = forms.IntegerField(label='계약 구분',
        widget=forms.Select(attrs={'class': 'form-control', 'name': 'contract_type', 'placeholder': '운영체제', 'type': 'text'}),
        required=True,
        error_messages={'required': '계약 구분을 선택하시오.'},
    )
    contract_period_start = forms.DateField(label='계약 시작 기간',
        widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'contract_period_start', 'placeholder': '계약 시작 기간', 'type': 'date'}),
        required=True,
        error_messages={'required': '계약 시작 기간을 입력하시오.'},
    )
    contract_period_end = forms.DateField(label='계약 종료 기간',
        widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'contract_period_end', 'placeholder': '계약 종료 기간', 'type': 'date'}),
        required=True,
        error_messages={'required': '계약 종료 기간을 선택하시오.'},
    )
    note = forms.CharField(label='비  고',
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'note', 'placeholder': '비  고', 'type': 'text', }),
        required=True,
        error_messages={'required': '비  고를 선택하시오.'},
    )   

    class Meta:
        model = Company
        fields = ['contract_date', 'salesman', 'license_type', 'licenses', 'license_period_start', 'license_period_end', 'contract_type', 'contract_period_start', 'contract_period_end', 'note']

    def clean_hostname(self):
        hostname = self.cleaned_data.get('hostname')
        queryset = Company.objects.filter(hostname=hostname)
        if queryset.exists():
	        raise forms.ValidationError('다른 호스트명을 입력하시오.')
        return hostname

    def clean_ip(self):
        ip_address = self.cleaned_data.get('ip_address')
        queryset = Company.objects.filter(ip=ip_address)
        if queryset.exists():
	        raise forms.ValidationError('다른 IP주소를 입력하시오.')
        return address

        