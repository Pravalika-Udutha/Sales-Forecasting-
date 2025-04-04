import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Data Loading
data = pd.read_csv(r'C:\Users\uduth\OneDrive\Desktop\Career\Projects and Case studies\Sales Forecasting for a Store\store_sales_data.csv')
    # Assume promo=1 then 10% discount

# Features and target
X = data[['Customers_Visited', 'Advertising_Budget','Discount_Percentage']]
y = data['Sales']

# Train-Test-Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

model = LinearRegression()
model.fit(X_train,y_train)

# Model Prediction function
def predict_sales(customers,promo,discount):
    calculated_discount_feature = promo * 10
    input_data = np.array([[customers,promo,calculated_discount_feature]])
    prediction = model.predict(input_data)
    return prediction[0]


# UI SetUp
st.title("Store Sales Forecasting App")
budget = st.sidebar.number_input("Advertising Budget",value=0)
customers = st.sidebar.number_input("Number of Customers Visited", min_value=0, max_value=10000, value=500)
discount = st.sidebar.number_input("Discount Percentage (%)", min_value=0.0, max_value=50.0, value=10.0)




if st.sidebar.button("Predict Sales"):
    sales = predict_sales(customers,budget,discount)
    st.subheader("Prediction Result")
    st.write(f"Predicted Monthly Sales: {(sales-10):.2f} Lakhs")


