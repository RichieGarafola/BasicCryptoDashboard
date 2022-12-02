import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen

# Title and subtitle
st.title("Cryptocurrency Daily Prices")


# Define crypto ticker variables
bitcoin = 'BTC-USD'
ethereum = 'ETH-USD'
ripple = 'XRP-USD'
bitcoinCash = 'BCH-USD'

# Access Data from yahoo finance
btc_data = yf.Ticker(bitcoin)
eth_data = yf.Ticker(ethereum)
xrp_data = yf.Ticker(ripple)
bch_data = yf.Ticker(bitcoinCash)

# Fetch history data from yahoo finance
btc_hist = btc_data.history(period = 'max')
eth_hist = eth_data.history(period = 'max')
xrp_hist = xrp_data.history(period = 'max')
bch_hist = bch_data.history(period = 'max')

# Fetch Crypto data for the dataframe

btc = yf.download(bitcoin)
eth = yf.download(ethereum)
xrp = yf.download(ripple)
bch = yf.download(bitcoinCash)


############
# Bitcoin
############
st.write("Bitcoin ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))

# Display image
st.image(imageBTC)

# Display dataframe
st.table(btc.tail(1))

# Display a chart
st.bar_chart(btc_hist.Close)

############
# Ethereum
############
st.write("Ethereum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))

# Display image
st.image(imageETH)

# Display dataframe
st.table(eth.tail(1))

# Display a chart
st.bar_chart(eth_hist.Close)

############
# Ripple
############
st.write("Ripple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))

# Display image
st.image(imageXRP)

# Display dataframe
st.table(xrp.tail(1))

# Display a chart
st.bar_chart(xrp_hist.Close)

############
# BitcoinCash
############
st.write("Bitcoin Cash($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))

# Display image
st.image(imageBCH)

# Display dataframe
st.table(bch.tail(1))

# Display a chart
st.bar_chart(bch_hist.Close)
