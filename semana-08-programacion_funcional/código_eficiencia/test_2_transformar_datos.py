import unittest
from collections import namedtuple
from typing import Generator

from utils import timeout, timer_decorator, memory_decorator, ruta_transacciones


# --- Elementos a testear ---

NamedTupleTransaccion = namedtuple('Estado', 'id,cc_num')


class ClaseTransacción:
    def __init__(self, _id, cc_num):
        self._id = _id
        self.cc_num = cc_num


def cargar_namedtuples() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = (int(x) for x in line.replace(', ', '-').strip().split(',')[:3:2])
            yield NamedTupleTransaccion(*info)

def cargar_clases() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = (int(x) for x in line.replace(', ', '-').strip().split(',')[:3:2])
            yield ClaseTransacción(*info)


# --- Función general para obtener datos desde los elementos a testear ---

N = 100000

def procesar_resultados(generador) -> list:
    return [next(generador) for _ in range(N)]


# --- Clase encargada de probar el código y hacer que tenga un tiempo máximo de ejecución ---

class TestNamedtuplesClases(unittest.TestCase):

    @timeout(60)
    @memory_decorator
    @timer_decorator
    def test_0_namedtuples(self) -> None:
        for _ in range(10):
            data = procesar_resultados(cargar_namedtuples())
        self.assertEqual(len(data), N)

    @timeout(60)
    @memory_decorator
    @timer_decorator
    def test_1_clases(self) -> None:
        for _ in range(10):
            data = procesar_resultados(cargar_clases())
        self.assertEqual(len(data), N)
