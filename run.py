#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
import sys
app = Flask(__name__)

@app.route('/')
def show_all():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
    reload(sys)