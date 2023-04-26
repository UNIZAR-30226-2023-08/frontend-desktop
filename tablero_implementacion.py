import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui
from Interfaces.tablero import  Ui_Tablero
from Interfaces.clickableLabel import ClickableLabel
from Controlador.controlador import Controlador
from Modelo.modelo import modelo_tablero

class tablero_implementacion(QMainWindow):
    numCartaSeleccionada = -1
    cartaSeleccionada = None

    def __init__(self, username) -> None:
        super().__init__()
        modelo = modelo_tablero()
        self.controlador = Controlador(modelo, self, username)
        self.inicializarGUI()
    
    def inicializarGUI(self):
        self.ui = Ui_Tablero()
        self.ui.setupUi(self)

        #Conectar señales cartas
        #self.rellenarMiMano()
        #self.mostrarTriunfo()
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
        #self.ui.carta_jugada1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.misCartas[self.numCartaSeleccionada] + ".png").scaled(100,200))
        #Dejamos de seleccionar la carta
        #self.cartaSeleccionada.setStyleSheet("")
        #self.cartaSeleccionada.setPixmap(QtGui.QPixmap(":/cartas/cartas1/dorso.png"))
        #self.cartaSeleccionada = None
        #self.misCartas[self.numCartaSeleccionada] = 'dorso'

        #Desactivamos el botón de jugar
        self.controlador.jugar_carta(self.numCartaSeleccionada)
        self.ui.botonJugar.setEnabled(False)

    def rellenarMiMano(self, modelo: modelo_tablero):
        self.ui.carta1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[0] + ".png"))
        self.ui.carta2.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[1] + ".png"))
        self.ui.carta3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[2] + ".png"))
        self.ui.carta4.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[3] + ".png"))
        self.ui.carta5.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[4] + ".png"))
        self.ui.carta6.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[5] + ".png"))

    def mostrarTriunfo(self, modelo: modelo_tablero):
        pm = QtGui.QPixmap(":/cartas/cartas1/" + modelo.carta_triunfo + ".png")
        t = QtGui.QTransform()
        t.rotate(-90)
        self.ui.carta_triunfo.setPixmap(pm.transformed(t))

def main():
    username = sys.argv[1]
    app = QApplication(sys.argv)
    ventana = tablero_implementacion(username)
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
