#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="public", template_folder="views")

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify(greeting="hello API")

@app.route("/api/timestamp/")
@app.route("/api/timestamp/<date_string>")
def timestamp(date_string=None):
    if date_string is None:
        date = datetime.now()
    else:
        try:
            date = datetime.fromisoformat(date_string)
        except:
            try:
                date = datetime.fromtimestamp(float(date_string) / 1000)
            except:
                return jsonify(error="Invalid Date")
    
    return jsonify(unix=int(date.timestamp() * 1000),
                   utc=date.astimezone(timezone.utc))
        
if __name__ == "__main__":
    app.run()
