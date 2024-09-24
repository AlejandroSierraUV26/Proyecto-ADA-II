import numpy as np

def solucion_dinamica(palabra1, palabra2, costos):
    n = len(palabra1)
    m = len(palabra2)
    

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    acciones = [["" for _ in range(m + 1)] for _ in range(n + 1)]
    
    
    for i in range(n + 1):
        dp[i][0] = i * costos['borrar']  
        acciones[i][0] = "Borrar" if i > 0 else ""  
    
    for j in range(m + 1):
        dp[0][j] = j * costos['insertar'] 
        acciones[0][j] = "Insertar" if j > 0 else ""  
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                costo_reemplazar = 0  
                accion_reemplazar = "Avanzar"
            else:
                costo_reemplazar = costos['reemplazar']
                accion_reemplazar = "Reemplazar"
            
            costo_borrar = dp[i - 1][j] + costos['borrar']
            costo_insertar = dp[i][j - 1] + costos['insertar']
            costo_reemplazo = dp[i - 1][j - 1] + costo_reemplazar
            

            if costo_borrar <= costo_insertar and costo_borrar <= costo_reemplazo:
                dp[i][j] = costo_borrar
                acciones[i][j] = "Borrar"
            elif costo_insertar <= costo_borrar and costo_insertar <= costo_reemplazo:
                dp[i][j] = costo_insertar
                acciones[i][j] = "Insertar"
            else:
                dp[i][j] = costo_reemplazo
                acciones[i][j] = accion_reemplazar
    
    
    dp = np.array(dp)
    print("Matriz de costos:")
    print(dp)
    
    
    secuencia_acciones = []
    i, j = n, m
    while i > 0 or j > 0:
        accion = acciones[i][j]
        secuencia_acciones.append(accion)
        if accion == "Borrar":
            i -= 1
        elif accion == "Insertar":
            j -= 1
        else:  
            i -= 1
            j -= 1
    
    secuencia_acciones.reverse()
    for i in range(len(secuencia_acciones)):
        if secuencia_acciones[i] == "Avanzar":
            secuencia_acciones[i] = "Avanzar ({} == {})".format(palabra1[i], palabra2[i])
        elif secuencia_acciones[i] == "Reemplazar":
            secuencia_acciones[i] = "Reemplazar ({} -> {})".format(palabra1[i], palabra2[i])
        else:
            secuencia_acciones[i] = secuencia_acciones[i].capitalize()
    
    print("Secuencia de acciones:")
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

palabra1 = "ingeniero"
palabra2 = "ingenioso"
costos = {
    'avanzar': 1,
    'borrar': 2,
    'insertar': 2,
    'reemplazar': 3,
    'destruir': 1
}

print("Mapeo de costos:", mapeo_costos(costos))
print("Costo mínimo:", solucion_dinamica(palabra1, palabra2, costos))
