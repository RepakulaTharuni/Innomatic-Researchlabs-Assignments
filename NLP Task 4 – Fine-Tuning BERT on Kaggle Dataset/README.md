# Task 4: Fine-Tuning BERT on Kaggle Dataset | Feb Internship NLP 2026

## 📌 Internship Details
- Program: Data Science Internship – February 2026  
- Task:NLP Task 4 – Fine-Tuning BERT on Kaggle Dataset  

## 🎯 Objective
The objective of this project is to build a text classification model by fine-tuning a pre-trained BERT model on a real-world dataset. The project focuses on understanding transformer-based models, applying tokenization, training, and evaluating performance using multiple metrics.



## 📂 Dataset
- Dataset Used:IMDB Movie Reviews Dataset (Kaggle)  
- The dataset contains movie reviews labeled as positive or negative for sentiment analysis.



## 🛠️ Technologies Used
- Python  
- Hugging Face Transformers  
- PyTorch  
- Scikit-learn  
- Pandas & NumPy  
- Jupyter Notebook / Google Colab  



## 🔄 Project Workflow
Raw Data → Preprocessing → Tokenization → Model Training → Evaluation → Comparison  



## ⚙️ Implementation Steps

### 1. Data Preprocessing
- Cleaned text data (lowercasing)
- Handled missing values
- Converted labels (positive → 1, negative → 0)

### 2. Data Splitting
- Train set (80%)  
- Validation set (10%)  
- Test set (10%)  

### 3. Tokenization
- Used pre-trained tokenizer  
- Converted text into tokens suitable for BERT  

### 4. Model Building
- Loaded pre-trained **DistilBERT model**  
- Used `AutoModelForSequenceClassification`

### 5. Fine-Tuning
- Optimizer: AdamW  
- Learning Rate: 2e-5  
- Trained model on dataset  

### 6. Model Evaluation
Evaluated using:
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  


## 🧪 Experiments Performed

### 🔹 Full Fine-Tuning
- All layers trained  
- Achieved highest performance  

### 🔹 Frozen Model
- BERT layers frozen  
- Only classifier trained  
- Lower performance  

### 🔹 Partial Fine-Tuning
- Only last layers trained  
- Balanced performance and efficiency  



## 📊 Results & Analysis
- Full fine-tuning produced the best results due to complete learning of contextual features  
- Frozen model had reduced performance as feature extraction was fixed  
- Partial fine-tuning improved performance while reducing training time  



## 🧠 Key Insights
- Transformer models significantly improve NLP tasks  
- Fine-tuning enhances contextual understanding  
- Trade-off exists between training time and accuracy  
- Pre-trained models reduce the need for large datasets  



## 🚀 Conclusion
This project demonstrates how transformer-based models like BERT can be effectively fine-tuned for sentiment analysis tasks. It highlights the importance of experimentation and evaluation in achieving optimal performance.

