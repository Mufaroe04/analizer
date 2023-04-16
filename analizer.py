import streamlit as st
# import  pandas as pd
import yfinance as yf
from PIL import Image
import time
def bit_coin():
    bit_image=Image.open('bitcoin .jpeg')
    st.image(bit_image,caption="bitcoin")
    bitcoin='BTC-USD'
    bitcoin_data=yf.Ticker(bitcoin)
    if bitcoin_data:
        start_date = st.date_input('Enter starting date for historical data')
        end_date = st.date_input('Enter ending date for historical data')
        if start_date and end_date:
            btc=yf.download(bitcoin,start=start_date ,end=end_date)
            st.table(btc)

    st.table(btc)
    bit_history=bitcoin_data.history(period="max")
    st.bar_chart(bit_history.Close)
   
def ethereum():
    eth_image=Image.open('ethereum .jpeg')
    st.image(eth_image,caption="ethereum")
    ethereum='ETH-USD'
    ethereum_data=yf.Ticker(ethereum)
    if ethereum_data:
        start_date = st.date_input('Enter starting date for historical data')
        end_date = st.date_input('Enter ending date for historical data')
        eth=yf.download(ethereum,start=start_date ,end=end_date)
        st.table(eth)
    ethereum_history=ethereum_data.history(period="max")
    st.bar_chart(ethereum_history)
   
def ripple():
    ripple_image=Image.open('ripple.jpeg')
    st.image(ripple_image,caption="ripple")
    ripple='XRP-USD'
    ripple_data=yf.Ticker(ripple)
    if ripple_data:
        start_date = st.date_input('Enter starting date for historical data')
        end_date = st.date_input('Enter ending date for historical data')
        rdata=yf.download(ripple,start=start_date ,end=end_date)
        st.table(rdata)
    ripple_history=ripple_data.history(period="max")
    st.bar_chart(ripple_history)
  
def bitcoin_cash():
    bit_cash_image=Image.open('bitcash.jpeg')
    st.image(bit_cash_image,caption="bitcoin cash ")
    bitcoin_cash='BCH-USD'
    #getting data from yahoo finance
    bitcion_cash_data=yf.Ticker(bitcoin_cash)
    if bitcion_cash_data:
        start_date = st.date_input('Enter starting date for historical data')
        end_date = st.date_input('Enter ending date for historical data')
        bit_data=yf.download(bitcoin_cash,start=start_date ,end=end_date)
        st.table(bit_data)
    #historical data from yahoo for crypto
    bit_cash_history=bitcion_cash_data.history(period="max")
    #fetch crypto data from yahoo and store in dataframe
    st.bar_chart(bit_cash_history)


def main():
    st.title("Cryptocurrency Data Visualization")
    coin_choices=st.sidebar.selectbox('Select your crypto type',
    ['BTC-USD','ETH-USD','XRP-USD','BCH-USD'])
    if coin_choices== 'BTC-USD':
        bit_coin()
    if coin_choices== 'ETH-USD':
        ethereum()
    if coin_choices== 'XRP-USD':
        ripple()
    if coin_choices== 'BCH-USD':
        bitcoin_cash()
if __name__=="__main__":
    main()