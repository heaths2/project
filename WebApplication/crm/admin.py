from django.contrib import admin

from .models import Address, Company, Customer, Contract, Product


class AddressInline(admin.StackedInline):
    model = Address  # 어느 모델을 가져올 것인지
    extra = 1  # 여분 작성 항목은 몇개를 기본으로 표시할 것인지


class CompanyAdmin(admin.ModelAdmin):
    # 표시할 필드의 순서를 조정한다.

    list_display = ['company', 'address', 'corporate_registration_number', 'business_conditions', 'category_of_business']
    fieldsets = [
        (None, {
            'fields': ['company', 'corporate_registration_number', 'business_conditions', 'category_of_business']
        }),
        ('주소', {
            'fields': ['address']
        })
    ]
    inlines = [AddressInline]


admin.site.register(Address)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(Product)