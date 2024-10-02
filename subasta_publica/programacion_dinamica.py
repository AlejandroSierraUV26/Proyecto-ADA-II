import numpy as np
def programacion_dinamica(MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers):
    # Tabla DP para almacenar el valor máximo posible con hasta A acciones
    dp = [[-float('inf')] * (MaxShares + 1) for _ in range(num_offers + 1)]
    dp[0][0] = 0  # Base: con 0 acciones y 0 ofertas, el valor es 0

    # Para rastrear las decisiones tomadas
    decisiones = [[[] for _ in range(MaxShares + 1)] for _ in range(num_offers + 1)]

    # Proceso de programación dinámica
    for i in range(1, num_offers + 1):
        precio, min_acciones, max_acciones = bidding_offers[i - 1]
        for x in range(MaxShares + 1):  # Iterar sobre cada cantidad posible de acciones asignadas

            if dp[i-1][x] == -float('inf'):

                continue  # Si no es posible llegar a este estado, saltar            # Intentar comprar entre el mínimo y el máximo número de acciones de la oferta actual

            for acciones in range(min_acciones, max_acciones + 1):

                if x + acciones <= MaxShares:  # Solo considerar si no excede el total de acciones
                    nuevo_valor = dp[i-1][x] + precio * acciones  # Calcular nuevo valor

                    if nuevo_valor > dp[i][x + acciones]:
                        dp[i][x + acciones] = nuevo_valor  # Actualizar valor máximo

                        # Guardar la decisión

                        decisiones[i][x + acciones] = decisiones[i-1][x] + [(i-1, acciones)]    # Buscar el mejor valor con la posibilidad de que el gobierno compre las acciones sobrantes

    max_valor = -float('inf')

    mejor_opcion = []    
    for x in range(MaxShares + 1):

        acciones_restantes = MaxShares - x  # Acciones que sobran después de las ofertas

        valor_gobierno = acciones_restantes * GovernmentBuyoutPrice  # Valor de las acciones sobrantes compradas por el gobierno

        total_valor = dp[num_offers][x] + valor_gobierno  # Valor total (ofertas + acciones sobrantes)        # Actualizar el valor máximo si encontramos una mejor opción

        if total_valor > max_valor:

            max_valor = total_valor

            mejor_opcion = decisiones[num_offers][x]  # Guardar la mejor combinación de ofertas    # Mostrar la mejor opción
    # dp = filtar_dp(dp)
    # print("Tabla DP: \n")
    # dp = np.array(dp)
    # print(dp)
    
    
    if mejor_opcion:
        # print("Mejor opción (ofertas):")
        # for oferta, cantidad in mejor_opcion:
        #     print(f"Oferta {oferta + 1}: Comprar {cantidad} acciones \nPrecio: ${f'{(bidding_offers[oferta][0] * cantidad):,}'.replace(",",".")}\n")    
        
    
        return max_valor
def filtar_dp(dp):
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j] == -float('inf'):
                dp[i][j] = 0
    return dp



