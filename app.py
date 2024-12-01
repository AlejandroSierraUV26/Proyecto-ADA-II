from flask import Flask, render_template, request, redirect, url_for, jsonify
from terminal_inteligente import fuerza_bruta as fb, programacion_dinamica as pd, voraz as vz
from subasta_publica import fuerza_bruta as fb_subasta, programacion_dinamica as pd_subasta, voraz as vz_subasta

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/terminal_inteligente', methods=['GET', 'POST'])
def terminal_inteligente():
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

        return render_template('terminal_inteligente.html', palabra1=palabra1, palabra2=palabra2,
                               costos=costos, resultado_fb=resultado_fb,
                               acciones_fb=acciones_fb, resultado_vz=resultado_vz,
                               acciones_vz=acciones_vz, resultado_pd=resultado_pd,
                               acciones_pd=acciones_pd)

    return render_template('terminal_inteligente.html')

@app.route('/subastas_publicas', methods=['GET', 'POST'])
def subastas_publicas():
    if request.method == 'POST':
        MaxShares = int(request.form['acciones'])
        GovernmentBuyoutPrice = int(request.form['precio_minimo'])
        ofertas = []

        i = 1
        while f'precio_{i}' in request.form:
            precio = int(request.form[f'precio_{i}'])
            minimo = int(request.form[f'minimo_{i}'])
            maximo = int(request.form[f'maximo_{i}'])
            ofertas.append((precio, minimo, maximo))
            i += 1

        num_offers = len(ofertas)

        resultado_pd, mejor_pd = pd_subasta.programacion_dinamica(MaxShares, GovernmentBuyoutPrice, num_offers, ofertas)
        resultado_fb, mejor_fb = fb_subasta.fuerza_bruta(MaxShares, GovernmentBuyoutPrice, num_offers, ofertas)
        resultado_voraz, mejor_vz = vz_subasta.solucion_voraz(MaxShares, GovernmentBuyoutPrice, num_offers, ofertas, 1)

        return jsonify({
            'resultado_pd': resultado_pd,
            'mejor_pd': mejor_pd,
            'resultado_fb': resultado_fb,
            'mejor_fb': mejor_fb,
            'resultado_voraz': resultado_voraz,
            'mejor_vz': mejor_vz
        })

    return render_template('subastas_publicas.html')
if __name__ == '__main__':
    app.run(debug=True)