from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from django.http.response import HttpResponseRedirect, HttpResponseForbidden


class MultiFormMixin(ContextMixin):

    """
    Register all from classes in this directory.
    Example: form_classes = {
                'form_name1': form_class1,
                'form_name2': form_class2
            }
    """
    form_classes = {}

    """
    Register a prefix for a form.
    Example: prefixes = {
                'form_name1': 'prefix1',
                'form_name2': 'prefix2'
            }
    """
    prefixes = {}

    """
    Register a success URL for each form name.
    Example: success_urls = {
                'form_name1': 'url1',
                'form_name2': 'url2'
            }
    """
    success_urls = {}

    """
    Register initials for this view.
    Example: initial = {'subject': 'Hi there!'}
    """    
    initial = {}

    """
    Here you can specify a global prefix for all forms in this view.
    """
    prefix = None

    """
    Here you can specify a global success URL for all forms in this view.
    """    
    success_url = None
     
    def get_form_classes(self):
        return self.form_classes
     
    def get_forms(self, form_classes):
        """
        Get a dictionary (form_name, form_class) with the forms that are specified by the parameter form_names.
        """        
        return dict([(key, self._create_form(key, class_name)) \
            for key, class_name in form_classes.items()])
    
    def get_form_kwargs(self, form_name):
        """
        Setup the kwargs for a form.
        """        
        kwargs = {}
        kwargs.update({'initial':self.get_initial(form_name)})
        kwargs.update({'prefix':self.get_prefix(form_name)})
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs
    
    def forms_valid(self, forms, form_name):
        """
        If the form is valid, redirect to the supplied URL.
        """        
        form_valid_method = '%s_form_valid' % form_name
        if hasattr(self, form_valid_method):
            return getattr(self, form_valid_method)(forms[form_name])
        else:
            return HttpResponseRedirect(self.get_success_url(form_name))
     
    def forms_invalid(self, forms):
        """
        If the form is invalid, redirect to the response.
        """        
        return self.render_to_response(self.get_context_data(forms=forms))
    
    def get_initial(self, form_name):
        """
        For each form a initial method can be declared.
        It is run when the form is created.
        The method MUST return a dictionary with the initial values.
        """    
        initial_method = 'get_%s_initial' % form_name
        if hasattr(self, initial_method):
            return getattr(self, initial_method)()
        else:
            return {'action': form_name}
        
    def get_prefix(self, form_name):
        """
        Returns the prefix for a specific form.
        Or if not defined, the global prefix.
        """        
        return self.prefixes.get(form_name, self.prefix)
        
    def get_success_url(self, form_name=None):
        """
        Returns the success URL for a specific form.
        Or if not defined, the global success URL.
        """        
        return self.success_urls.get(form_name, self.success_url)
    
    def _create_form(self, form_name, form_class):
        """
        This method creates a from.
        """        
        form_kwargs = self.get_form_kwargs(form_name)
        form = form_class(**form_kwargs)
        return form


class ProcessMultipleFormsView(ProcessFormView):
    """
    This class handles the POST and GET requests for the forms.
    """

    def get(self, request, *args, **kwargs):
        """
        The GET request renders the specified forms.
        When overriding this method please call super()
        """        
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))
     
    def post(self, request, *args, **kwargs):
        """
        The POST request calls the handles the form(s) and checks if it's valid.
        When overriding this method please call super()
        """        
        form_classes = self.get_form_classes()
        form_name = request.POST.get('action')
        return self._process_individual_form(form_name, form_classes)
        
    def _process_individual_form(self, form_name, form_classes):
        """
        Perform the is_valid() check for a single form.
        """        
        forms = self.get_forms(form_classes)
        form = forms.get(form_name)
        if not form:
            return HttpResponseForbidden()
        elif form.is_valid():
            return self.forms_valid(forms, form_name)
        else:
            return self.forms_invalid(forms)
 
 
class BaseMultipleFormsView(MultiFormMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """

 
class MultiFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaying several forms, and rendering a template response.
    """