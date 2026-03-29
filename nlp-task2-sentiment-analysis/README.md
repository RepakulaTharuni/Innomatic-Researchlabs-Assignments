# Sentiment Analysis using NLP & Machine Learning

##  Project Overview
This project builds an end-to-end Sentiment Analysis system using Natural Language Processing (NLP) and Machine Learning models. The goal is to classify text into positive or negative sentiment.

---

## Dataset
- Source: IMDb Movie Reviews Dataset
- Total Samples: 40,000+
- Labels:
  - 0 → Negative
  - 1 → Positive

---

##  Project Pipeline
Raw Text → Preprocessing → Feature Engineering → Model Training → Evaluation → Comparison

---

##  NLP Preprocessing
- Lowercasing
- Removal of punctuation & special characters
- Stopword removal
- Tokenization
- Lemmatization
- URL removal

---

##  Feature Engineering
- Bag of Words (BoW)
- TF-IDF Vectorization

---

##  Models Used
1. Logistic Regression  (Best Model)
2. Naive Bayes
3. Decision Tree

---

##  Model Performance

| Model                | Accuracy | F1 Score |
|---------------------|----------|----------|
| Logistic Regression | 88.55%   | 0.885    |
| Naive Bayes         | 84.51%   | 0.845    |
| Decision Tree       | 71.93%   | 0.719    |

---

##  Key Insights
- Logistic Regression performed best with TF-IDF features.
- Naive Bayes works efficiently with Bag of Words.
- Decision Tree tends to overfit text data.
- Preprocessing significantly improves model performance.
- Dataset is balanced, making accuracy a reliable metric.

---

##  Sample Predictions
- "This movie was amazing!" → Positive ✅  
- "Worst film ever" → Negative ❌  
- "It was okay, not great" → Positive  

---

##  Technologies Used
- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn

---

##  How to Run
1. Open the notebook in Google Colab / Jupyter
2. Upload the dataset (`Train.csv`)
3. Run all cells
4. View model results and predictions


