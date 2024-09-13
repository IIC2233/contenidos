import unittest
from collections import namedtuple
from functools import reduce
from typing import Generator

from utils import timeout, timer_decorator, ruta_transacciones


# --- Elementos a testear ---

def filtrar_con_generadores(datos: Generator) -> int:
    datos = filter(lambda x: x.gender == 'F' and x.city == 'Dublin', datos)
    cantidad = reduce(lambda total, _: total + 1, datos, 0)
    return cantidad

def filtrar_con_listas(datos: list) -> int:
    datos = list(datos)
    datos = filter(lambda x: x.gender == 'F' and x.city == 'Dublin', datos)
    cantidad = reduce(lambda total, _: total + 1, datos, 0)
    return cantidad


# --- Función general para obtener datos desde los elementos a testear ---

Transacción = namedtuple('Transacción', 'id,trans_date_trans_time,cc_num,merchant,'\
                                        'category,amt,first,last,gender,street,city,'\
                                        'state,zip,lat,long,city_pop,job,dob,trans_num,'\
                                        'unix_time,merch_lat,merch_long,is_fraud,merch_zipcode')

def cargar_transacciones() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = line.replace(', ', '-').strip().split(',')
            yield Transacción(*info)


# --- Clase encargada de probar el código y hacer que tenga un tiempo máximo de ejecución ---

class TestGeneradoresIterables(unittest.TestCase):

    @timeout(60)
    @timer_decorator
    def test_0_generadores(self) -> None:
        for _ in range(10):
            data = cargar_transacciones()
            resultado = filtrar_con_generadores(data)
        self.assertEqual(resultado, 552)

    @timeout(60)
    @timer_decorator
    def test_1_listas(self) -> None:
        for _ in range(10):
            data = cargar_transacciones()
            resultado = filtrar_con_listas(data)
        self.assertEqual(resultado, 552)
