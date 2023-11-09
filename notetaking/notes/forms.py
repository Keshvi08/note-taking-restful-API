from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=('title', 'text', 'created_at', 'modified_at')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control my-3'}),
            'text':forms.Textarea(attrs={'class':'form-control my-3'}),
        }
