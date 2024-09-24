import fuerza_bruta as fb
import programacion_dinamica as pd
import voraz as vz  

import time
import numpy as np

# Comparacion de tiempos
palabra1 = "francesa" 
palabra2 = "frambuesas"  

costos = {
    'avanzar': 1,
    'borrar': 2,
    'insertar': 2,
    'reemplazar': 3,
    'destruir': 1
}

print("Comparación de tiempos:")
print("=" * 25)
start_time = time.time()

fb_costo = fb.solucion_fuerza_bruta(palabra1, palabra2, costos)

end_time = time.time()
print("=" * 25)

print(f"Costo de la solución por fuerza bruta: {fb_costo}")
print(f"Tiempo de ejecución: {end_time - start_time}")
print()


start_time = time.time()
print("=" * 25)
vz_costo = vz.solucion_voraz(palabra1, palabra2, costos)

end_time = time.time()
print("=" * 25)
print()
print(f"Costo de la solución voraz: {vz_costo}")
print(f"Tiempo de ejecución: {end_time - start_time}")
print()

start_time = time.time()

pd_costo = pd.solucion_dinamica(palabra1, palabra2, costos)

end_time = time.time()
print("=" * 25)
print()
print(f"Costo de la solución por programación dinámica: {pd_costo}")
print(f"Tiempo de ejecución: {end_time - start_time}")
print("=" * 25)
print()
