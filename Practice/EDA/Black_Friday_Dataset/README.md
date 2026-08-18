# 🛍️ Black Friday Purchase Predictor

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-green.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange.svg)

A Machine Learning project that predicts the purchase amount of a customer during Black Friday sales based on demographics and product details. The project involves Exploratory Data Analysis (EDA), Feature Engineering, Model Training using XGBoost, and an interactive web application built with Streamlit.

---

## ✨ Features
- **User-Friendly Interface**: Developed a beautiful UI using Streamlit where users can enter their details to get predictions.
- **Accurate Predictions**: Uses a robust XGBoost Regression model to predict the monetary purchase amount.
- **Comprehensive EDA**: Includes an in-depth Jupyter Notebook covering data cleaning, visualization, and feature engineering.
- **Real-Time Inference**: Connects user inputs directly to the saved `.pkl` model for instant results.

---

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: Numpy, Pandas, Matplotlib, Seaborn
- **Framework**: Streamlit
- **Machine Learning**: XGBoost (Regression), Scikit-Learn

---

## 📂 Project Structure

```text
Black_Friday_Dataset/
│
├── app.py                                      # Main Streamlit web application
├── BlackFriday EDA And Feature Engineering.ipynb # Notebook with EDA & Model training
├── purchase_prediction_model_xgb.pkl           # Pre-trained XGBoost Model
├── train.csv                                   # Training dataset (features & target)
├── test.csv                                    # Testing dataset (only features)
└── README.md                                   # Project documentation (this file)
```

---

## 🚀 How to Run Locally

Follow these steps to set up and run the application on your local machine:

**1. Navigate to the project folder:**
```bash
cd Path/To/Black_Friday_Dataset
```

**2. Install the required dependencies:**
Make sure you have Python installed. Then, install the required packages:
```bash
pip install streamlit numpy xgboost joblib pandas scikit-learn
```

**3. Run the Streamlit app:**
```bash
streamlit run app.py
```

**4. Open your browser:**
Navigate to `http://localhost:8501` to interact with the application!

---

## 📊 About the Dataset
The dataset comprises sales transactions captured at a retail store. It includes:
- **Customer Demographics:** `Age`, `Gender`, `Marital Status`, `City_Category`, `Stay_In_Current_City_Years`, `Occupation`.
- **Product Details:** `Product_Category_1`, `Product_Category_2`, `Product_Category_3`.

The target variable is **`Purchase`** (amount spent). 

---

## 💡 Author
This project was developed as part of practical Data Science and Machine Learning learning. Enjoy exploring the data and predicting purchases!
