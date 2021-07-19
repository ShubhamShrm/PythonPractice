# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:18:54 2021

@author: shubham.sharma1
"""


from flask import Flask, request
app = Flask(__name__)



@app.route('/enc/<s>',methods=['GET'])
def Rotn(s):
    a = ''
    n = int(request.args.get('n'))
    for i in s:
        x = chr(ord(i) + n)
        a = a + x
    print(a)
    return(a)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')