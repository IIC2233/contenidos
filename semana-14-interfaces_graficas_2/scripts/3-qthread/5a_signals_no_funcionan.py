import sys
from PyQt6.QtCore import QThread, QTimer, pyqtSignal
from PyQt6.QtWidgets import QApplication


class Thread1(QThread):
    signal_t1 = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.t2 = None

    def run(self) -> None:
        print("[Thread 1] Crear Thread 2")
        # OJO: este objeto se crea DENTRO de run, es decir, en el thread de T1.
        # Por lo tanto, el objeto t2 "vive" (tiene afinidad) en el thread de T1
        self.t2 = Thread2(self.signal_t1)

        print("[Thread 1] Conectar signal_t2 con imprimir de T2")
        self.t2.signal_t2.connect(self.t2.imprimir)

        print("[Thread 1] Ejecutar Thread 2 y esperar a que termine")
        self.t2.start()
        self.t2.wait()

        print("[Thread 1] Emitir signal_t1 y signal_t2")
        self.signal_t1.emit("signal_t1 emitida desde Thread 1")
        self.t2.signal_t2.emit("signal_t2 emitida desde Thread 1")

    def imprimir(self, texto: str) -> None:
        print("\t[imprimir de T1] ->", texto)


class Thread2(QThread):
    signal_t2 = pyqtSignal(str)

    def __init__(self, signal_t1: pyqtSignal) -> None:
        super().__init__()
        self.signal_t1 = signal_t1

    def run(self) -> None:
        print("[Thread 2] Emitir signal_t1 y signal_t2")
        self.signal_t1.emit("signal_t1 emitida desde Thread 2")
        self.signal_t2.emit("signal_t2 emitida desde Thread 2")

    def imprimir(self, texto: str) -> None:
        print("\t[imprimir de T2] ->", texto)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    print("[Main] Crear Thread 1")
    hilo = Thread1()
    print("[Main] Conectar signal_t1 con imprimir de T1")
    hilo.signal_t1.connect(hilo.imprimir)
    print("[Main] Ejecutar Thread 1")
    hilo.start()

    # Cerramos el programa después de 1 segundo
    QTimer.singleShot(1000, app.quit)
    app.exec()
    hilo.wait()
