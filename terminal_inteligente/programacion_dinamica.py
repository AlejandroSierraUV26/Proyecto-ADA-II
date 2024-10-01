import numpy as np

def solucion_dinamica(palabra1, palabra2, costos, acc = 0):
    n = len(palabra1)
    m = len(palabra2)

    # Inicialización de las tablas de costos y acciones
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    acciones = [["" for _ in range(m + 1)] for _ in range(n + 1)]

    # Inicializar primera fila y primera columna
    for i in range(n + 1):
        dp[i][0] = i * costos['borrar']
        acciones[i][0] = f"Borrar -> {costos['borrar']}" if i > 0 else ""
    
    for j in range(m + 1):
        dp[0][j] = j * costos['insertar']
        acciones[0][j] = f"Insertar -> {costos['insertar']}" if j > 0 else ""
    
    # Rellenar la tabla de dp y acciones
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            costo_borrar = dp[i - 1][j] + costos['borrar']
            costo_insertar = dp[i][j - 1] + costos['insertar']
            
            if palabra1[i - 1] == palabra2[j - 1]:
                costo_avanzar = dp[i - 1][j - 1] + costos['avanzar']
                accion_avanzar = f"Avanzar ( {palabra1[i - 1]} == {palabra2[j - 1]} ) -> {costos['avanzar']}"
            else:
                costo_avanzar = float('inf')  # No es una opción válida si los caracteres no coinciden
                accion_avanzar = ""

            costo_reemplazar = dp[i - 1][j - 1] + costos['reemplazar']
            accion_reemplazar = f"Reemplazar ( {palabra1[i - 1]} -> {palabra2[j - 1]} ) -> {costos['reemplazar']}"
            
            # Seleccionar la acción con el costo mínimo
            min_costo = min(costo_avanzar, costo_borrar, costo_insertar, costo_reemplazar)
            
            if min_costo == costo_avanzar:
                dp[i][j] = costo_avanzar
                acciones[i][j] = accion_avanzar
            elif min_costo == costo_borrar:
                dp[i][j] = costo_borrar
                acciones[i][j] = f"Borrar ( {palabra1[i - 1]} ) -> {costos['borrar']}"
            elif min_costo == costo_insertar:
                dp[i][j] = costo_insertar
                acciones[i][j] = f"Insertar ( {palabra2[j - 1]} ) -> {costos['insertar']}"
            else:
                dp[i][j] = costo_reemplazar
                acciones[i][j] = accion_reemplazar

    # Reconstrucción de la secuencia de acciones
    secuencia_acciones = []
    i, j = n, m
    while i > 0 or j > 0:
        accion = acciones[i][j]
        secuencia_acciones.append(accion)
        if "Borrar" in accion:
            i -= 1
        elif "Insertar" in accion:
            j -= 1
        else:
            i -= 1
            j -= 1
    
    secuencia_acciones.reverse()
    
    # Devolver resultados según la opción elegida (solo costo, solo acciones o ambos)
    if acc == 1:
        return secuencia_acciones
    elif acc == 2:
        return dp[n][m], secuencia_acciones
    return dp[n][m]
