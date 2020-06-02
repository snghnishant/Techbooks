from django import forms
from catalog.models import BookRequestModel, Review

#Request Form
class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequestModel
        fields = '__all__'

#Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book_linked', 'name', 'email', 'text')
