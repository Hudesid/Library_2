from django import forms
from .models import Book, Comment


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_date', 'descriptions')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a title name'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter an author'
            }),
            'published_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',

            }),
            'descriptions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a description',

            }),
        }

class BookCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'add_date', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a comment'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name'
            }),
            'add_date': forms.DateInput(attrs={
                'class': 'form-control',
            })
        }