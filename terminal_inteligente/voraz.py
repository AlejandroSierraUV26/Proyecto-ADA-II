def solucion_voraz(palabra1, palabra2, costos, acc = 0):
    n = len(palabra1)
    m = len(palabra2)
    i, j = 0, 0
    costo_total = 0
    acciones = []

    while i < n and j < m:
        if palabra1[i] == palabra2[j]:
            acciones.append(f"Avanzar ( {palabra1[i]} == {palabra2[j]} )")
            i += 1
            j += 1
            costo_total += costos['avanzar']
        else:
            acciones.append(f"Reemplazar ( {palabra1[i]} -> {palabra2[j]} )")
            i += 1
            j += 1
            costo_total += costos['reemplazar']
    
    while i < n:
        acciones.append(f"Borrar ( {palabra1[i]} )")
        i += 1
        costo_total += costos['borrar']

    while j < m:
        acciones.append(f"Insertar ( {palabra2[j]} )")
        j += 1
        costo_total += costos['insertar']

    
    # print("Secuencia de acciones:")
    # for accion in acciones:
    #     print(accion)
    if acc == 1:
        return acciones
    elif acc == 2:
        return costo_total, acciones
    return costo_total
