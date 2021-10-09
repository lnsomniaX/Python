#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импорт бибиотеки math
import numpy #импорт библиотеки numpy
import matplotlib.pyplot as mpp #импорт модуля pyplot из matlplotlib и присвоение ему имени mpp

if __name__=='__main__':          # проверяет, что модуль был запущен напрямую интерпритаором, а не импортирован.
    arguments = numpy.arange(0, 200, 0.1) #присваивает переменной "arguments" массив значений от 0 (включая) до 200 (не включая) с шагом 0.1
    mpp.plot(                     #построение графика
        arguments,                #аргумент функции принимает значения переменой "arguments"
        [math.sin(a) * math.sin(a/20.0) for a in arguments],#значения функции для каждого значения аргумента из массива "arguments" задаются уравнением sin(a)*sin(a/20), где a принимает все значения переменной "arguments"
        color='orange',           #задать оранжевый цвет графика
        label = 'sin(x)*six(x/20)'#имя графика
    )
    mpp.plot(                     #построение графика
        arguments,                #аргумент функции принимает значения переменой "arguments"
        [ math.cos(a/6) * math.log(a+1, 10)/1.3 for a in arguments],#значения функции для каждого значения аргумента из массива "arguments" задаются уравнением cos(x/6)*lg(x+1), где a принимает все значения переменной "arguments"
        color='purple',           #задать фиолетовый цвет графика
        label = 'cos(x/6)*lg(x+1)'#имя графика
    )
    mpp.xlabel('x', fontsize=14) #подписать ось абсцисс
    mpp.ylabel('y', fontsize=14) #подписать ось ординат
    mpp.grid(True, which='major', color='grey', linestyle='dashed')#задать сетку
    mpp.legend(loc='best')       #задать легенду графика
    mpp.show()                   #показать график