from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name',
                  'journal',
                  'author',
                  'published_date',
                  'description',
                  'publisher']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'journal': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
        }
