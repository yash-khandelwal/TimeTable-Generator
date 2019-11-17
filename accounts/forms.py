from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model, authenticate
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts import models
from django.utils.translation import ugettext_lazy as _
import unicodedata

class LoginForm(AuthenticationForm):
    """
    This form is linked with model User, it determines the fields in log in page
    """
    model = models.User
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

class SignupForm(UserCreationForm):
    """
    it determines the fields in  sign up page
    """

    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = models.User
        fields = ('first_name','last_name', 'phone_no', 'email', 'password1', 'password2')

    def clean_email(self):
        """
        Checks if email is already in use
        """
        email = self.cleaned_data.get('email')

        if email in models.User.objects.all().values_list('email', flat=True) or email in models.User.objects.all().values_list('email', flat=True):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return email
    # def clean_address(self):
    #     address = self.cleaned_data.get('address')
    #     if 'save_as_draft' in self.data:
    #         return address
    #     elif 'submit_application' in self.data:
    #         if (address == ''):
    #             raise forms.ValidationError(_("Address is required"))
    #         return address
