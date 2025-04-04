import unittest
from typing import Generator

from utils import timeout, timer_decorator, ruta_transacciones


# --- Consultas a testear ---

def cargar_archivo_generador() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        for line in file:
            yield line.strip().split(',')

def cargar_archivo_memoria() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        for line in file.readlines():
            yield line.strip().split(',')


# --- Función general para obtener datos desde las funciones a testear ---

N = 100000

def procesar_resultados(generador: Generator) -> list:
    return [next(generador) for _ in range(N)]


# --- Clase encargada de probar el código y hacer que tenga un tiempo máximo de ejecución ---

class TestCargarArchivo(unittest.TestCase):

    @timeout(60)
    @timer_decorator
    def test_0_generador(self) -> None:
        for _ in range(10):
            data = procesar_resultados(cargar_archivo_generador())
        self.assertEqual(len(data), N)

    @timeout(60)
    @timer_decorator
    def test_1_memoria(self) -> None:
        for _ in range(10):
            data = procesar_resultados(cargar_archivo_memoria())
        self.assertEqual(len(data), N)
