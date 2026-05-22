import streamlit as st
import pandas as pd 
import numpy as np
import joblib

model = joblib.load("house_price_model.pkl")


st.title("California House Price Pridiction App")

st.write(
    "Enter house details to predict California house prices."
)

longitude = st.number_input("Longitude")

latitude = st.number_input("Latitude")

housing_median_age = st.number_input("Housing Median Age")

total_rooms = st.number_input("Total Rooms",
                              min_value=1.0
                              )

total_bedrooms = st.number_input("Total Bedrooms")

population = st.number_input("Population",
                             min_value=1.0
                             )

households = st.number_input("Households",
                             min_value=1.0
                             )

median_income = st.number_input("Median Income")

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)


rooms_per_household = (
    total_rooms / households
)

bedrooms_per_room = (
    total_bedrooms / total_rooms
)

population_per_household = (
    population / households
)


input_data = pd.DataFrame({

    'longitude': [longitude],

    'latitude': [latitude],

    'housing_median_age': [housing_median_age],

    'total_rooms': [total_rooms],

    'total_bedrooms': [total_bedrooms],

    'population': [population],

    'households': [households],

    'median_income': [median_income],

    'ocean_proximity': [ocean_proximity],

    'rooms_per_household': [rooms_per_household],

    'bedrooms_per_room': [bedrooms_per_room],

    'population_per_household': [population_per_household]
})

if st.button("Predict House Price"):

    prediction = model.predict(input_data)

    prediction = np.expm1(prediction)

    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )
