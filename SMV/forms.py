from django import forms
from django.core.validators import RegexValidator

class RegistrationForm(forms.Form):
    # Name of Registrar
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter full name'
        }),
        label='Name of Registrar'
    )
    
    # Father Name/Husband Name
    guardian_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter father/husband name'
        }),
        label="Father's Name/Husband's Name"
    )
    
    # Date of Birth
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        label='Date of Birth',
        required=False
    )
    
    # Age
    age = forms.IntegerField(
        min_value=0,
        max_value=150,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter age'
        }),
        label='Age',
        required=False
    )
    
    # Profession
    profession = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter profession'
        }),
        label='Profession'
    )
    
    # Address
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter full address'
        }),
        label='Address'
    )
    
    # Mobile Number with validation
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    mobile_no = forms.CharField(
        validators=[phone_regex],
        max_length=17,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+91XXXXXXXXXX'
        }),
        label='Mobile No.'
    )
    
    # Email ID
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com'
        }),
        label='E-mail ID'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get('date_of_birth')
        age = cleaned_data.get('age')
        
        # Ensure at least one of DOB or Age is provided
        if not dob and not age:
            raise forms.ValidationError(
                "Please provide either Date of Birth or Age."
            )
        
        return cleaned_data
