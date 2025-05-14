# sentiment_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/sentiment/', views.predict_sentiment, name='predict_sentiment'),
     path('form/', views.form_view),
    path('api/sentiment/', views.predict_sentiment),
     path('create/', views.create_sentiment, name='create_sentiment'),
    path('read/', views.read_sentiments, name='read_sentiments'),
    path('update/<int:pk>/', views.update_sentiment, name='update_sentiment'),
    path('delete/<int:pk>/', views.delete_sentiment, name='delete_sentiment'),
     path('predict-save/', views.predict_and_save, name='predict_and_save'),
    path('all/', views.all_sentiments, name='all_sentiments'),
]
