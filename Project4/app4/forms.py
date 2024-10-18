from django import forms
from.models import Student
from django.core import validators

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

        labels={
            'stu_id':' Enter student ID',
            'f_name':'ENTER FIRST NAME',
            'email':'ENTER EMAIL ID',
            'l_name': 'ENTER LAST name',
            'roll_no':'ENTER Roll number' }

        widgets={
             
            'patient_id':forms.NumberInput(
                attrs={
                       'class':'form-control'}),
            'f_name':forms.TextInput(
                attrs={
                       'class':'form-control'}),
            'email':forms.EmailInput(
                attrs={
                       'class':'form-control'}),
            'l_name':forms.TextInput(
                attrs={
                       'class':'form-control'}),
            'age':forms.NumberInput(
                attrs={
                       'class':'form-control'}),          
        }

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



