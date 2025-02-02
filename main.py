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
        
        # Ruta completa al ejecutable Rscript
        rscript_path = '/usr/local/bin/Rscript'  # Ajusta esta ruta según la ubicación de Rscript en tu contenedor
        
        # Ejecutar el script en R, pasando el tamaño de la celda
        if test_type == 'fisher':
            result = subprocess.run([rscript_path, 'run_fisher_test.R', str(cell_size)], capture_output=True, text=True)
        elif test_type == 'chi':
            result = subprocess.run([rscript_path, 'run_chi_test.R', str(cell_size)], capture_output=True, text=True)
        
        # Pasar el resultado del test a la plantilla de resultados
        return render_template('result.html', result=result.stdout)
    return render_template('tarea3.html')

