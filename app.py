import streamlit as st
import numpy as np
import pickle
import tensorflow as tf

# Load the trained model and scaler
model = tf.keras.models.load_model("model_ann.h5")
scaler = pickle.load(open("scaler.pkl", "rb"))

# App title
st.title("🏠 House Price Prediction using ANN")
st.markdown("Enter the details of the house to predict its price.")

# Input fields
longitude = st.number_input("Longitude", value=-122.23, format="%.4f")
latitude = st.number_input("Latitude", value=37.88, format="%.4f")
housing_median_age = st.number_input("Housing Median Age", value=41.0, format="%.2f")
total_rooms = st.number_input("Total Rooms", value=880.0, format="%.2f")
total_bedrooms = st.number_input("Total Bedrooms", value=129.0, format="%.2f")
population = st.number_input("Population", value=322.0, format="%.2f")
households = st.number_input("Households", value=126.0, format="%.2f")
median_income = st.number_input("Median Income", value=8.3252, format="%.4f")

ocean_proximity_map = {
    "<1H OCEAN": 0,
    "INLAND": 1,
    "NEAR OCEAN": 2,
    "NEAR BAY": 3,
    "ISLAND": 4
}
ocean_proximity_str = st.selectbox("Ocean Proximity", list(ocean_proximity_map.keys()))
ocean_proximity = ocean_proximity_map[ocean_proximity_str]

# Predict button
if st.button("Predict Price"):
    features = np.array([longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
                         population, households, median_income, ocean_proximity])
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    st.success(f"Predicted House Price: ${prediction[0][0]:,.2f}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit & TensorFlow")
