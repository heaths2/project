from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView
)

from .models import Company, Customer, Product, Contract
from .forms import CompanyForm, CustomerForm, ProductForm, ContractForm
from .multiform import MultiFormsView


class CRMCreateView(LoginRequiredMixin, CreateView):
    # form_class = CompanyForm
    # form_class1 = CompanyForm
    # form_class2 = CustomerForm
    # context_object_name = 'form'
    template_name = 'crm/Edit.html'
    login_url = 'sso/Login'
    success_url = reverse_lazy('blog:list')

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

# class CRMCreateView(LoginRequiredMixin, MultiFormsView):
#     template_name = 'crm/Edit.html'
#     login_url = 'sso/Login'
#     form_classes = {
#         'company': CompanyForm,
#         'customer': CustomerForm,
#         'product': ProductForm,
#         'contract': ContractForm
#     }

#     success_url = reverse_lazy('blog:list')

