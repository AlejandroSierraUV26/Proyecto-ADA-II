from flask import Flask, render_template, request
from terminal_inteligente import fuerza_bruta as fb, programacion_dinamica as pd, voraz as vz

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        palabra1 = request.form.get('palabra1')
        palabra2 = request.form.get('palabra2')
        costos = {
            'avanzar': int(request.form.get('costo_avanzar', 1)),
            'borrar': int(request.form.get('costo_borrar', 2)),
            'insertar': int(request.form.get('costo_insertar', 2)),
            'reemplazar': int(request.form.get('costo_reemplazar', 3)),
            'destruir': int(request.form.get('costo_destruir', 1))
        }

        resultado_fb = fb.solucion_fuerza_bruta(palabra1, palabra2, costos)
        acciones_fb = fb.mapeo_costos(palabra1, palabra2, costos)

        resultado_vz, acciones_vz = vz.solucion_voraz(palabra1, palabra2, costos, acc=2)
        resultado_pd, acciones_pd = pd.solucion_dinamica(palabra1, palabra2, costos, acc=2)

        return render_template('index.html', palabra1=palabra1, palabra2=palabra2,
                               costos=costos, resultado_fb=resultado_fb,
                               acciones_fb=acciones_fb, resultado_vz=resultado_vz,
                               acciones_vz=acciones_vz, resultado_pd=resultado_pd,
                               acciones_pd=acciones_pd)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
