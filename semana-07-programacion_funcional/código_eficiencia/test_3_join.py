import unittest
from collections import namedtuple, defaultdict
from functools import reduce
from itertools import product
from typing import Generator

from utils import timeout, timer_decorator, ruta_transacciones, ruta_estados


# --- Elementos a testear ---

def join_con_generadores(transacciones: Generator, estados: Generator) -> filter:
    join_generadores = product(transacciones, estados)
    join_filtrado = filter(lambda x: x[0].state == x[1][0], join_generadores)
    return join_filtrado


def join_manual(transacciones: Generator, estados: Generator) -> list:
    dict_transacciones = defaultdict(list)
    list(map(lambda t: dict_transacciones[t.state].append(t), transacciones))

    join_anidado = (((t, e) for t in dict_transacciones[e[0]]) for e in estados)
    join = reduce(lambda acc, t: acc + list(t), join_anidado, [])
    return join


# --- Función general para obtener datos desde los elementos a testear ---

Transacción = namedtuple('Transacción', 'id,trans_date_trans_time,cc_num,merchant,'\
                                        'category,amt,first,last,gender,street,city,'\
                                        'state,zip,lat,long,city_pop,job,dob,trans_num,'\
                                        'unix_time,merch_lat,merch_long,is_fraud,merch_zipcode')

Estado = namedtuple('Estado', 'id,nombre')

def cargar_transacciones() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = line.replace(', ', '-').strip().split(',')
            yield Transacción(*info)

def cargar_estados() -> Generator:
    with open(ruta_estados, encoding='utf-8') as file:
        for line in file:
            info = line.strip().split(';')
            yield Estado(*info)

def filtrar_transacciones(t) -> bool:
    return float(t.amt) < 10


# --- Clase encargada de probar el código y hacer que tenga un tiempo máximo de ejecución ---

class TestJoin(unittest.TestCase):

    @timeout(60)
    @timer_decorator
    def test_0_join_generadores(self) -> None:
        for _ in range(10):
            transacciones = cargar_transacciones()
            transacciones = filter(filtrar_transacciones, transacciones)
            estados = cargar_estados()
            resultado = join_con_generadores(transacciones, estados)
        self.assertEqual(len(list(resultado)), 335718)

    @timeout(60)
    @timer_decorator
    def test_1_join_manual(self) -> None:
        for _ in range(10):
            transacciones = cargar_transacciones()
            transacciones = filter(filtrar_transacciones, transacciones)
            estados = cargar_estados()
            resultado = join_manual(transacciones, estados)
        self.assertEqual(len(resultado), 335718)
