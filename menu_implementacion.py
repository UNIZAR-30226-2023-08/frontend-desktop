import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout
from Interfaces.menu_buscar_partida import Ui_menu_buscar_partida

class menu_implementacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()

    def inicializarGUI(self):
        #Crear un objeto QStackedWidget
        self.stacked_widget = QStackedWidget()

        #Crear los widgets que se desean agregar al QStacketWidget
        self.buscar_partida_widget = QWidget()
        self.ui_buscar_partida = Ui_menu_buscar_partida()
        self.ui_buscar_partida.setupUi(self.buscar_partida_widget)

        #Agrega los widgets al QstackedWidget
        self.stacked_widget.addWidget(self.buscar_partida_widget)

        # Crear un objeto QWidget que contendrá el QStackedWidget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Crear un objeto QVBoxLayout para el layout del QWidget
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        # Agregar el QStackedWidget al layout
        layout.addWidget(self.stacked_widget)
        
def main():
    app = QApplication(sys.argv)
    ventana = menu_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()