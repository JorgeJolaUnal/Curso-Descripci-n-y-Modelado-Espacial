from flask import Blueprint, render_template, request
import subprocess
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def tarea1():
    return render_template('tarea1.html')


@main.route('/tarea2')
def tarea2():
    return render_template('tarea2.html')

@main.route('/tarea3',methods=['GET', 'POST'])
def tarea3():
    if request.method == 'POST':
        test_type = request.form['test_type']
        cell_size = int(request.form['cell_size'])
        if test_type == 'fisher':
            result = subprocess.run(['Rscript', 'run_fisher_test.R', str(cell_size)], capture_output=True, text=True)
        elif test_type == 'chi':
            result = subprocess.run(['Rscript', 'run_chi_test.R', str(cell_size)], capture_output=True, text=True)
        return render_template('result.html', result=result.stdout)
    return render_template('tarea3.html')

