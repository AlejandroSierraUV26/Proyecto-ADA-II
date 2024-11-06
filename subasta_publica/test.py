import timeit
from programacion_dinamica import programacion_dinamica
from fuerza_bruta import fuerza_bruta
from voraz import solucion_voraz

def medir_tiempo(func, *args):
    def wrapper():
        return func(*args)
    return timeit.timeit(wrapper, number=1)

def pruebas():
    pruebas = [
    (12, 3, 2, [(1, 1, 4), (2, 2, 5)]),
    (10, 5, 3, [(3, 1, 5), (2, 2, 7), (1, 3, 9)]),
    (18, 4, 3, [(4, 1, 6), (2, 2, 7), (3, 3, 8)]),
    (15, 4, 4, [(5, 2, 6), (3, 1, 8), (4, 3, 10), (2, 1, 5)]),
    (22, 5, 4, [(5, 2, 7), (4, 1, 6), (3, 3, 8), (2, 1, 5)]),
    (20, 6, 5, [(6, 2, 7), (5, 3, 9), (4, 1, 8), (3, 2, 6), (2, 1, 5)]),
    (35, 6, 5, [(6, 1, 7), (5, 3, 8), (4, 2, 9), (3, 1, 10), (2, 4, 12)]),
    (40, 7, 5, [(7, 1, 9), (6, 3, 8), (5, 2, 7), (4, 1, 6), (3, 4, 10)]),
    (25, 8, 6, [(8, 1, 10), (7, 2, 9), (6, 3, 8), (5, 4, 7), (4, 1, 6), (3, 2, 5)]),
    (28, 7, 6, [(7, 3, 9), (6, 2, 8), (5, 1, 7), (4, 4, 11), (3, 2, 10), (2, 1, 5)]),
    (30, 10, 8, [(10, 2, 12), (9, 3, 11), (8, 1, 10), (7, 4, 9), (6, 2, 8), (5, 1, 7), (4, 3, 6), (3, 2, 5)]), # 9
    (45, 9, 8, [(9, 1, 12), (8, 2, 11), (7, 3, 10), (6, 4, 9), (5, 2, 8), (4, 1, 7), (3, 3, 6), (2, 1, 5)]) #12
    ]



    i = 0
    txt = ""
    for MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers in pruebas:
        txt += f"Prueba {i+1} con MaxShares: {MaxShares}, GovernmentBuyoutPrice: {GovernmentBuyoutPrice}, num_offers: {num_offers}, bidding_offers: {bidding_offers}\n"
        i += 1
        print(f"Prueba {i} con MaxShares: {MaxShares}, GovernmentBuyoutPrice: {GovernmentBuyoutPrice}, num_offers: {num_offers}, bidding_offers: {bidding_offers}")

        tiempo = medir_tiempo(programacion_dinamica, MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers)
        resultado = programacion_dinamica(MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers)
        txt += f"D = {i}: {tiempo:.6f}\n"
        print(f"D = {i}: {tiempo:.6f} => {resultado}")

        tiempo = medir_tiempo(fuerza_bruta, MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers,1)
        resultado = fuerza_bruta(MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers, 1)
        txt += f"F = x{i}: {tiempo:.6f}\n"
        print(f"F = {i}: {tiempo:.6f} => {resultado}")

        tiempo = medir_tiempo(solucion_voraz, MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers)
        resultado = solucion_voraz(MaxShares, GovernmentBuyoutPrice, num_offers, bidding_offers)
        txt += f"V = {i}: {tiempo:.6f}\n"
        print(f"V = {i}: {tiempo:.6f} => {resultado}")

        print("\n")

    with open("resultados_subastas.txt", "w") as f:
        f.write(txt)

if __name__ == "__main__":
    pruebas()