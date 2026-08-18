import streamlit as st
import joblib 
import numpy as np

model=joblib.load('purchase_prediction_model_xgb.pkl')

st.title("🛍️ Black Friday Purchase Predictor")
st.write("Customer details bharo — predicted purchase amount milega!")

gender=st.selectbox("Gender", ["Male", "Female"])
age=st.selectbox("Age Group", ["0-17", "18-25", "26-35", "36-45", "46-50", "51-55", "55+"])
occupation    = st.slider("Occupation Code", 0, 20, 4)
city          = st.selectbox("City Category", ["A", "B", "C"])
stay          = st.slider("Stay In Current City (Years)", 0, 4, 1)
marital       = st.selectbox("Marital Status", ["Single", "Married"])
cat1          = st.slider("Product Category 1", 1, 20, 5)
cat2 = st.selectbox("Product Category 2", [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
cat3 = st.selectbox("Product Category 3", [0, 3, 5, 8, 9, 12, 14, 16])


gender_enc = 1 if gender == "Male" else 0
marital_enc = 1 if marital == "Married" else 0

age_map = {"0-17":0, "18-25":1, "26-35":2, "36-45":3, "46-50":4, "51-55":5, "55+":6}
age_enc = age_map[age]

city_B = 1 if city == "B" else 0
city_C = 1 if city == "C" else 0

if st.button("Predict Purchase Amount 🚀"):
    input_data = np.array([[gender_enc, age_enc, occupation,
                             stay, marital_enc,
                             cat1, cat2, cat3,
                             city_B, city_C]])

    prediction = model.predict(input_data)[0]

    # sirf clip karo — warning mat dikhao
    prediction = max(500, prediction)  # minimum ₹500 rakho

    st.success(f"Predicted Purchase Amount: ₹{round(prediction, 2)}")

