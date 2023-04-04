import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui
from Interfaces.tablero import  Ui_Tablero
from Interfaces.clickableLabel import ClickableLabel

class tablero_implementacion(QMainWindow):
    misCartas = ['oros-12', 'oros-4', 'copas-3', 'copas-7', 'copas-11', 'espadas-5']
    numCartaSeleccionada = -1
    cartaSeleccionada = None

    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()
    
    def inicializarGUI(self):
        self.ui = Ui_Tablero()
        self.ui.setupUi(self)

        #Conectar señales cartas
        self.rellenarMiMano()
        self.ui.carta1.clicked.connect(lambda: self.seleccionarCarta(1, self.ui.carta1))
        self.ui.carta2.clicked.connect(lambda: self.seleccionarCarta(2, self.ui.carta2))
        self.ui.carta3.clicked.connect(lambda: self.seleccionarCarta(3, self.ui.carta3))
        self.ui.carta4.clicked.connect(lambda: self.seleccionarCarta(4, self.ui.carta4))
        self.ui.carta5.clicked.connect(lambda: self.seleccionarCarta(5, self.ui.carta5))
        self.ui.carta6.clicked.connect(lambda: self.seleccionarCarta(6, self.ui.carta6))
        #Conectar señales botones
        self.ui.botonJugar.clicked.connect(self.jugarCarta)
        self.show()

    def seleccionarCarta(self, numCarta, carta):
        if self.cartaSeleccionada != None:
            self.cartaSeleccionada.setStyleSheet("")
        self.cartaSeleccionada = carta
        self.numCartaSeleccionada = numCarta - 1
        self.cartaSeleccionada.setStyleSheet("border: 2px solid red;")
        self.ui.botonJugar.setEnabled(True)

    def jugarCarta(self):
        #Mostramos la carta jugada en el centro
        self.ui.carta_jugada1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[self.numCartaSeleccionada] + ".png").scaled(100,200))
        #Dejamos de seleccionar la carta
        self.cartaSeleccionada.setStyleSheet("")
        self.cartaSeleccionada.setPixmap(QtGui.QPixmap(":/cartas/cartas1/dorso.png"))
        self.cartaSeleccionada = None
        self.misCartas[self.numCartaSeleccionada] = 'dorso'

        for carta in self.misCartas:
            print(carta)
        #Desactivamos el botón de jugar
        self.ui.botonJugar.setEnabled(False)

    def rellenarMiMano(self):
        self.misCartas.sort(key= len)
        self.ui.carta1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[0] + ".png"))
        self.ui.carta2.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[1] + ".png"))
        self.ui.carta3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[2] + ".png"))
        self.ui.carta4.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[3] + ".png"))
        self.ui.carta5.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[4] + ".png"))
        self.ui.carta6.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + self.misCartas[5] + ".png"))


def main():
    app = QApplication(sys.argv)
    ventana = tablero_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
