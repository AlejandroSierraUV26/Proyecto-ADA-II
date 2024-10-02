import fuerza_bruta as fb
import programacion_dinamica as pd
import voraz as vz  

import time
import numpy as np


A = 1000  # Cantidad total de acciones
B = 100   # Precio mínimo por acción que el gobierno paga por acciones sobrantes
n = 4     # Número de ofertas
ofertas = [
    (500, 700, 1000),  # Oferta 1: precio 500, mínimo 700 acciones, máximo 1000 acciones
    (450, 100, 400),   # Oferta 2: precio 450, mínimo 100 acciones, máximo 400 acciones
    (400, 100, 400),   # Oferta 3: precio 400, mínimo 100 acciones, máximo 400 acciones
    (200, 50, 200)     # Oferta 4: precio 200, mínimo 50 acciones, máximo 200 acciones
]



vz_start = time.time()
vz_valor = vz.solucion_voraz(A, B, n, ofertas)
vz_end = time.time()
print("Voraz:")
print(f"Valor máximo: ${vz_valor:,}".replace(',', '.'))
print(f"Tiempo: {vz_end - vz_start:.6f} segundos")
print()

pd_start = time.time()
pd_valor = pd.programacion_dinamica(A, B, n, ofertas)
pd_end = time.time()
print("Programación Dinámica:")
print(f"Valor máximo: ${pd_valor:,}".replace(',', '.'))
print(f"Tiempo: {pd_end - pd_start:.6f} segundos")
print()

fb_start = time.time()
fb_valor, fb_opcion = fb.fuerza_bruta(A, B, n, ofertas)
fb_end = time.time()
print("Fuerza Bruta:")
print(f"Valor máximo: ${fb_valor:,}".replace(',', '.'))
print(f"Tiempo: {fb_end - fb_start:.6f} segundos")
print()
