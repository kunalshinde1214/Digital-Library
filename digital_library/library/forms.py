from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'language', 'release_date', 'summary', 'file', 'file_type']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }