import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Interfaces.tablero import  Ui_Tablero
from Interfaces.clickableLabel import ClickableLabel

class tablero_implementacion(QMainWindow):
    numCartaSeleccionada = 0
    cartaSeleccionada = None

    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()
    
    def inicializarGUI(self):
        self.ui = Ui_Tablero()
        self.ui.setupUi(self)

        self.ui.carta1.clicked.connect(lambda: self.seleccionarCarta(1, self.ui.carta1))
        self.ui.carta2.clicked.connect(lambda: self.seleccionarCarta(2, self.ui.carta2))
        self.ui.carta3.clicked.connect(lambda: self.seleccionarCarta(3, self.ui.carta3))
        self.ui.carta4.clicked.connect(lambda: self.seleccionarCarta(4, self.ui.carta4))
        self.ui.carta5.clicked.connect(lambda: self.seleccionarCarta(5, self.ui.carta5))
        self.ui.carta6.clicked.connect(lambda: self.seleccionarCarta(6, self.ui.carta6))
        self.show()

    def seleccionarCarta(self, numCarta, carta):
        if self.cartaSeleccionada != None:
            self.cartaSeleccionada.setStyleSheet("")
        self.cartaSeleccionada = carta
        self.numCartaSeleccionada = numCarta
        self.cartaSeleccionada.setStyleSheet("border: 2px solid red;")
        

def main():
    app = QApplication(sys.argv)
    ventana = tablero_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
