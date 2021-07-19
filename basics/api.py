# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:59:43 2021

@author: shubham.sharma1
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first API call!'

    