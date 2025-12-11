from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def index(request):
    """Render the English version of the homepage"""
    return render(request, 'index.html')

def index_kannada(request):
    """Render the Kannada version of the homepage"""
    return render(request, 'index_kann.html')

def register(request):
    """Render the registration form"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # For now, we'll just redirect to a success page or back to index
            return render(request, 'register.html', {
                'form': form,
                'success_message': 'Registration submitted successfully!'
            })
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def register_kannada(request):
    """Render the Kannada registration form"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # For now, we'll just redirect to a success page or back to index
            return render(request, 'register_kannada.html', {
                'form': form,
                'success_message': 'Registration submitted successfully!'
            })
    else:
        form = RegistrationForm()
    
    return render(request, 'register_kannada.html', {'form': form})
