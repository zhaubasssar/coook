from django import forms
from main.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingridients', 'cooking', 'image']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['type'] = "text"
        self.fields['title'].widget.attrs['class'] = "form-control mb-3"
        self.fields['title'].widget.attrs['placeholder'] = "Post title"
        self.fields['title'].widget.attrs['name'] = "title"

        self.fields['image'].widget.attrs['class'] = "form-control mb-3 custom-file-input"
        self.fields['image'].widget.attrs['type'] = "file"
        self.fields['image'].widget.attrs['name'] = "image"
        self.fields['image'].widget.attrs['id'] = "formFile"




