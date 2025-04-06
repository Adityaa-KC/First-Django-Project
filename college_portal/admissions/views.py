from django.shortcuts import render
from .forms import StudentApplicationForm

def home(request):
    return render(request, 'admissions/home.html')

def apply(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'admissions/success.html')
        else:
            print(form.errors)  
    else:
        form = StudentApplicationForm()
        
    return render(request, 'admissions/apply.html', {'form': form})
