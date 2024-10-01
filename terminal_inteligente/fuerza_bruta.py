def fuerza_bruta(palabra1, palabra2, costos, i, j):
    if i == len(palabra1):
        return (len(palabra2) - j) * costos['insertar'], [
            "Insertar ({}) -> {}".format(palabra2[j], costos['insertar']) for j in range(j, len(palabra2))
        ]

    elif j == len(palabra2):
        return (len(palabra1) - i) * costos['borrar'], [
            "Borrar ({}) -> {}".format(palabra1[i], costos['borrar']) for i in range(i, len(palabra1))
        ]

    # Si los caracteres son iguales, no avanzamos automáticamente
    # sino que comparamos el costo de avanzar con el costo de otras operaciones
    costo_avanzar, acciones_avanzar = float('inf'), []
    if palabra1[i] == palabra2[j]:
        costo_avanzar, acciones_avanzar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j + 1)
        costo_avanzar += costos['avanzar']

    # Opción de reemplazar
    costo_reemplazar, acciones_reemplazar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j + 1)
    costo_reemplazar += costos['reemplazar']

    # Opción de insertar
    costo_insertar, acciones_insertar = fuerza_bruta(palabra1, palabra2, costos, i, j + 1)
    costo_insertar += costos['insertar']

    # Opción de borrar
    costo_borrar, acciones_borrar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j)
    costo_borrar += costos['borrar']

    # Elegimos el menor costo entre avanzar, reemplazar, insertar y borrar
    min_costo = min(costo_avanzar, costo_reemplazar, costo_insertar, costo_borrar)

    if min_costo == costo_avanzar:
        return costo_avanzar, ["Avanzar ({} == {}) -> {}".format(palabra1[i], palabra2[j], costos['avanzar'])] + acciones_avanzar
    elif min_costo == costo_reemplazar:
        return costo_reemplazar, ["Reemplazar ({} -> {}) -> {}".format(palabra1[i], palabra2[j], costos['reemplazar'])] + acciones_reemplazar
    elif min_costo == costo_insertar:
        return costo_insertar, ["Insertar ({}) -> {}".format(palabra2[j], costos['insertar'])] + acciones_insertar
    else:
        return costo_borrar, ["Borrar ({}) -> {}".format(palabra1[i], costos['borrar'])] + acciones_borrar

def solucion_fuerza_bruta(palabra1, palabra2, costos):
    costo, acciones = fuerza_bruta(palabra1, palabra2, costos, 0, 0)
    return costo

def mapeo_costos(pala1, pala2, costos):
    costo, acciones = fuerza_bruta(pala1, pala2, costos, 0, 0)
    return acciones
