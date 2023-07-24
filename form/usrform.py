from django import forms
from django.forms import ModelForm
from .models import form



class usrform(ModelForm):
    class Meta:
        model = form
        fields = ('name','number','email','destination','budget')
        labels ={
            'name': '',
            'number':'',
            'email':'',
            'destination':'',
            'budget':'',
        

        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'FULL NAME'}),
            'number':forms.TextInput(attrs={'class':'form-control','placeholder':'TELEPHONE'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'E-MAIL'}),
            'destination':forms.TextInput(attrs={'class':'form-control','placeholder':'DESTINATION'}),
            'budget':forms.TextInput(attrs={'class':'form-control','placeholder':'BUDGET'}),
        }