import json
from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)
from app import app


@app.route('/')
def home():
    return "Flask says 'Hello world!'"


@app.route('/lab04')
def lab04_bootstrap():
    return app.send_static_file('lab04_bootstrap.html')