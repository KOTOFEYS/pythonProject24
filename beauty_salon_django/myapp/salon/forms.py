from django import forms
class UserRegister(forms.Form):
    username = forms.CharField(max_length=30)
    num_tel = forms.CharField(max_length=16)
