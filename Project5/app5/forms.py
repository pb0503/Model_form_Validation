from django import forms
from.models import Resident
from django.core import validators

class ResidentForm(forms.ModelForm):
    class Meta:
        model=Resident
        fields='__all__'

        labels={
            'flat_no':' Enter flat No',
            'full_name':'ENTER FULL NAME',
            'society_name':'ENTER SOCIETY NAME',
            'wing_name': 'ENTER Wing name'}

        widgets={
             
            'flat_no':forms.NumberInput(
                attrs={
                       'class':'form-control'}),
            'full_name':forms.TextInput(
                attrs={
                       'class':'form-control'}),
            'wing_name':forms.TextInput(
                attrs={
                       'class':'form-control'}),
            'society_name':forms.TextInput(
                attrs={
                       'class':'form-control'})          
        }

    def clean_full_name(self):
        fnm=self.cleaned_data['full_name']
        if fnm.istitle()!=True:
            raise validators.ValidationError('First Character has to be in Upper Case')
        return fnm
    
    def clean_society_name(self):
        snm=self.cleaned_data['society_name']
        if snm.istitle()!=True:
            raise validators.ValidationError('First Character has to be in Upper Case')
        return snm
    def clean_wing_name(self):
        wnm=self.cleaned_data['wing_name']
        if wnm.istitle()!=True:
            raise validators.ValidationError('First Character has to be in Upper Case')
        return wnm




