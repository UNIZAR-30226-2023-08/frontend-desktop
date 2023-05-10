import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout
from PyQt5 import QtGui, QtCore
from Interfaces.tablero4 import Ui_tablero4
from Interfaces.salaEspera4 import Ui_sala_espera4
from Interfaces.clickableLabel import ClickableLabel
from Controlador.controlador import Controlador
from Modelo.modelo import modelo_tablero

class tablero_implementacion(QMainWindow):
    numCartaSeleccionada = -1
    cartaSeleccionada = None
    num_cartas_posibles = []

    def __init__(self, username) -> None:
        super().__init__()
        self.username = username
        modelo = modelo_tablero()
        self.inicializarGUI()
        self.controlador = Controlador(modelo, self, username)
        
    
    def inicializarGUI(self):
        #Crear un objeto QStackedWidget
        self.stacked_widget = QStackedWidget()

        #Crear los widgets que se desean agregar al QStacketWidget
        self.sala_espera_widget = QWidget()
        self.ui_sala_espera = Ui_sala_espera4()
        self.ui_sala_espera.setupUi(self.sala_espera_widget)
        

        self.tablero_widget = QWidget()
        self.ui_tablero = Ui_tablero4()
        self.ui_tablero.setupUi(self.tablero_widget)

        #Agrega los widgets al QstackedWidget
        self.stacked_widget.addWidget(self.sala_espera_widget)
        self.stacked_widget.addWidget(self.tablero_widget)

        # Crear un objeto QWidget que contendrá el QStackedWidget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Crear un objeto QVBoxLayout para el layout del QWidget
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        # Agregar el QStackedWidget al layout
        layout.addWidget(self.stacked_widget)

        #Conectar señales botones
        self.ui_tablero.botonJugar.clicked.connect(self.jugarCarta)
        self.ui_tablero.boton_enviar_chat.clicked.connect(self.enviar_mensaje)
        #Conectar señales cartas
        self.ui_tablero.carta1.clicked.connect(lambda: self.seleccionarCarta(1, self.ui_tablero.carta1))
        self.ui_tablero.carta2.clicked.connect(lambda: self.seleccionarCarta(2, self.ui_tablero.carta2))
        self.ui_tablero.carta3.clicked.connect(lambda: self.seleccionarCarta(3, self.ui_tablero.carta3))
        self.ui_tablero.carta4.clicked.connect(lambda: self.seleccionarCarta(4, self.ui_tablero.carta4))
        self.ui_tablero.carta5.clicked.connect(lambda: self.seleccionarCarta(5, self.ui_tablero.carta5))
        self.ui_tablero.carta6.clicked.connect(lambda: self.seleccionarCarta(6, self.ui_tablero.carta6))

        

    def mostrar_jugadores_sala_espera(self, modelo: modelo_tablero):
        self.ui_sala_espera.j1_label.setText(modelo.jugador0)
        self.ui_sala_espera.dorso1_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/oro-1.png"))
        if modelo.jugador1 != "Jugador 2":
            self.ui_sala_espera.j2_label.setText(modelo.jugador1)
            self.ui_sala_espera.dorso2_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/copa-1.png"))

    def pantalla_tablero(self):
        print("X")
        QtCore.QMetaObject.invokeMethod(self.stacked_widget, "setCurrentWidget", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(QWidget, self.tablero_widget))
        print("XX")
        
        #self.rellenarMiMano()
        #self.mostrarTriunfo()
        

    def seleccionarCarta(self, numCarta, carta):
        if self.cartaSeleccionada != None:
            self.cartaSeleccionada.setStyleSheet("")
        self.cartaSeleccionada = carta
        self.numCartaSeleccionada = numCarta - 1
        self.cartaSeleccionada.setStyleSheet("border: 2px solid red;")
        if self.jugada_posible:
            self.ui_tablero.botonJugar.setEnabled(True)

    def puede_jugar(self, puede, num_cartas_posibles):
        if puede:
            self.jugada_posible = True
        else:
            self.jugada_posible = False
            self.ui_tablero.botonJugar.setEnabled(False)

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
            self.ui_tablero.carta_jugada1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[0] + ".png").scaled(100,200))
            self.ui_tablero.carta_jugada3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[1] + ".png").scaled(100,200))
        else:
            self.ui_tablero.carta_jugada1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[1] + ".png").scaled(100,200))
            self.ui_tablero.carta_jugada3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.cartas_jugadas[0] + ".png").scaled(100,200))

    def rellenarMiMano(self, modelo: modelo_tablero):
        self.ui_tablero.carta1.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[0] + ".png"))
        self.ui_tablero.carta2.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[1] + ".png"))
        self.ui_tablero.carta3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[2] + ".png"))
        self.ui_tablero.carta4.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[3] + ".png"))
        self.ui_tablero.carta5.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[4] + ".png"))
        self.ui_tablero.carta6.setPixmap(QtGui.QPixmap(":/cartas/cartas1/" + modelo.mis_cartas[5] + ".png"))

    def mostrarTriunfo(self, modelo: modelo_tablero):
        pm = QtGui.QPixmap(":/cartas/cartas1/" + modelo.carta_triunfo + ".png")
        t = QtGui.QTransform()
        t.rotate(-90)
        self.ui_tablero.carta_triunfo.setPixmap(pm.transformed(t))






    def enviar_mensaje(self):
        mensaje = self.ui_tablero.text_chat.text()
        self.ui_tablero.text_chat.clear()
        self.ui_tablero.chat_box.append(self.username + ": " + mensaje)

def main():
    username = sys.argv[1]
    app = QApplication(sys.argv)
    ventana = tablero_implementacion(username)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
