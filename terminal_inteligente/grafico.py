import matplotlib.pyplot as plt
from test import pruebas

def leer_datos(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    pruebas = []
    tiempos_dinamica = []
    tiempos_fuerza_bruta = []
    tiempos_voraz = []

    for linea in lineas:
        if linea.startswith("Prueba con palabra1:"):
            pruebas.append(linea.strip())
        elif linea.startswith("D ="):
            tiempos_dinamica.append(float(linea.split(":")[1].strip()))
        elif linea.startswith("F ="):
            tiempos_fuerza_bruta.append(float(linea.split(":")[1].strip()))
        elif linea.startswith("V ="):
            tiempos_voraz.append(float(linea.split(":")[1].strip()))

    # Organizar de menor a mayor
    pruebas = sorted(pruebas)
    
    tiempos_dinamica = sorted(tiempos_dinamica)
    tiempos_fuerza_bruta = sorted(tiempos_fuerza_bruta)
    tiempos_voraz = sorted(tiempos_voraz)
    
    
    return pruebas, tiempos_dinamica, tiempos_fuerza_bruta, tiempos_voraz

def ordenar_datos(pruebas, tiempos_dinamica, tiempos_fuerza_bruta, tiempos_voraz):
    datos = list(zip(pruebas, tiempos_dinamica, tiempos_fuerza_bruta, tiempos_voraz))
    datos_ordenados = sorted(datos, key=lambda x: (x[1], x[2], x[3]))

    pruebas_ordenadas, tiempos_dinamica_ordenados, tiempos_fuerza_bruta_ordenados, tiempos_voraz_ordenados = zip(*datos_ordenados)
    return list(pruebas_ordenadas), list(tiempos_dinamica_ordenados), list(tiempos_fuerza_bruta_ordenados), list(tiempos_voraz_ordenados)

def graficar(pruebas, tiempos_dinamica, tiempos_fuerza_bruta, tiempos_voraz):
    indices = range(len(pruebas))

    plt.figure(figsize=(10, 6))
    plt.plot(indices, tiempos_dinamica, label='Programación Dinámica', marker='o')
    plt.plot(indices, tiempos_fuerza_bruta, label='Fuerza Bruta', marker='o')
    plt.plot(indices, tiempos_voraz, label='Voraz', marker='o')

    plt.xlabel('Pruebas')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.legend()
    plt.xticks(indices, [f'Prueba {i+1}' for i in indices], rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    pruebas()
    archivo = 'resultados.txt'
    pruebas, tiempos_dinamica, tiempos_fuerza_bruta, tiempos_voraz = leer_datos(archivo)
    graficar(pruebas, tiempos_dinamica, tiempos_fuerza_bruta, tiempos_voraz)