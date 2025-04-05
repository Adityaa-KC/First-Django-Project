from django.shortcuts import render, redirect
from .forms import AdmissionForm

def admission_view(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            # Process form data here
            # You can save it to the database or print it
            print(form.cleaned_data)
            return redirect('thank_you')  # redirect to success page
    else:
        form = AdmissionForm()
    
    return render(request, 'admission_form.html', {'form': form})
