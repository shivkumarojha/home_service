from django import forms
from .models import Enquiry, Newsletter

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'mobile_number', 'address','select_service']
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['name'].widget.attrs.update(
    #         {
    #             'class': 'form-control bg-dark text-white',                'placeholder': 'Email'
    #         }
    #     )
    
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
