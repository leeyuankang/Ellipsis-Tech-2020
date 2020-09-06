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

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return "Home Page"

@app.route('/stock_counter', methods = ['GET', 'POST'])
def stock_counter():
    
    form_info = request.form

    stock_list = ["BIDU", "TSLA", "UBER"]

    # Testing with a random ticker
    tickers = {}
    test_ticker_info = yf.Ticker("UBER").info
    for stock in stock_list:
        test_ticker_info = yf.Ticker(stock).info
        tickers[stock] = test_ticker_info

    # Retrive from form
    # stock_ticker = yf.Ticker(form_info["ticker"])
    
    # ticker_info = test_ticker.info

    return tickers

@app.route('/history', methods = ['GET', 'POST'])
def history():

    # Valid Periods  --> 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    period = "1y"
    msft = yf.Ticker("MSFT")    
    # form_info = request.form
        
    # get historical market data
    hist = msft.history(period = period)

    # get historical market data
    hist = hist.reset_index()
    hist['Date'] = pd.to_datetime(hist['Date']).astype(str)
    hist.set_index(['Date'], inplace=True)
    json_historical_price = hist.to_dict('index')

    return json_historical_price

@app.route('/recommendations', methods = ['GET', 'POST'])
def recommendations():

    msft = yf.Ticker("MSFT")    
    # form_info = request.form
        
    # get historical market data
    recommendations_df = msft.recommendations

    recommendations_df.reset_index(inplace=True)
    recommendations_df['Year'] = recommendations_df['Date'].dt.year
    recommendations_df['date'] = recommendations_df['Date'].dt.date
    recommendations_df = recommendations_df.rename(columns={'Date': 'Datetime'}).astype(str)
    recommendations_df.groupby("Datetime")
    recommendations_df.set_index(['Datetime'], inplace=True)

    json_recommendations = recommendations_df.to_dict('index')

    return json_recommendations

if __name__ == "__main__":
    logging.info("Starting application ...")
    app.run(debug = True)