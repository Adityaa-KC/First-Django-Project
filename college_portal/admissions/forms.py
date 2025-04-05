from django import forms

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
COURSE_CHOICES = [
    ('B.Sc Computer Science', 'B.Sc Computer Science'),
    ('B.Com', 'B.Com'),
    ('B.A', 'B.A'),
    ('B.Tech', 'B.Tech'),
    ('M.Sc', 'M.Sc'),
]

class AdmissionForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    phone = forms.CharField(max_length=10)
