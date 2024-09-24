def fuerza_bruta(palabra1, palabra2, costos, i, j):
    if i == len(palabra1) and j == len(palabra2):
        return 0, []
    
    if i == len(palabra1):
        return (len(palabra2) - j) * costos['insertar'], ["Insertar"] * (len(palabra2) - j)
    
    if j == len(palabra2):
        return (len(palabra1) - i) * costos['borrar'], ["Borrar"] * (len(palabra1) - i)
    
    if palabra1[i] == palabra2[j]:
        costo, acciones = fuerza_bruta(palabra1, palabra2, costos, i + 1, j + 1)
        return costo, ["Avanzar ({} == {})".format(palabra1[i], palabra2[j])] + acciones
    
    costo_reemplazar, acciones_reemplazar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j + 1)
    costo_reemplazar += costos['reemplazar']
    
    costo_insertar, acciones_insertar = fuerza_bruta(palabra1, palabra2, costos, i, j + 1)
    costo_insertar += costos['insertar']
    
    costo_borrar, acciones_borrar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j)
    costo_borrar += costos['borrar']
    
    if costo_reemplazar <= costo_insertar and costo_reemplazar <= costo_borrar:
        return costo_reemplazar, ["Reemplazar ({} -> {})".format(palabra1[i], palabra2[j])] + acciones_reemplazar
    elif costo_insertar <= costo_reemplazar and costo_insertar <= costo_borrar:
        return costo_insertar, ["Insertar"] + acciones_insertar
    else:
        return costo_borrar, ["Borrar"] + acciones_borrar

def solucion_fuerza_bruta(palabra1, palabra2, costos):
    costo, acciones = fuerza_bruta(palabra1, palabra2, costos, 0, 0)
    print("Secuencia de acciones:")
    for accion in acciones:
        print(accion)
    return costo


palabra1 = "ingeniero"
palabra2 = "ingenioso"
costos = {
    'avanzar': 1,
    'borrar': 2,
    'insertar': 2,
    'reemplazar': 3,
    'destruir': 1
}

print("Costo mínimo con fuerza bruta:", solucion_fuerza_bruta(palabra1, palabra2, costos))
