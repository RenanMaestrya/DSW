from django import forms
from .models import Disk

class DisksForm(forms.ModelForm):
    class Meta:
        model = Disk
        fields = '__all__'