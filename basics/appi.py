# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:32:40 2021

@author: shubham.sharma1
"""

from flask import Flask

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0')
    