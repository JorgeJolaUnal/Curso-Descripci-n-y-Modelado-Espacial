from flask import Blueprint, render_template, request,send_from_directory ,jsonify, redirect
import numpy as np
from sympy import symbols, integrate,exp,sqrt

main=Blueprint('main',__name__)

@main.route('/')
def tarea1():
    return render_template('tarea1.html')