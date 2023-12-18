from .models import Review
from django import forms

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_email', 'review_content']