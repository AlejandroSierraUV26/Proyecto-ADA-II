def fuerza_bruta(palabra1, palabra2, costos, i, j):
    if i == len(palabra1) and j == len(palabra2):
        return 0, []
    
    elif i == len(palabra1):
        return (len(palabra2) - j) * costos['insertar'], ["Insertar ({})-> {}".format(palabra2[j], costos['insertar']) for j in range(j, len(palabra2))]
    
    elif j == len(palabra2):
        return (len(palabra1) - i) * costos['borrar'], ["Borrar ({})-> {}".format(palabra1[i], costos['borrar']) for i in range(i, len(palabra1))]
    
    elif palabra1[i] == palabra2[j]:
        costo, acciones = fuerza_bruta(palabra1, palabra2, costos, i + 1, j + 1)
        return costo + costos['avanzar'], ["Avanzar ({} == {}) -> {}".format(palabra1[i], palabra2[j], costos['avanzar'])] + acciones
    
    costo_reemplazar, acciones_reemplazar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j + 1)
    costo_reemplazar += costos['reemplazar']
    
    costo_insertar, acciones_insertar = fuerza_bruta(palabra1, palabra2, costos, i, j + 1)
    costo_insertar += costos['insertar']
    
    costo_borrar, acciones_borrar = fuerza_bruta(palabra1, palabra2, costos, i + 1, j)
    costo_borrar += costos['borrar']
    
    if costo_reemplazar <= costo_insertar and costo_reemplazar <= costo_borrar:
        return costo_reemplazar, ["Reemplazar ({} -> {}) -> {}".format(palabra1[i], palabra2[j], costos['reemplazar'])] + acciones_reemplazar
    elif costo_insertar <= costo_reemplazar and costo_insertar <= costo_borrar:
        return costo_insertar, ["Insertar ({}) -> {}".format(palabra2[j], costos['insertar'])] + acciones_insertar
    else:
        return costo_borrar, ["Borrar ({}) -> {}".format(palabra1[i], costos['borrar'])] + acciones_borrar

def solucion_fuerza_bruta(palabra1, palabra2, costos):
    costo, acciones = fuerza_bruta(palabra1, palabra2, costos, 0, 0)
    # print("Secuencia de acciones:")
    # for accion in acciones:
    #     print(accion)
    return costo
def mapeo_costos(pala1, pala2, costos):
    costo, acciones = fuerza_bruta(pala1, pala2, costos, 0, 0)
    return acciones


