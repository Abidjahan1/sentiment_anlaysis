from django.db import models

# Create your models here.


class SentimentRecord(models.Model):
    text = models.TextField()
    predicted_sentiment = models.CharField(max_length=10)  # e.g., "positive", "negative"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}... - {self.predicted_sentiment}"
