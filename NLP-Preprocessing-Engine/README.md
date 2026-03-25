# NLP Preprocessing Engine (Advanced)

##  Project Overview


The objective is to build a robust NLP preprocessing pipeline capable of handling noisy real-world text data and converting it into clean, structured tokens suitable for machine learning models.


##  Objectives

* Clean and normalize raw text data
* Handle noise such as URLs, emojis, numbers, and repeated characters
* Extract meaningful tokens
* Perform token-level statistical analysis
* Build a reusable NLP preprocessing pipeline



##  Features Implemented

* ✅ Removal of URLs and email patterns
* ✅ Removal of numbers
* ✅ Lowercase text normalization
* ✅ Handling repeated characters (e.g., "soooo" → "so")
* ✅ Removal of special characters and emojis
* ✅ Removal of extra spaces
* ✅ Filtering short tokens (≤2 length, except "no", "not")
* ✅ Token analytics (count, unique words, average length)
* ✅ Frequency analysis using Counter
* ✅ Full pipeline function for batch processing
* ✅ Edge case handling (empty text, only emojis, only numbers)


##  Technologies Used

* Python
* Regular Expressions (re)
* NumPy
* Collections (Counter)



## How to Run

1. Open the notebook in Jupyter Notebook or Google Colab
2. Run all cells sequentially
3. View outputs for preprocessing, analytics, and results



