from django.shortcuts import render, redirect, resolve_url
from django.http.response import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
)

from .models import Company, Customer, Product, Contract
from .forms import CompanyForm, CustomerForm, ProductForm, ContractForm
from .multiform import MultiFormsView

# class CRMCreateView(LoginRequiredMixin, CreateView):
#     # form_class = CompanyForm
#     # form_class1 = CompanyForm
#     # form_class2 = CustomerForm
#     # context_object_name = 'form'
#     template_name = 'crm/Edit.html'
#     login_url = 'sso/Login'
#     success_url = reverse_lazy('blog:list')

#     def get(self, request, *args, **kwargs):
#         super(CRMCreateView, self).get(request, *args, **kwargs)
#         form1 = self.form_class1
#         form2 = self.form_class2
#         return self.render_to_response(
#             self.get_context_data(object=self.object, form=form1, form2=form2)
#         )

#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST' and not bannedphraseform.is_valid():
#             expectedphraseform = CompanyForm(request.POST, prefix='expected')
#             bannedphraseform = CustomerForm(prefix='expected')
#             if expectedphraseform.is_valid():
#                 expectedphraseform.save()

#         else:
#             expectedphraseform = ExpectedPhraseForm(prefix='expected')


class CRMListView(LoginRequiredMixin, ListView):
    template_name = 'crm/List.html'
    # template_name = 'blog/post_list.html'
    # queryset = .objects.all()
    # queryset = Post.objects.all().order_by('-created_at')[:10]
    ordering = ['-created_at']
    # paginate_by = 10
    login_url = 'sso/Login'
    resolve_url = 'user:Login'
    success_url = reverse_lazy('crm:list')


class CRMCreateView(LoginRequiredMixin, MultiFormsView):
    template_name = 'crm/Edit.html'
    login_url = 'sso/Login'
    form_classes = {
        'company': CompanyForm,
        'customer': CustomerForm,
        'product': ProductForm,
        'contract': ContractForm
    }

    success_urls = {
        'company': reverse_lazy('crm:list'),
        'customer': reverse_lazy('crm:list'),
        'product': reverse_lazy('crm:list'),
        'contract': reverse_lazy('crm:list'),
    }

    # def company_form_valid(self, form):
    #     'company form processing goes in here'

    # def customer_form_valid(self, form):
    #     'customer form processing goes in here'

    # def product_form_valid(self, form):
    #     'product form processing goes in here'

    # def contract_form_valid(self, form):
    #     'contract form processing goes in here'        
