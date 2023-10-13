# user_management/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_management.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and username.startswith('admin'):
            raise forms.ValidationError("Username cannot start with 'admin'.")
        return username

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        # Perform custom validation checks here
        if not mobile.isdigit() or len(mobile) < 10:
            raise forms.ValidationError('Invalid mobile number format.')
        return mobile

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'country', 'nationality', 'mobile', 'password1', 'password2')
