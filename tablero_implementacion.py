import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui
from Interfaces.tablero import  Ui_Tablero
from Interfaces.salaEspera import  Ui_salaEspera
from Interfaces.clickableLabel import ClickableLabel
from Controlador.controlador import Controlador
from Modelo.modelo import modelo_tablero

class tablero_implementacion(QMainWindow):
    numCartaSeleccionada = -1
    cartaSeleccionada = None
    num_cartas_posibles = []

    def __init__(self, username) -> None:
        super().__init__()
        modelo = modelo_tablero()
        self.controlador = Controlador(modelo, self, username)
        self.inicializarGUI()
    
    def inicializarGUI(self):
        self.ui = Ui_salaEspera()
        self.ui.setupUi(self)

    def mostrar_jugadores_sala_espera(self, modelo: modelo_tablero):
        self.ui.j1_label.setText(modelo.jugador0)
        self.ui.dorso1_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/oro-1.png"))
        if modelo.jugador1 != "Jugador 2":
            self.ui.j2_label.setText(modelo.jugador1)
            self.ui.dorso2_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/copa-1.png"))


    def pantallaTablero(self):
        print("a")
        self.ui = Ui_Tablero()
        print("b")
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

    def seleccionarCarta(self, numCarta, carta):
        if self.cartaSeleccionada != None:
            self.cartaSeleccionada.setStyleSheet("")
        self.cartaSeleccionada = carta
        self.numCartaSeleccionada = numCarta - 1
        self.cartaSeleccionada.setStyleSheet("border: 2px solid red;")
        if self.jugada_posible:
            self.ui.botonJugar.setEnabled(True)

    def puede_jugar(self, puede, num_cartas_posibles):
        if puede:
            self.jugada_posible = True
        else:
            self.jugada_posible = False
            self.ui.botonJugar.setEnabled(False)

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

    def mostrar_cartas_jugadas(self, modelo: modelo_tablero, jugador):
        if jugador == 0:
            self.ui.carta_jugada1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[0] + ".png").scaled(100,200))
            self.ui.carta_jugada3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[1] + ".png").scaled(100,200))
        else:
            self.ui.carta_jugada1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[1] + ".png").scaled(100,200))
            self.ui.carta_jugada3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[0] + ".png").scaled(100,200))

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
