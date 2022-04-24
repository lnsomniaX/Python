#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...
# 0 0.9 1.8 2.8 3.8 4.8 5.7, 3.8 2.3 1.4 0.8 0.5 0.3 0.2
import base64
from io import BytesIO
import flask
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import requests
import scipy.optimize
from flask import Flask, render_template, \
    request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def index():
    return render_template(
        'graph_select.html',
        data=[{'name': 'exponential'}, {'name': 'linear'}, {'name': 'quadratic'}])


@app.route("/graph", methods=['GET', 'POST'])
def test():
    name_param = request.args.get('name')
    request.form.get('graph_select')
    graph = 'exponential'
    plot_url = 0
    print(name_param)

    if name_param is not None:
        csfont = {'fontname': 'Liberation Serif'}
        print(name_param)
        p = name_param.split(', ')
        x = np.array(p[0].split())
        number = []
        for item in x:
            number.append(float(item))
        x = np.array(number)

        y = np.array(p[1].split())
        number = []
        for item in y:
            number.append(float(item))
        y = np.array(number)

        plt.scatter(x, y, color='blue', s=3, linewidth=2.0)
        c = 0

        for item in x:
            c += 1

        if graph == 'exponential':
            def exp(x1, a, b):
                return a * np.exp(b * x1)

            popt, cov = scipy.optimize.curve_fit(exp, x, y)
            a, b = popt

            first_X = np.linspace(x[0], x[c - 1], 100)

            plt.plot(first_X, a * np.exp(first_X * b), color='green', label='Экспоненциальное приближение'
                     )
        img = BytesIO()
        plt.xlabel('X', fontsize=14, **csfont)
        plt.ylabel('Y', fontsize=14, **csfont)
        plt.grid()
        plt.legend(loc='best')
        plt.minorticks_on()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    if name_param is None:
        cat_image_url = 'https://i.imgur.com/xYUVlZ0.jpg'

        response = requests.get(cat_image_url)
        with open('test.png', 'wb') as f:
            f.write(response.content)
        plot_url = base64.b64encode(open('test.png', 'rb').read()).decode('utf-8')
        name_param = ''

    return flask.render_template('graph.html',
                                 name=name_param,
                                 plot_url=plot_url, )


if __name__ == '__main__':
    app.run(debug=True)
