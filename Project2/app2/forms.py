from django import forms
from.models import Employee
from django.core import validators

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        labels={
            'emp_id':'ENTER Emp Id.',
            'f_name':'ENTER FIRST NAME',
            'email':'ENTER EMAIL ID',
            'l_name': 'ENTER LAST name',
            'age':'ENTER AGE'}
        widgets={
            'emp_id':forms.NumberInput(
                attrs={'class':'form-control'}),        
            'f_name':forms.TextInput(
                attrs={'class':'form-control'}),       
            'email':forms.EmailInput(
                attrs={'class':'form-control'}),          
            'l_name':forms.TextInput(
                attrs={ 'class':'form-control'}),         
            'age':forms.NumberInput(
                attrs={ 'class':'form-control'}) }
    
    def clean_patient_id(self):
        ei=self.cleaned_data['emp_id']
        if ei>100:
            raise validators.ValidationError('Employee Id should be below 100')
        return ei
      
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

