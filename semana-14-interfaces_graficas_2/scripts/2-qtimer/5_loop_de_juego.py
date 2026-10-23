import sys
from random import randint
from PyQt6.QtCore import QObject, QTimer, Qt, pyqtSignal
from PyQt6.QtGui import QColor, QKeyEvent, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

ANCHO, ALTO = 500, 400
TAMAÑO = 20
CANTIDAD_PELOTAS = 30
TICK_MS = 16  # ~60 actualizaciones por segundo


class Pelota:
    """
    Una pelota es solo datos: posición y velocidad. No es un thread ni un
    QObject, porque no hace nada por sí misma. Quien la mueve es el Juego.
    """

    def __init__(self, id_pelota: int) -> None:
        self.id = id_pelota
        self.x = randint(0, ANCHO - TAMAÑO)
        self.y = randint(0, ALTO - TAMAÑO)
        self.vx = randint(-4, 4) or 1
        self.vy = randint(-4, 4) or 1

    def mover(self) -> None:
        self.x += self.vx
        self.y += self.vy
        # Rebotamos en los bordes de la ventana
        if not 0 <= self.x <= ANCHO - TAMAÑO:
            self.vx *= -1
        if not 0 <= self.y <= ALTO - TAMAÑO:
            self.vy *= -1


class Juego(QObject):
    """
    Back-end. Un único QTimer hace avanzar a TODAS las pelotas en cada tick.
    """

    senal_mover = pyqtSignal(int, int, int)  # id, x, y
    senal_pausa = pyqtSignal(bool)  # True si quedó en pausa

    def __init__(self) -> None:
        super().__init__()
        self.pelotas = [Pelota(i) for i in range(CANTIDAD_PELOTAS)]
        self.timer = QTimer(self)
        self.timer.setInterval(TICK_MS)
        self.timer.timeout.connect(self.tick)

    def iniciar(self) -> None:
        self.timer.start()

    def tick(self) -> None:
        # En cada tick actualizamos el estado de todo el juego y avisamos
        # al front-end. Todo ocurre en el thread principal: no hay
        # problemas de concurrencia que cuidar
        for pelota in self.pelotas:
            pelota.mover()
            self.senal_mover.emit(pelota.id, pelota.x, pelota.y)

    def pausar_o_reanudar(self) -> None:
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()
        self.senal_pausa.emit(not self.timer.isActive())


class Ventana(QWidget):
    """
    Front-end. Solo dibuja lo que le dice el back-end y le avisa
    cuando el usuario presiona la barra espaciadora.
    """

    senal_tecla_pausa = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Loop de juego con un QTimer (Espacio: pausa)")
        self.setFixedSize(ANCHO, ALTO)
        self.setStyleSheet("background: #1e1e2e;")

        self.labels = {}
        for i in range(CANTIDAD_PELOTAS):
            pixmap = QPixmap(TAMAÑO, TAMAÑO)
            pixmap.fill(QColor(randint(80, 255), randint(80, 255), randint(80, 255)))
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setGeometry(-TAMAÑO, -TAMAÑO, TAMAÑO, TAMAÑO)
            self.labels[i] = label

        self.label_pausa = QLabel("PAUSA", self)
        self.label_pausa.setStyleSheet("color: white; font-size: 40px;")
        self.label_pausa.setGeometry(ANCHO // 2 - 70, ALTO // 2 - 30, 140, 60)
        self.label_pausa.hide()

    def mover(self, id_pelota: int, x: int, y: int) -> None:
        self.labels[id_pelota].move(x, y)

    def mostrar_pausa(self, en_pausa: bool) -> None:
        self.label_pausa.setVisible(en_pausa)

    def keyPressEvent(self, evento: QKeyEvent) -> None:
        if evento.key() == Qt.Key.Key_Space and not evento.isAutoRepeat():
            self.senal_tecla_pausa.emit()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    juego = Juego()
    ventana = Ventana()

    # Conectamos back-end y front-end
    juego.senal_mover.connect(ventana.mover)
    juego.senal_pausa.connect(ventana.mostrar_pausa)
    ventana.senal_tecla_pausa.connect(juego.pausar_o_reanudar)

    ventana.show()
    juego.iniciar()
    sys.exit(app.exec())
