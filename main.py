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
        test_type = request.form['test_type']  # 'chi' o 'fisher'
        cell_size = int(request.form['cell_size'])  # Tamaño de la celda
        
        # Determinar el script de R a ejecutar
        if test_type == 'fisher':
            r_script = 'run_fisher_test.R'
        elif test_type == 'chi':
            r_script = 'run_chi_test.R'
        else:
            return "Tipo de prueba no válido", 400
        
        # Ejecutar el script de R
        result = subprocess.run(['Rscript', r_script, str(cell_size)], capture_output=True, text=True)
        
        # Pasar el resultado del test a la plantilla de resultados
        return render_template('result.html', result=result.stdout)
    return render_template('tarea3.html')

