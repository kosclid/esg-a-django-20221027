from django import forms
from diary.models import Memory

class DiaForm(forms.ModelForm):  # ModelForm -> 
    class Meta:
        model = Memory
        fields = '__all__'