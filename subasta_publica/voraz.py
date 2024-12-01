def solucion_voraz(MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers, acc=0):
    # Ordenar ofertas por precio por acción en orden descendente
    ofertas_ordenadas = sorted(bidding_offers, key=lambda x: x[0], reverse=True)
    
    total_valor = 0
    acciones_vendidas = 0
    mejor_opcion = []

    # Iterar sobre las ofertas ordenadas
    for i in range(num_offers):
        precio, min_acciones, max_acciones = ofertas_ordenadas[i]
        
        # Calcular la cantidad de acciones a comprar en esta oferta
        acciones_a_comprar = min(max_acciones, MaxShares - acciones_vendidas)
        
        if acciones_a_comprar >= min_acciones:
            acciones_a_comprar = max(acciones_a_comprar, min_acciones)
            total_valor += acciones_a_comprar * precio
            acciones_vendidas += acciones_a_comprar
            mejor_opcion.append((i + 1, acciones_a_comprar))  # Guardar la oferta (i+1 por índice 1)
        
        # Si ya hemos vendido todas las acciones, romper el bucle
        if acciones_vendidas >= MaxShares:
            break

    # Calcular el valor de las acciones que quedan para el gobierno
    acciones_restantes = MaxShares - acciones_vendidas
    valor_gobierno = acciones_restantes * GovernmentBuyoutPrice
    total_valor += valor_gobierno

    # Mostrar la mejor opción

    # for oferta, cantidad in mejor_opcion:
    #     print(f"Oferta {oferta}: Comprar {cantidad} acciones \nPrecio: ${f'{cantidad * bidding_offers[oferta - 1][0]:,}'.replace(',', '.')}\n")
    if acc == 0:
        return total_valor
    else:
        return total_valor, mejor_opcion

