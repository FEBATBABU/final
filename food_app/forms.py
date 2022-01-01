from .models import food
from django import forms
class ModeForms(forms.ModelForm):
    class Meta:
        model=food
        fields=['name','desc','img','price']