from django import forms
from .models import SentimentRecord

class SentimentForm(forms.ModelForm):
    class Meta:
        model = SentimentRecord
        fields = ['text', 'predicted_sentiment']
