from django import forms
from .models import Blog

class Blog_Form(forms.Form):
    title = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(
            
        )
    )

    content = forms.CharField(
        max_length = 1000,
        widget = forms.Textarea(
            
        )
    )



