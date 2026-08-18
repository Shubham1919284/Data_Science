import streamlit as st
import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).with_name("flight_price_model.pkl")
model = joblib.load(MODEL_PATH)

FEATURE_ORDER = [
    "Airline",
    "Source",
    "Destination",
    "Total_Stops",
    "Additional_Info",
    "Date",
    "Month",
    "Arrival_Hour",
    "Arrival_Minute",
    "Dep_Hour",
    "Dep_Minute",
    "Total_Duration",
    "Duration_Hour",
    "Duration_Min",
    "Dep_Time_Bucket",
]

st.title('✈️ Flight Price Prediction App')
st.write("Flight details bharo — predicted price milega!")

airline = st.selectbox("Airline", [
    "Air Asia",
    "Air India",
    "GoAir",
    "IndiGo",
    "Jet Airways",
    "Jet Airways Business",
    "Multiple carriers",
    "Multiple carriers Premium economy",
    "SpiceJet",
    "Trujet",
    "Vistara",
    "Vistara Premium economy",
])
source = st.selectbox("Source City", ["Banglore", "Chennai", "Delhi", "Kolkata", "Mumbai"])
destination = st.selectbox("Destination City", ["Banglore", "Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"])
departure_date = st.date_input("Departure Date")
departure_time = st.time_input("Departure Time")
arrival_time = st.time_input("Arrival Time")
stops_text = st.selectbox("Total Stops", ["non-stop", "1 stop", "2 stops", "3 stops", "4 stops"])
additional_info = st.selectbox("Additional Info", [
    "1 Long layover",
    "1 Short layover",
    "2 Long layover",
    "Business class",
    "Change airports",
    "In-flight meal not included",
    "No Info",
    "No check-in baggage included",
    "No info",
    "Red-eye flight",
])

airline_map = {
    "Air Asia": 0,
    "Air India": 1,
    "GoAir": 2,
    "IndiGo": 3,
    "Jet Airways": 4,
    "Jet Airways Business": 5,
    "Multiple carriers": 6,
    "Multiple carriers Premium economy": 7,
    "SpiceJet": 8,
    "Trujet": 9,
    "Vistara": 10,
    "Vistara Premium economy": 11,
}
source_map = {"Banglore": 0, "Chennai": 1, "Delhi": 2, "Kolkata": 3, "Mumbai": 4}
destination_map = {"Banglore": 0, "Cochin": 1, "Delhi": 2, "Hyderabad": 3, "Kolkata": 4, "New Delhi": 5}
additional_info_map = {
    "1 Long layover": 0,
    "1 Short layover": 1,
    "2 Long layover": 2,
    "Business class": 3,
    "Change airports": 4,
    "In-flight meal not included": 5,
    "No Info": 6,
    "No check-in baggage included": 7,
    "No info": 8,
    "Red-eye flight": 9,
}
stops_map = {"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}


def get_time_of_day(hour: int) -> int:
    if 5 <= hour < 12:
        return 0  # Morning
    if 12 <= hour < 17:
        return 1  # Afternoon
    if 17 <= hour < 21:
        return 2  # Evening
    return 3  # Night

airline_enc = airline_map[airline]
source_enc = source_map[source]
destination_enc = destination_map[destination]
additional_info_enc = additional_info_map[additional_info]
stops_enc = stops_map[stops_text]

dep_hour = departure_time.hour
dep_minute = departure_time.minute
arr_hour = arrival_time.hour
arr_minute = arrival_time.minute

dep_total_minutes = dep_hour * 60 + dep_minute
arr_total_minutes = arr_hour * 60 + arr_minute
if arr_total_minutes < dep_total_minutes:
    arr_total_minutes += 24 * 60

total_duration = arr_total_minutes - dep_total_minutes
duration_hour = total_duration // 60
duration_min = total_duration % 60
dep_time_bucket = get_time_of_day(dep_hour)

if st.button("Predict Price 🚀"):
    feature_values = {
        "Airline": airline_enc,
        "Source": source_enc,
        "Destination": destination_enc,
        "Total_Stops": stops_enc,
        "Additional_Info": additional_info_enc,
        "Date": departure_date.day,
        "Month": departure_date.month,
        "Arrival_Hour": arr_hour,
        "Arrival_Minute": arr_minute,
        "Dep_Hour": dep_hour,
        "Dep_Minute": dep_minute,
        "Total_Duration": total_duration,
        "Duration_Hour": duration_hour,
        "Duration_Min": duration_min,
        "Dep_Time_Bucket": dep_time_bucket,
    }
    input_data = np.array([[feature_values[name] for name in FEATURE_ORDER]], dtype=np.float32)

    prediction = model.predict(input_data)[0]

    # sirf clip karo — warning mat dikhao
    prediction = max(1000, prediction)  # minimum ₹1000 rakho

    st.success(f"Predicted Flight Price: ₹{round(prediction, 2)}")

st.write("Made with ❤️ by Shubham")