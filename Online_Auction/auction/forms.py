from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user_profile


class Custom_user_registration_form(UserCreationForm):
    email = forms.EmailField(required=True, widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Eric'}))
    last_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'developer'}))
    role = forms.ChoiceField(choices=user_profile.role, required=True, widget=forms.Select(attrs={'class': 'form-control,'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        def save(self, commit = True):
            user  = super(). save(commit = False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
                user_profile.objects.create(user = user, role = self.cleaned_data['role'])

            return user


        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email = email).exists():
                raise forms.ValidationError("This email is already in use.")
            
            return email