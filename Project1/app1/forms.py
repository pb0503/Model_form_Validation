from django import forms
from.models import Patient
from django.core import validators

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

        labels={'patient_id':' Enter Paient ID',
            'f_name':'ENTER FIRST NAME',
            'email':'ENTER EMAIL ID',
            'l_name': 'ENTER LAST name',
            'age':'ENTER AGE' }
        widgets={'patient_id':forms.NumberInput(
                attrs={'class':'form-control'}),       
            'f_name':forms.TextInput(
                attrs={'class':'form-control'}),        
            'email':forms.EmailInput(
                attrs={'class':'form-control'}),         
            'l_name':forms.TextInput(
                attrs={'class':'form-control'}),         
            'age':forms.NumberInput(
                attrs={'class':'form-control'}) }
    def clean_patient_id(self):
        pi=self.cleaned_data['patient_id']
        if pi>100:
            raise validators.ValidationError('Patient Id should be below 100')
        return pi
      
    def clean_f_name(self):
        fnm=self.cleaned_data['f_name']
        if fnm.istitle()!=True:
            raise validators.ValidationError('First Character has to be in Upper Case')
        return fnm
    
    def clean_l_name(self):
        lnm=self.cleaned_data['l_name']
        if lnm.istitle()!=True:
            raise validators.ValidationError('First Character has to be in Upper Case')
        return lnm

