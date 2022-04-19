import pandas as pd
import requests
import streamlit as st


days = st.slider('Days', 1, 365, 90)

currency = st.radio(
     "currency",
     ('CAD', 'USD', 'INR'))

BASE_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency="

API_URL = BASE_URL + currency +"&days=" + str(days)+"&interval=daily"

#GET DATA 
req = requests.get(API_URL)

if req.status_code == 200:
    data = req.json()['prices']
    df = pd.DataFrame(data=data, columns=['Date', 'Price'])
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df = df.set_index('Date')
    st.line_chart(df)
    st.text('Average price during this time was '+ str(df['Price'].mean()) + ' '+ currency)