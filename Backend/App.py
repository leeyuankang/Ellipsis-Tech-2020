import logging
import socket
from flask_cors import CORS, cross_origin
from backend import app
from flask import Blueprint, Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import pandas as pd
import pprint
import json
import requests
import base64
import urllib.request
import os
import yfinance as yf
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return "Home Page"

@app.route('/price', methods = ['GET', 'POST'])
def stock_counter():

    ticker_list = ["BIDU", "TSLA", "UBER"]

    json_historical_price = {}

    for ticker in ticker_list:
        period = "5d"
        ticker_info = yf.Ticker(ticker)    

        # get historical market data
        hist = ticker_info.history(period = period)

        # get historical market data
        hist = hist.reset_index() 

        hist['Date'] = pd.to_datetime(hist['Date']).astype(str)
        hist.set_index(['Date'], inplace=True)
        
        difference = hist['Close'][-1] - hist['Close'][-2]
        
        change = round(difference / hist['Close'][-2] * 100, 2)
        
        json_historical_price[ticker] = [hist['Close'][-1], change]

    return json_historical_price

@app.route('/history', methods = ['GET', 'POST'])
def history():

    period = "1y"
    bidu = yf.Ticker("BIDU")    

    # get historical market data
    hist = bidu.history(period = period)

    # get historical market data
    hist = hist.reset_index()

    hist['Timestamp'] = hist['Date'].apply(lambda x: unix_time_millis(x)) 

    hist['Date'] = pd.to_datetime(hist['Date']).astype(str)
    hist.set_index(['Date'], inplace=True)
    json_historical_price = hist[['Timestamp','Open', 'High', 'Low', 'Close', 'Volume']].to_dict('index')

    return json_historical_price

if __name__ == "__main__":
    logging.info("Starting application ...")
    app.run(port=8000, host='0.0.0.0')