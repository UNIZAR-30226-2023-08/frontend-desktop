import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class menu_implementacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()

    def inicializarGUI(self):
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        self.ui.boton_login.clicked.connect(self.iniciar_sesion)
        self.ui.boton_registrarse.clicked.connect(self.cambioPantallaRegistro)
        self.show()
        
def main():
    app = QApplication(sys.argv)
    ventana = menu_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()