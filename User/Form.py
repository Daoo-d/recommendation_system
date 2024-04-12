from django import forms
from .models import CustomUser,Employee

class SignUp(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','autocomplete':'off'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password','autocomplete':'off'}))
    username = forms.CharField(label = 'Username',widget=forms.TextInput(attrs={'placeholder': 'Username','autocomplete':'off'}))
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")
    class Meta:
        model = CustomUser
        exclude = ('is_employee','is_employer','groups','user_permissions','slug','date_joined')
        labels = {
            'fullname':'Full Name',
            'dob':'Date of Birth'
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email','autocomplete':'off'}),
            'fullname': forms.TextInput(attrs={'placeholder': 'Full Name','autocomplete':'off'}),
            'city':forms.TextInput(attrs={'placeholder': 'City','autocomplete':'off'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','autocomplete':'off'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username','autocomplete':'off'}),
            'dob': forms.DateInput(format=('%d-%m-%Y'), 
                                   attrs={'class': 'form-control', 
                                          'placeholder': 'Select a date',
                                          'type': 'date'}),
        }     

# # class CommaSeparatedField(forms.CharField):
# #     def to_python(self, value):
# #         # Convert the comma-separated string to a list of skills
# #         my_array=[]
# #         if value:
# #             my_array = value.split(',')
# #             return my_array
# #         return my_array
            
class portfolio_data(forms.ModelForm):
    user_s = forms.CharField(label='Skills', widget=forms.TextInput(attrs={'id': 'skillsInput','placeholder': 'Enter skills (comma-separated)','autocomplete':'off'}))
    class Meta:
        model = Employee
        exclude =('user','skills')
        widgets = {
        'profile_title': forms.TextInput(attrs={'placeholder': 'Enter profile title'}),
        'profile_description': forms.Textarea(attrs={'placeholder': 'Enter profile description'}),
        'education': forms.Textarea(attrs={'placeholder': 'Enter education details'}),
        'hourly_rate': forms.NumberInput(attrs={'placeholder': 'Enter hourly rate'}),
        'profile_links': forms.URLInput(attrs={'placeholder': 'Enter profile link'}),
        'experience': forms.Textarea(attrs={'placeholder': 'Enter experience details'}),
        'availability': forms.Select(attrs={'placeholder': 'Enter experience details'}),
    }

