from django import forms
from django.contrib import messages
# def validate_email_domain(value):
#     print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",flush=True)
#     if not value.endswith("@gmail.com"):
#         raise forms.ValidationError(
#             "Email must be a Gmail address."
#         )
    # print(value)
    # توضیح باگ سرویس


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=254,required=False)
    last_name = forms.CharField(max_length=254,required=False)
    email = forms.EmailField(required=False,max_length=20)
    bio = forms.CharField(widget=forms.Textarea,required=False)
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be from the domain '@gmail.com'.")
        return email
    
    
    def clean(self):
        cleaned_data = super().clean()
        lastname = cleaned_data.get('last_name')
        if lastname and not lastname.isalpha():
            raise forms.ValidationError("Last name must contain only alphabetic characters.")
        return cleaned_data