import numpy as np

def solucion_dinamica(palabra1, palabra2, costos):
    n = len(palabra1)
    m = len(palabra2)
    

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    acciones = [["" for _ in range(m + 1)] for _ in range(n + 1)]

    
    for i in range(n + 1):
        dp[i][0] = i * costos['borrar']  

        acciones[i][0] = f"Borrar -> {costos['borrar']}" if i > 0 else ""  
    
    for j in range(m + 1):
        dp[0][j] = j * costos['insertar'] 
        acciones[0][j] = f"Insertar -> {costos['insertar']}" if j > 0 else ""  
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                costo_avanzar = dp[i - 1][j - 1] + costos['avanzar'] 
                accion_avanzar = f"Avanzar ( {palabra1[i - 1]} == {palabra2[j - 1]} ) -> {costos['avanzar']}"
            else:
                costo_reemplazar = dp[i - 1][j - 1] + costos['reemplazar']
                accion_reemplazar = f"Reemplazar ( {palabra1[i - 1]} -> {palabra2[j - 1]} ) -> {costos['reemplazar']}"
            
            costo_borrar = dp[i - 1][j] + costos['borrar']
            costo_insertar = dp[i][j - 1] + costos['insertar']
            

            if palabra1[i - 1] == palabra2[j - 1]: 
                dp[i][j] = costo_avanzar
                acciones[i][j] = accion_avanzar
            elif costo_borrar <= costo_insertar and costo_borrar <= costo_reemplazar:
                dp[i][j] = costo_borrar
                acciones[i][j] = f"Borrar ( {palabra1[i - 1]} ) -> {costos['borrar']}"
            elif costo_insertar <= costo_borrar and costo_insertar <= costo_reemplazar:
                dp[i][j] = costo_insertar
                acciones[i][j] = f"Insertar ( {palabra2[j - 1]} ) -> {costos['insertar']}"
            else:
                dp[i][j] = costo_reemplazar
                acciones[i][j] = accion_reemplazar
    
    
    dp = np.array(dp)
    # print("Matriz de costos:")
    # print(dp)
    
    
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
    
    print("Secuencia de acciones con costos:")
    for accion in secuencia_acciones:
        print(accion)
        
    
    return dp[n][m]

def mapeo_costos(costos):
    return {
        'avanzar': costos['avanzar'],
        'borrar': costos['borrar'],
        'insertar': costos['insertar'],
        'reemplazar': costos['reemplazar'],
        'destruir': costos['destruir']
    }
