import logging
import socket
from flask_cors import CORS, cross_origin
from backend import app
from flask import Blueprint
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
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
def problems():
    
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

if __name__ == "__main__":
    logging.info("Starting application ...")
    app.run(debug = True)