from django import forms
from .models import Students,Book,issue_book

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['id','is_borrowed']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter book title'}),
            'author' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter book author'}),
            'ISBN' : forms.NumberInput(attrs={'class':'form-control'}),
            'genre' : forms.Select(attrs={'class':'form-control'}),
            'book_no' : forms.NumberInput(attrs={'class':'form-control'}),
        }

class issue_bookForm(forms.ModelForm):
    class Meta:
        model = issue_book
        exclude = ['issue_date', 'due_date', 'date_returned']

