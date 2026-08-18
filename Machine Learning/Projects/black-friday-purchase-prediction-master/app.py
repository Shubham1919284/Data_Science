from pathlib import Path

import streamlit as st
import joblib
import numpy as np


MODEL_PATH = Path('purchase_prediction_model_xgb.pkl')
SCALER_PATH = Path('scaler.pkl')

if not MODEL_PATH.exists() or not SCALER_PATH.exists():
    st.error(
        "Required model files are missing (purchase_prediction_model_xgb.pkl and/or scaler.pkl). "
        "This app cannot make predictions without the real trained model, so it will not run."
    )
    st.stop()

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

st.title("🛍️ Black Friday Purchase Predictor")
st.write("Customer details bharo — predicted purchase amount milega!")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.selectbox("Age Group", ["0-17", "18-25", "26-35", "36-45", "46-50", "51-55", "55+"])
occupation = st.slider("Occupation Code", 0, 20, 4)
city = st.selectbox("City Category", ["A", "B", "C"])
stay = st.slider("Stay In Current City (Years)", 0, 4, 1)
marital = st.selectbox("Marital Status", ["Single", "Married"])
cat1 = st.slider("Product Category 1", 1, 20, 5)
cat2 = st.selectbox("Product Category 2", [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
cat3 = st.selectbox("Product Category 3", [0, 3, 5, 8, 9, 12, 14, 16])


gender_enc = 1 if gender == "Male" else 0
marital_enc = 1 if marital == "Married" else 0

# NOTE: must match the training-time encoding exactly (1-indexed, not 0-indexed)
age_map = {"0-17": 1, "18-25": 2, "26-35": 3, "36-45": 4, "46-50": 5, "51-55": 6, "55+": 7}
age_enc = age_map[age]

city_B = 1 if city == "B" else 0
city_C = 1 if city == "C" else 0

if st.button("Predict Purchase Amount 🚀"):
    # Column order must match training: Gender, Age, Occupation, Stay, Marital, Cat1, Cat2, Cat3, B, C
    input_data = np.array([[gender_enc, age_enc, occupation,
                             stay, marital_enc,
                             cat1, cat2, cat3,
                             city_B, city_C]])

    # Model was trained on StandardScaler-transformed features — raw input must be scaled the same way
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    prediction = max(500, prediction)  # floor at a realistic minimum purchase amount

    st.success(f"Predicted Purchase Amount: ₹{round(prediction, 2)}")