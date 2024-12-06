from django import forms
from .models import user_profile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = user_profile

        fields = ['role', 
                  'username',
                  'full_name',
                  'phone_number', 
                  'password',
                  'password_confirm']

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')

            # Function to check if the password match

            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Passwords do not match!")
            
            return cleaned_data

    