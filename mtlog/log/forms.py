from django.forms import ModelForm
from log.models import log_page_model

class log_form(ModelForm):
    class Meta:
        model = log_page_model        
