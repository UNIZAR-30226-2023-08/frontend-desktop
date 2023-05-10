import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout
from Interfaces.login import Ui_login
from Interfaces.registro import Ui_registro

class login_implementacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()


    def inicializarGUI(self):
        #Crear un objeto QStackedWidget
        self.stacked_widget = QStackedWidget()

        #Crear los widgets que se desean agregar al QStacketWidget
        self.login_widget = QWidget()
        self.ui_login = Ui_login()
        self.ui_login.setupUi(self.login_widget)
        

        self.registro_widget = QWidget()
        self.ui_registro = Ui_registro()
        self.ui_registro.setupUi(self.registro_widget)

        #Agrega los widgets al QstackedWidget
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.registro_widget)

        # Crear un objeto QWidget que contendrá el QStackedWidget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Crear un objeto QVBoxLayout para el layout del QWidget
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        # Agregar el QStackedWidget al layout
        layout.addWidget(self.stacked_widget)

        #Conectar botones login
        self.ui_login.boton_login.clicked.connect(self.iniciar_sesion)
        self.ui_login.boton_registrarse.clicked.connect(self.cambioPantallaRegistro)

        #Conectar botones registro
        self.ui_registro.boton_confirmar_registro.clicked.connect(self.registrarse)
        """
        elf.ui = Ui_Login()
        self.ui.setupUi(self)
        
        
        self.show()
        """
    def iniciar_sesion(self):
        nombre_usuario = self.ui_login.text_nombre_usuario.text().strip()
        contrasenya = self.ui_login.text_contrasenya.text().strip()
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Error")

        if not len(nombre_usuario) or not len(contrasenya):
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Todos los campos deben estar rellenados")
            mensaje.exec_()
        else:
            pass

    
    def cambioPantallaRegistro(self):
        self.stacked_widget.setCurrentWidget(self.registro_widget)

        

    def registrarse(self):
        nombre_real = self.ui_registro.text_nombre_real.text().strip()
        nombre_usuario = self.ui_registro.text_nombre_usuario_registro.text().strip()
        correo_electronico = self.ui_registro.text_correo.text().strip()
        contrasenya = self.ui_registro.text_contrasenya_registro.text().strip()
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Error")

        if not len(nombre_real) or not len(nombre_usuario) \
            or not len(correo_electronico) or not len(contrasenya):
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText("Todos los campos deben estar rellenados")
            mensaje.exec_()
        elif self.ui_registro.boton_terminos.checkState() == False:
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