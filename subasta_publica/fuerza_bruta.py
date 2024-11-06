import itertools

def fuerza_bruta(MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers, acc = 0):
    # Crear un rango de acciones posibles que se pueden comprar en cada oferta
    acciones_posibles = [
        range(bidding_offers[i][1], bidding_offers[i][2] + 1)
        for i in range(num_offers)
    ]
    
    max_valor = 0
    mejor_opcion = []

    # Evaluar todas las combinaciones posibles
    for combinacion in itertools.product(*acciones_posibles):
        if sum(combinacion) == MaxShares:  # Asegurarse de que la suma total es igual a MaxShares
            # Calcular el valor total de esta combinación
            valor_total = sum(combinacion[i] * bidding_offers[i][0] for i in range(num_offers))
            acciones_restantes = MaxShares - sum(combinacion)
            valor_gobierno = acciones_restantes * GovernmentBuyoutPrice
            
            total_valor = valor_total + valor_gobierno
            
            # Actualizar el mejor valor y opción
            if total_valor > max_valor:
                max_valor = total_valor
                mejor_opcion = combinacion

    if acc != 0:
        return max_valor
    return max_valor, mejor_opcion