from django import forms

class NameForm(forms.Form):
    fname = forms.CharField(required=True)
    lname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
