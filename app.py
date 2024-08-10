import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title='Customer Churn Prediction App',
    page_icon="📊",  
    layout='wide'
)

# Title of the app
st.title('ChurnPredictor')

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Data", "DashBoard", "Predict","History"])


# Home page

if page == "Home":
    st.write("Welcome to the Customer Churn Prediction App!")
    st.write("This app helps you predict customer churn using machine learning model.")
    st.write("Check out the project on GitHub: [ChurnPredictor](https://github.com/Ogoms/ChurnPredictor)")
