# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:52:02 2021

@author: Mad_ToBy
"""
from datetime import timedelta
from flask import Flask
app = Flask(__name__)
from flask import render_template
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
@app.route('/')
def thehtml():
    return render_template('test.html')
    
if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = 8080,debug = True)
    