import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QSoundEffect, QAudioOutput
from os.path import join


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Configuramos los widgets de la interfaz
        self.boton_sorpresa = QPushButton("Wooow", self)
        self.boton_empezar = QPushButton("Empezar música de fondo", self)
        self.boton_parar = QPushButton("Parar música de fondo", self)

        self.boton_sorpresa.setGeometry(10, 10, 230, 30)
        self.boton_empezar.setGeometry(10, 50, 230, 30)
        self.boton_parar.setGeometry(10, 90, 230, 30)

        self.boton_sorpresa.clicked.connect(self.empezar_sonido_sorpresa)
        self.boton_empezar.clicked.connect(self.empezar_musica_fondo)
        self.boton_parar.clicked.connect(self.parar_musica_fondo)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo Sonidos")
        self.setGeometry(50, 50, 250, 200)

        # Opción MP3: QMediaPlayer (reproduce muchos formatos, como MP3)
        # 1. Para que QMediaPlayer reproduzca audio, se debe agregar un QAudioOutput
        # 2. Usamos el path absoluto. Para generarlo usamos os.path.abspath
        #    (del módulo os), que transforma el path relativo en absoluto
        # 3. Se utiliza setSource para indicar el path al audio a escuchar
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        path = os.path.abspath(join("sounds", "waku-waku.mp3"))
        self.player.setSource(QUrl.fromLocalFile(path))

        # Opción WAV: QSoundEffect (solo reproduce archivos WAV)
        self.media_player_wav = QSoundEffect(self)
        self.media_player_wav.setVolume(0.1)  # Opcional
        # Como es música de fondo, la repetimos indefinidamente
        self.media_player_wav.setLoopCount(QSoundEffect.Loop.Infinite.value)
        file_url = QUrl.fromLocalFile(join("sounds", "see-you-again.wav"))
        self.media_player_wav.setSource(file_url)

        # Mostrar ventana
        self.show()

    def empezar_sonido_sorpresa(self) -> None:
        self.player.play()

    def empezar_musica_fondo(self) -> None:
        if not self.media_player_wav.isPlaying():
            self.media_player_wav.play()

    def parar_musica_fondo(self) -> None:
        if self.media_player_wav.isPlaying():
            self.media_player_wav.stop()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
