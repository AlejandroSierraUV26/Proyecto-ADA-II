def solucion_voraz(palabra1, palabra2, costos, acc=0):
    n = len(palabra1)
    m = len(palabra2)
    i, j = 0, 0
    costo_total = 0
    acciones = []

    # Mientras no hayamos recorrido completamente las palabras
    while i < n and j < m:
        if palabra1[i] == palabra2[j]:
            # Si los caracteres coinciden, elegimos entre avanzar o la opción más barata
            costo_avanzar = costos['avanzar']
            costo_reemplazar = costos['reemplazar']
            costo_borrar = costos['borrar']
            costo_insertar = costos['insertar']

            min_costo = min(costo_avanzar, costo_reemplazar, costo_borrar, costo_insertar)

            if min_costo == costo_avanzar:
                acciones.append(f"Avanzar ( {palabra1[i]} == {palabra2[j]} )")
                costo_total += costo_avanzar
                i += 1
                j += 1
            elif min_costo == costo_reemplazar:
                acciones.append(f"Reemplazar ( {palabra1[i]} -> {palabra2[j]} )")
                costo_total += costo_reemplazar
                i += 1
                j += 1
            elif min_costo == costo_borrar:
                acciones.append(f"Borrar ( {palabra1[i]} )")
                costo_total += costo_borrar
                i += 1
            else:
                acciones.append(f"Insertar ( {palabra2[j]} )")
                costo_total += costo_insertar
                j += 1
        else:
            # Si los caracteres no coinciden, consideramos reemplazar, borrar o insertar
            costo_reemplazar = costos['reemplazar']
            costo_borrar = costos['borrar']
            costo_insertar = costos['insertar']

            min_costo = min(costo_reemplazar, costo_borrar, costo_insertar)

            if min_costo == costo_reemplazar:
                acciones.append(f"Reemplazar ( {palabra1[i]} -> {palabra2[j]} )")
                costo_total += costo_reemplazar
                i += 1
                j += 1
            elif min_costo == costo_borrar:
                acciones.append(f"Borrar ( {palabra1[i]} )")
                costo_total += costo_borrar
                i += 1
            else:
                acciones.append(f"Insertar ( {palabra2[j]} )")
                costo_total += costo_insertar
                j += 1

    # Si quedan caracteres en palabra1, los borramos o destruimos
    while i < n:
        acciones.append(f"Borrar ( {palabra1[i]} )")
        costo_total += costos['borrar']
        i += 1

    # Si quedan caracteres en palabra2, los insertamos
    while j < m:
        acciones.append(f"Insertar ( {palabra2[j]} )")
        costo_total += costos['insertar']
        j += 1

    # Devolver resultados según acc
    if acc == 1:
        return acciones
    elif acc == 2:
        return costo_total, acciones
    return costo_total
