# sentiment_app/views.py
import pickle
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import SentimentRecord
from .forms import SentimentForm

# Load model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), '../model/model.pkl')
tfidf_path = os.path.join(os.path.dirname(__file__), '../model/tfidf.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(tfidf_path, 'rb') as f:
    vectorizer = pickle.load(f)

@api_view(['POST'])
def predict_sentiment(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "No text provided"}, status=400)

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]

    label = "Positive" if prediction == 1 else "Negative"
    return Response({"text": text, "sentiment": label})


@csrf_exempt
def form_view(request):
    sentiment = None
    if request.method == 'POST':
        text = request.POST.get('text')
        vector = vectorizer.transform([text])
        prediction = model.predict(vector)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"
     
    return render(request, "form.html", {"sentiment": sentiment})


# Create
def create_sentiment(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_sentiments')
    else:
        form = SentimentForm()
    return render(request, 'create.html', {'form': form})

# Read
def read_sentiments(request):
    sentiments = SentimentRecord.objects.all().order_by('-created_at')
    return render(request, 'read.html', {'sentiments': sentiments})

# Update
def update_sentiment(request, pk):
    sentiment = get_object_or_404(SentimentRecord, pk=pk)
    if request.method == 'POST':
        form = SentimentForm(request.POST, instance=sentiment)
        if form.is_valid():
            form.save()
            return redirect('read_sentiments')
    else:
        form = SentimentForm(instance=sentiment)
    return render(request, 'update.html', {'form': form})

# Delete
def delete_sentiment(request, pk):
    sentiment = get_object_or_404(SentimentRecord, pk=pk)
    sentiment.delete()
    return redirect('read_sentiments')


@api_view(['POST'])
def predict_and_save(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "No text provided"}, status=400)

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"

    # Save to DB
    record = SentimentRecord.objects.create(text=text, predicted_sentiment=sentiment)

    return Response({
        "id": record.id,
        "text": record.text,
        "predicted_sentiment": record.predicted_sentiment,
        "created_at": record.created_at,
    })

@api_view(['GET'])
def all_sentiments(request):
    records = SentimentRecord.objects.all().values('id', 'text', 'predicted_sentiment', 'created_at')
    return Response(list(records), content_type='application/json')
