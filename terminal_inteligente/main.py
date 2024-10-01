import fuerza_bruta as fb
import programacion_dinamica as pd
import voraz as vz  

import time
import numpy as np

# Comparacion de tiempos 
palabra1 = "oso" 
palabra2 = "oso" 

costos = {
    'avanzar': 1,
    'borrar': 2,
    'insertar': 2,
    'reemplazar': 1,
    'destruir': 1
}

# Fuerza Bruta
start = time.time()
acciones = fb.mapeo_costos(palabra1, palabra2, costos)
costo = fb.solucion_fuerza_bruta(palabra1, palabra2, costos)
end = time.time()
print(f"Costo: {costo}")
print(f"Acciones: {acciones}")
print(f"Tiempo: {end - start}")
print()
# Programacion Dinamica
start = time.time()
costo,acciones = pd.solucion_dinamica(palabra1, palabra2, costos, acc=2)
end = time.time()
print(f"Costo: {costo}")
print(f"Acciones: {acciones}")
print(f"Tiempo: {end - start}")
print()
# Voraz
start = time.time()
costo, acciones = vz.solucion_voraz(palabra1, palabra2, costos, acc=2)
end = time.time()
print(f"Costo: {costo}")
print(f"Tiempo: {end - start}")
print(f"Acciones: {acciones}")

