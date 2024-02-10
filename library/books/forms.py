from django import forms
from .models import Book

"""class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ("title","book","image","genre","blurb",)"""

"""class BookForm(forms.ModelForm):
    # Add a CharField for the genre
    genre_input = forms.CharField(max_length=50, required=True, label="Genre")

    class Meta:
        model = Book
        fields = ("title", "author","book", "image", "blurb",)



    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.title = instance.title.upper()
        instance.genre_input= instance.genre_input.upper() # Capitalize the title
        if commit:
            instance.save()
        return instance"""

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "book", "image", "blurb", "genre")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.title = instance.title.upper()
       # instance.genre = instance.genre.upper()  # Capitalize the genre
        if commit:
            instance.save()
        return instance



class AddBookForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
    author = forms.CharField(max_length=255, required=False)
    library_books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
