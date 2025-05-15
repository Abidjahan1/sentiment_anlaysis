# sentiment_anlaysis

# 🧠 Sentiment Analysis Web App (Django + ML + PostgreSQL)

This is a web-based **Sentiment Analysis** application built with **Django** that uses a **Logistic Regression** machine learning model to classify input text as **Positive** or **Negative**. The model is trained on a public dataset and integrated into a web form and API using Django REST Framework.

---

## 🚀 Features

- Logistic Regression-based text sentiment classification
- REST API for predictions (`/predict/`)
- Web form for text submission (`/form/`)
- Saves user input and predictions to **PostgreSQL**
- Lists all records as JSON via API (`/all/`)

---

## 🧠 Machine Learning Model

- **Algorithm**: Logistic Regression
- **Vectorization**: TF-IDF
- **Dataset**: [Sentiment140 (Kaggle)](https://www.kaggle.com/datasets/kazanova/sentiment140)

---

## 📁 Project Structure

sentiment/
├── sentiment/ # Main Django project settings
├── model
│ ├── model.pkl
│ ├── tfidf.pkl
├── sentiment_app/ # Core Django app
│ ├── views.py # Predict API, Form handler, List view
│ ├── models.py # SentimentRecord model
│ ├── urls.py # App-level routes
│ └── templates/
│ └── form.html # HTML form to submit text
│ └── create.html # add new record
│ └── update.html # update the record
│ └── read.html # read all records
├── manage.py
├── requirements.txt
└── README.md


🌐 API Endpoints

| Method | URL Pattern         | Name                | Description                                                               |
| ------ | ------------------- | ------------------- | ------------------------------------------------------------------------- |
| POST   | `/api/sentiment/`   | `predict_sentiment` | Predict sentiment from raw text using Logistic Regression model (no save) |
| GET    | `/form/`            | -                   | Web form (HTML) to input text and get sentiment prediction                |
| POST   | `/create/`          | `create_sentiment`  | Create a new sentiment record manually                                    |
| GET    | `/read/`            | `read_sentiments`   | View all sentiment records in the database                                |
| PUT    | `/update/<int:pk>/` | `update_sentiment`  | Update a specific sentiment record by ID                                  |
| DELETE | `/delete/<int:pk>/` | `delete_sentiment`  | Delete a specific sentiment record by ID                                  |
| POST   | `/predict-save/`    | `predict_and_save`  | Predict sentiment from text and save the result into the database         |
| GET    | `/all/`             | `all_sentiments`    | Return all sentiment records as a JSON response                           |

