import streamlit as st
import requests

# Define the API URL
url = "https://ojwebapp-bteqf0h9a0a9cmgv.francecentral-01.azurewebsites.net/predict"



# this is the main function in which we define our webpage  
def main():
    st.markdown("# Wine Quality Prediction App 🍷🍇")
    st.markdown("### This app is meant to predict red wine quality " +
            "according to different chemical")

# Init code
if __name__=='__main__': 
    main()

# slider version 
volatile_acidity = st.slider('Volatile Acidity', 0.0, 2.0, 0.319, 0.001) 
alcohol = st.slider('Alcohol', 0.0, 16.0, 11.634, 0.01) 

st.text(volatile_acidity)
st.text(alcohol)

if st.button('Predict Quality'):
    data = {
        'volatile_acidity': volatile_acidity,
        'alcohol': alcohol
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Predicted Quality: {prediction}")
        else:
            st.error(f"API Error: {response.status_code}")
            st.error(f"Response: {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")