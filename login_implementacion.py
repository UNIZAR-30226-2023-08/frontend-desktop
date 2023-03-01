import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Interfaces.login import  Ui_Login
from Interfaces.registro import Ui_Registro

class login_implementacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()


    def inicializarGUI(self):
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        self.ui.boton_login.clicked.connect(self.iniciar_sesion)
        self.ui.boton_registrarse.clicked.connect(self.cambioPantallaRegistro)
        self.show()

    def iniciar_sesion(self):
        nombre_usuario = self.ui.text_nombre_usuario.text().strip()
        contrasenya = self.ui.text_contrasenya.text().strip()
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Error")

        if not len(nombre_usuario) or not len(contrasenya):
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Todos los campos deben estar rellenados")
            mensaje.exec_()
        else:
            pass

    
    def cambioPantallaRegistro(self):
        self.ui = Ui_Registro()
        self.ui.setupUi(self)

        self.ui.boton_confirmar_registro.clicked.connect(self.registrarse)

    def registrarse(self):
        nombre_real = self.ui.text_nombre_real.text().strip()
        nombre_usuario = self.ui.text_nombre_usuario_registro.text().strip()
        correo_electronico = self.ui.text_correo.text().strip()
        contrasenya = self.ui.text_contrasenya_registro.text().strip()
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Error")

        if not len(nombre_real) or not len(nombre_usuario) \
            or not len(correo_electronico) or not len(contrasenya):
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Todos los campos deben estar rellenados")
            mensaje.exec_()
        elif self.ui.boton_terminos.checkState() == False:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Debe aceptar los términos de la aplicación")
            mensaje.exec_()
        else:
            pass



def main():
    app = QApplication(sys.argv)
    ventana = login_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()