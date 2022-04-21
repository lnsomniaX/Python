#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...
import numpy as np
import flask
from flask import Flask, request
import scipy.optimize
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import requests

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.context_processor
def inject_globals():
    return {
        "isclever": [
            "глупый",
            "умный",
            "маленький"
        ]
    }


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/name', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param is None:
        name_param="Анонимус"
    print(name_param)
    return flask.render_template(
        'name.html',
        name=name_param,
        method=request.method
    )


@app.route('/graph', methods = ['GET'])
def graph():
    graphic_param = request.args.get('graphic')
    name_param = request.args.get('name')
    plot_url=0
    if graphic_param == 'exponential':
        img = BytesIO()
        if name_param is None:
            CAT_IMAGE_URL = 'https://i.imgur.com/xYUVlZ0.jpg'

            response = requests.get(CAT_IMAGE_URL)
            with open('test.png', 'wb') as f:
                f.write(response.content)
            plot_url = base64.b64encode(open('test.png', 'rb').read()).decode('utf-8')


        if name_param is not None:
            print(name_param)
            A = name_param.split(', ')
            X = A[0]
            X = X.split()
            X = np.array(X)
            number = []
            for item in X:
                number.append(float(item))
            X = number
            X = np.array(X)

            Y = A[1]
            Y = Y.split()
            Y = np.array(Y)
            number = []
            for item in Y:
                number.append(float(item))
            Y = number
            Y = np.array(Y)

            plt.scatter(X, Y, color='blue', s=3, linewidth=2.0)
            C = 0

            for item in X:
                C += 1
            def exp(x, a, b):
                 return a * np.exp(b * x)

            popt, cov = scipy.optimize.curve_fit(exp, X, Y)
            a, b = popt

            first_X = np.linspace(X[0], X[C-1], 100)

            plt.plot(first_X, a * np.exp(first_X * b), color='green', label='Экспоненциальное приближение'
                                                                             ' зависимости напряжения на конденсаторе'
                                                                             ' от времени')
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return flask.render_template(
        'graph.html',
        graphic=graphic_param,
        name=name_param,
        plot_url=plot_url,
    )
if __name__ == '__main__':
   app.run(debug = True)
