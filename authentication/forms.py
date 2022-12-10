from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    password1= forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender',
                  'number_phone', 'bio', 'province', 'city', 'district', 'image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']




class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    password1= forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    password2= forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_lurah", "is_nakes")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user