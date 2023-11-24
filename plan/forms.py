import username as username
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput


class CustomUserCreationForm(UserCreationForm):
   # email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['class'] = 'form-control'

        # self.fields[fieldname].labels = None

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'})
        }
