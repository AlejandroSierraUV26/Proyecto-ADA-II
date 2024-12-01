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
    (120, 30, 2, [(10, 20, 40), (20, 30, 50)]),
    (100, 50, 3, [(30, 10, 50), (20, 20, 70), (10, 30, 90)]),
    (180, 40, 3, [(40, 10, 60), (20, 20, 70), (30, 30, 80)]),
    (150, 40, 4, [(50, 20, 60), (30, 10, 80), (40, 30, 100), (20, 10, 50)]),
    (220, 50, 4, [(50, 20, 70), (40, 10, 60), (30, 30, 80), (20, 10, 50)]),
    (200, 60, 5, [(60, 20, 70), (50, 30, 90), (40, 10, 80), (30, 20, 60), (20, 10, 50)]),
    (350, 60, 5, [(60, 10, 70), (50, 30, 80), (40, 20, 90), (30, 10, 100), (20, 40, 120)]),
    (400, 70, 5, [(70, 10, 90), (60, 30, 80), (50, 20, 70), (40, 10, 60), (30, 40, 100)]),
    (250, 80, 6, [(80, 10, 100), (70, 20, 90), (60, 30, 80), (50, 40, 70), (40, 10, 60), (30, 20, 50)]),
    (280, 70, 6, [(70, 30, 90), (60, 20, 80), (50, 10, 70), (40, 40, 110), (30, 20, 100), (20, 10, 50)]),
    (450, 90, 8, [(90, 10, 120), (80, 20, 110), (70, 30, 100), (60, 40, 90), (50, 20, 80), (40, 10, 70), (30, 30, 60), (20, 10, 50)]) #12
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