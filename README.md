# 16 Personalities Test Web Application 🎯

A web application that implements a personality test based on the 16 Personalities model using machine learning (KNN classifier) and Streamlit.

## ✨ Features

- Interactive personality questionnaire
- Real-time personality prediction
- Detailed personality descriptions
- User-friendly interface
- Thai language support

## 🛠️ Technology Stack

- Streamlit - Web framework
- Scikit-learn - Machine learning (KNN classifier)
- Pandas - Data handling
- Joblib - Model serialization

## 📊 Model Performance

The KNN classifier achieves:
- Accuracy: 98.29%
- Precision: 98.31%
- Recall: 98.29%
- F1 Score: 98.26%

## 🚀 Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/oppolise/16-Personalities-Classification-Web-App
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

## 📱 Usage

1. Open the web application in your browser
2. Answer all personality questions
3. Submit your answers
4. View your personality type and description

## 📊 Dataset

The dataset consists of:
- 6000 rows
- 62 columns (60 features + personality type)
- Questions rated on a scale from -3 to 3

## 🤖 Model Details

Algorithm: K-Nearest Neighbors (KNN) Classifier
Best Parameters:
- n_neighbors: 10
- weights: distance
- p: 2