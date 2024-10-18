from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class Reloj(QObject):

    actualizar_hora_signal = pyqtSignal(int, int, int)
    actualizar_cronometro_signal = pyqtSignal(int, int, int, int)

    def __init__(self):
        super().__init__()
        self.segundo_actual = 0
        self.minuto_actual = 0
        self.hora_actual = 0
        self.milesima_cronometro = 0
        self.segundo_cronometro = 0
        self.minuto_cronometro = 0
        self.hora_cronometro = 0
        self.reloj = QTimer()
        self.reloj.setInterval(1000)
        self.reloj.timeout.connect(self.paso_del_tiempo)
        self.cronometro = QTimer()
        self.cronometro.setInterval(1)
        self.cronometro.timeout.connect(self.tiempo_cronometro)

    def paso_del_tiempo(self):
        if self.segundo_actual < 59:
            self.segundo_actual += 1
        else:
            self.segundo_actual = 0
            if self.minuto_actual < 59:
                self.minuto_actual += 1
            else:
                self.minuto_actual = 0
                if self.hora_actual < 23:
                    self.hora_actual += 1
                else:
                    self.hora_actual = 0
        self.actualizar_hora_signal.emit(self.hora_actual, self.minuto_actual, self.segundo_actual)

    def comenzar_reloj(self):
        self.reloj.start()

    def tiempo_cronometro(self):
        if self.milesima_cronometro < 9:
            self.milesima_cronometro += 1
        else:
            self.milesima_cronometro = 0
            if self.segundo_cronometro < 59:
                self.segundo_cronometro += 1
            else:
                self.segundo_cronometro = 0
                if self.minuto_cronometro < 59:
                    self.minuto_cronometro += 1
                else:
                    self.minuto_cronometro = 0
                    self.hora_cronometro += 1
        self.actualizar_cronometro_signal.emit(self.hora_cronometro, self.minuto_cronometro,
                                               self.segundo_cronometro, self.milesima_cronometro)

    def comenzar_cronometro(self):
        self.cronometro.start()

    def pausar_cronometro(self):
        self.cronometro.stop()

    def reiniciar_cronometro(self):
        self.milesima_cronometro = 0
        self.segundo_cronometro = 0
        self.minuto_cronometro = 0
        self.hora_cronometro = 0
        self.actualizar_cronometro_signal.emit(self.hora_cronometro, self.minuto_cronometro,
                                               self.segundo_cronometro, self.milesima_cronometro)

    def cambiar_hora(self, hora):
        if hora.count(":") == 2:
            hora = hora.split(":")
            if hora[0].isdigit() and hora[1].isdigit() and hora[2].isdigit():
                if int(hora[0]) < 24 and int(hora[1]) < 60 and int(hora[2]) < 60:
                    self.hora_actual = int(hora[0])
                    self.minuto_actual = int(hora[1])
                    self.segundo_actual = int(hora[2])
