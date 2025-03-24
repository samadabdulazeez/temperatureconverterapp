import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def classify_temperature(temp, unit):
    """Classifies the temperature as Cold or Hot."""
    if unit == "C":
        return "Cold" if temp < 10 else "Hot"
    elif unit == "F":
        return "Cold" if temp < 50 else "Hot"

st.title("Temperature Converter")


temp = st.number_input("Enter the temperature value:")
unit = st.selectbox("Select unit:", ("Celsius (°C)", "Fahrenheit (°F)"))

if unit == "Celsius (°C)":
    converted = celsius_to_fahrenheit(temp)
    category = classify_temperature(converted, "F")
    st.write(f"{temp}°C is {converted:.2f}°F → {category}")
elif unit == "Fahrenheit (°F)":
    converted = fahrenheit_to_celsius(temp)
    category = classify_temperature(converted, "C")
    st.write(f"{temp}°F is {converted:.2f}°C → {category}")