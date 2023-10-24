from django  import forms
from django.contrib import messages


class LoginForm(forms.Form):
    username = forms.CharField(label='username kiriting', required=True, widget=forms.TextInput(attrs={'class': "form-control mb-4"})) 
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': "form-control mb-4"}))
    
    def check_pass(self):
        cleaned_data = super(LoginForm, self).clean()
        password = self.cleaned_data.get("password")
        if (password == ''):
            messages.error("Xato malumot")
        return cleaned_data
    