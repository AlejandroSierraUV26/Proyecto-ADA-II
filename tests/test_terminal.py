import sys
import os

# Agrega el directorio raíz del proyecto al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from terminal_inteligente import fuerza_bruta as fb, programacion_dinamica as pd, voraz as vz
import unittest
import time


class TestSoluciones(unittest.TestCase):
    def setUp(self):
        # Palabras de prueba y costos
        self.palabra1 = "oso"
        self.palabra2 = "casa"
        
        self.palabra3 = "algorithm"
        self.palabra4 = "altruistic"
        
        self.palabra5 = "ingenioso"
        self.palabra6 = "ingenierio"
        
        self.palabra7 = "francesa"
        self.palabra8 = "ancestro"
        
        
        self.costos = {
            'avanzar': 1,
            'borrar': 2,
            'insertar': 2,
            'reemplazar': 3,
            'destruir': 1
        }
    

    def test_solucion_fuerza_bruta(self):
        resultado1 = fb.solucion_fuerza_bruta(self.palabra1, self.palabra2, self.costos)
        self.assertEqual(resultado1, 9)
        
        resultado2 = fb.solucion_fuerza_bruta(self.palabra3, self.palabra4, self.costos)
        self.assertEqual(resultado2, 20)
        
        resultado3 = fb.solucion_fuerza_bruta(self.palabra5, self.palabra6, self.costos)
        self.assertEqual(resultado3, 15)
        
        resultado4 = fb.solucion_fuerza_bruta(self.palabra7, self.palabra8, self.costos)
        self.assertEqual(resultado4, 16)
        
        

    def test_solucion_voraz(self):
        resultado1 = vz.solucion_voraz(self.palabra1, self.palabra2, self.costos)
        self.assertEqual(resultado1, 11)
        
        resultado2 = vz.solucion_voraz(self.palabra3, self.palabra4, self.costos)
        self.assertEqual(resultado2, 23)
        
        resultado3 = vz.solucion_voraz(self.palabra5, self.palabra6, self.costos)
        self.assertEqual(resultado3, 17)
        
        resultado4 = vz.solucion_voraz(self.palabra7, self.palabra8, self.costos)
        self.assertEqual(resultado4, 24)
        
        

    def test_solucion_dinamica(self):
        resultado1 = pd.solucion_dinamica(self.palabra1, self.palabra2, self.costos)
        self.assertEqual(resultado1, 9)
        
        resultado2 = pd.solucion_dinamica(self.palabra3, self.palabra4, self.costos)
        self.assertEqual(resultado2, 20)
        
        resultado3 = pd.solucion_dinamica(self.palabra5, self.palabra6, self.costos)
        self.assertEqual(resultado3, 15)
        
        resultado4 = pd.solucion_dinamica(self.palabra7, self.palabra8, self.costos)
        self.assertEqual(resultado4, 16)
        
        

    def test_comparacion_tiempos(self):
        # Medición de tiempos
        tiempos = {}
        start_time = time.time()
        fb.solucion_fuerza_bruta(self.palabra1, self.palabra2, self.costos)
        tiempos['fuerza_bruta'] = time.time() - start_time

        start_time = time.time()
        vz.solucion_voraz(self.palabra1, self.palabra2, self.costos)
        tiempos['voraz'] = time.time() - start_time

        start_time = time.time()
        pd.solucion_dinamica(self.palabra1, self.palabra2, self.costos)
        tiempos['dinamica'] = time.time() - start_time

        # Verificar que los tiempos sean razonables (no negativos)
        for metodo, tiempo in tiempos.items():
            self.assertGreaterEqual(tiempo, 0, f"El tiempo para {metodo} es negativo, algo está mal.")

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_terminal