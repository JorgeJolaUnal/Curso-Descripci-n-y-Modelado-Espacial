from flask import Blueprint, render_template, request, redirect
import subprocess
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def tarea1():
    return render_template('tarea1.html')


@main.route('/tarea2')
def tarea2():
    return render_template('tarea2.html')

@main.route('/tarea3', methods=['GET', 'POST'])
def tarea3():
    return redirect("https://f0av15-jorge0andres-jola0hernandez.shinyapps.io/Tarea3/")

