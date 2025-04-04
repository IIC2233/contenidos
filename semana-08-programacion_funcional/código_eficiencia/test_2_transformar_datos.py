import unittest
from collections import namedtuple
from typing import Generator

from utils import timeout, timer_decorator, memory_decorator, ruta_transacciones


# --- Elementos a testear ---

NamedTupleTransacción = namedtuple('Transacción', 'id,trans_date_trans_time,cc_num,merchant,'\
                                        'category,amt,first,last,gender,street,city,'\
                                        'state,zip,lat,long,city_pop,job,dob,trans_num,'\
                                        'unix_time,merch_lat,merch_long,is_fraud,merch_zipcode')


class ClaseTransacción:
    def __init__(self, _id, trans_date_trans_time, cc_num, merchant, category, amt, first, 
                    last, gender, street, city, state, zip, lat, long, city_pop, job, dob,
                    trans_num, unix_time, merch_lat, merch_long, is_fraud, merch_zipcode):
        self._id = _id
        self.trans_date_trans_time = trans_date_trans_time
        self.cc_num = cc_num
        self.merchant = merchant
        self.category = category
        self.amt = amt
        self.first = first
        self.last = last
        self.gender = gender
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.lat = lat
        self.long = long
        self.city_pop = city_pop
        self.job = job
        self.dob = dob
        self.trans_num = trans_num
        self.unix_time = unix_time
        self.merch_lat = merch_lat
        self.merch_long = merch_long
        self.is_fraud = is_fraud
        self.merch_zipcode = merch_zipcode

    def método_1(self, *args, **kwargs):
        # Método que hace algo random
        texto = self.gender
        return texto.upper()

    def método_2(self, *args, **kwargs):
        # Método que hace otra cosa random
        return self.lat, self.long

    def método_3(self, *args, **kwargs):
        # Método que hace más cosas random
        fraud = float(self.is_fraud) > 50
        return fraud


def cargar_namedtuples() -> Generator:
    with open(ruta_transacciones, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = line.replace(', ', '-').strip().split(',')
            yield NamedTupleTransacción(*info)

def cargar_clases() :
    with open(ruta_transacciones, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = line.replace(', ', '-').strip().split(',')
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
