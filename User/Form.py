from django import forms
from .models import CustomUser,Employee

class SignUp(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','autocomplete':'off'}))
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")
    class Meta:
        model = CustomUser
        exclude = ('is_employee','is_employer')
        labels = {
            'fullname':'Full Name',
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email','autocomplete':'off'}),
            'fullname': forms.TextInput(attrs={'placeholder': 'Full Name','autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password','autocomplete':'off'}),
            'city':forms.TextInput(attrs={'placeholder': 'City','autocomplete':'off'}),
            'dob': forms.DateInput(format=('%d-%m-%Y'), 
                                   attrs={'class': 'form-control', 
                                          'placeholder': 'Select a date',
                                          'type': 'date'}),
        }     
class portfolio_data(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'        