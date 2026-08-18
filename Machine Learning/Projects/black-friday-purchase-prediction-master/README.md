# Black Friday Purchase Predictor — XGBoost + Streamlit

> An end-to-end Machine Learning project that predicts customer purchase amounts during Black Friday sales, combining in-depth EDA, XGBoost regression modeling, and a real-time Streamlit web application.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://github.com/Shubham1919284/black-friday-purchase-prediction)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://github.com/Shubham1919284/black-friday-purchase-prediction)
[![XGBoost](https://img.shields.io/badge/XGBoost-Regression-189AB4?style=flat)](https://github.com/Shubham1919284/black-friday-purchase-prediction)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Pipeline-F7931E?style=flat&logo=scikitlearn&logoColor=white)](https://github.com/Shubham1919284/black-friday-purchase-prediction)
[![Status](https://img.shields.io/badge/Status-Completed-28a745?style=flat)](https://github.com/Shubham1919284/black-friday-purchase-prediction)

---

## App Preview

> Enter customer demographics and product details — get an instant predicted purchase amount.

![App Screenshot](https://github.com/Shubham1919284/black-friday-purchase-prediction/blob/main/app_preview.png)

---

## Project Objective

Black Friday sales generate massive transaction volumes. This project uses historical purchase data to build a regression model that predicts how much a customer is likely to spend — based on who they are and what they are buying.

The end-to-end pipeline covers:
- Exploratory Data Analysis and Feature Engineering
- Training and comparing multiple regression models
- Deploying the best model as an interactive Streamlit web app

---

## Model Performance

All models were evaluated on the same held-out test split (33% of training data, `random_state=42`).

| Model | MAE | RMSE | R² Score |
|-------|-----|------|----------|
| Linear Regression | 3577.24 | 4683.93 | 0.1295 |
| Decision Tree | 2362.27 | 3337.43 | 0.5580 |
| Random Forest | 2226.12 | 3056.58 | 0.6293 |
| Gradient Boosting | 2269.16 | 2993.26 | 0.6445 |
| **XGBoost (Deployed)** | **2137.54** | **2878.57** | **0.6712** |

> Linear Regression underfits significantly (R² = 0.13), confirming purchase amount is not linearly related to these features. Tree-based ensembles perform far better, with XGBoost giving the best error/variance trade-off and was selected for deployment.

### Feature Importance (from the deployed XGBoost model)

| Feature | Importance |
|---|---|
| Product_Category_1 | 79.6% |
| Product_Category_2 | 7.4% |
| Product_Category_3 | 4.5% |
| City Category = C | 1.5% |
| Occupation | 1.4% |
| Age | 1.3% |
| Stay in Current City (Years) | 1.2% |
| City Category = B | 1.0% |
| Marital Status | 1.0% |
| Gender | 1.0% |

> `Product_Category_1` alone accounts for ~80% of the model's decision-making — customer demographics contribute comparatively little to predicting purchase amount.

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.8+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn (Linear Regression, Decision Tree, Random Forest, Gradient Boosting), XGBoost |
| Deployment | Streamlit |
| Model Persistence | Joblib |

---

## Project Structure

```text
black-friday-purchase-prediction/
│
├── app.py                                          # Streamlit web application
├── BlackFriday EDA And Feature Engineering.ipynb   # EDA, feature engineering & model training
├── purchase_prediction_model_xgb.pkl               # Serialized XGBoost model
├── scaler.pkl                                      # Serialized StandardScaler (required for correct predictions)
├── train.csv                                       # Training dataset (features + target)
├── test.csv                                        # Test dataset (features only)
└── README.md                                       # Project documentation
```

---

## Dataset

The dataset contains retail sales transactions with the following features:

**Customer Demographics**
- `Gender`, `Age`, `Marital_Status`, `Occupation`
- `City_Category`, `Stay_In_Current_City_Years`

**Product Details**
- `Product_Category_1`, `Product_Category_2`, `Product_Category_3`

**Target Variable**
- `Purchase` — amount spent (in INR)

> Source: [Black Friday Dataset — Kaggle](https://www.kaggle.com/datasets/mehdidag/black-friday)
> Total Records (train + test): 783,667

---

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/Shubham1919284/black-friday-purchase-prediction.git
cd black-friday-purchase-prediction
```

**2. Install dependencies**

```bash
pip install streamlit numpy pandas xgboost scikit-learn joblib matplotlib seaborn
```

**3. Run the Streamlit app**

```bash
streamlit run app.py
```

**4. Open in browser**

```
http://localhost:8501
```

---

## How It Works

1. User inputs customer details (gender, age, city, occupation) and product categories via the Streamlit UI
2. Inputs are encoded to match the training-time categorical mappings, then transformed using the saved `StandardScaler` (`scaler.pkl`) so they're on the same scale the model was trained on
3. The pre-trained XGBoost model (`purchase_prediction_model_xgb.pkl`) generates a real-time prediction
4. Predicted purchase amount is displayed instantly on screen

---

## Known Limitations & Future Enhancements

- `Product_Avg_Purchase` and `Product_Purchase_Count` were engineered during EDA but are not currently used by the deployed model — including them could improve accuracy further.
- Add SHAP-based feature importance visualization for deeper model explainability
- Extend to classification (high / medium / low spender segmentation)
- Deploy on Streamlit Cloud for public access
- Add a data upload feature so users can run batch predictions via CSV

---

## Author

**Shubham Kumar Jha**
B.Tech CSE (Data Science) — Gulzar Group of Institutes, PTU

[![Email](https://img.shields.io/badge/Email-sk1919284@gmail.com-D44638?style=flat&logo=gmail&logoColor=white)](mailto:sk1919284@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-shubham--kumar--jha-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/shubham-kumar-jha-1a2b3c)
[![GitHub](https://img.shields.io/badge/GitHub-Shubham1919284-181717?style=flat&logo=github&logoColor=white)](https://github.com/Shubham1919284)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-4CAF50?style=flat&logo=googlechrome&logoColor=white)](https://shubham1919284.github.io/Portfolio/)

---

*Open-source and free to use for educational and portfolio purposes. Attribution appreciated.*