#!/usr/bin/env python
# Martin Kersner, m.kersner@gmail.com
# 2016/01/15

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/classifiers")
def classifiers():
  return "Classifiers"

@app.route("/datasets")
def datasets():
  return "Datasets"

@app.route('/')
def index(name=None):
  return render_template('index.html', name=name)

if __name__ == "__main__":
  app.debug = True
  app.run()
