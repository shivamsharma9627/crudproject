from django import forms
from .models import Student





class StudentForm(forms.ModelForm):
    roll=forms.CharField(max_length=100,label_suffix='', required=True,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your roll', 'onchange': 'change_text()'}))
    name=forms.CharField(max_length=100,label_suffix='', required=True,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your name', 'onchange': 'change_text()'}))
    email=forms.CharField(max_length=100,label_suffix='', required=True,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your email', 'onchange': 'change_text()'}))
    password=forms.CharField(max_length=100,label_suffix='', required=True,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your password', 'onchange': 'change_text()'}))
    phone=forms.CharField(max_length=100,label_suffix='', required=True,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your phone', 'onchange': 'change_text()'}))
    address=forms.CharField(max_length=100,label_suffix='', required=True,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your address', 'onchange': 'change_text()'}))    
    


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['roll'].label = "roll"

    class Meta:
        model = Student
        fields = ('roll', 'name', 'email', 'password', 'phone','address')