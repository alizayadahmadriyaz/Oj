from django import forms 
from submit.models import Codesubmission

Lang_choices=[
    ('c','C'),
    ('cpp','C++'),
    ('py','python'),
]
class CodeSubmissionForm(forms.ModelForm):
    language=forms.ChoiceField(choices=Lang_choices)
    class Meta:
        model=Codesubmission
        fields=['model','language','input_data']