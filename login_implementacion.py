import sys
import requests
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout
from Interfaces.login import Ui_login
from Interfaces.registro import Ui_registro

class login_implementacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.inicializarGUI()
        self.rutaPeticiones = 'http://localhost:8000'


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
            params = {'username': nombre_usuario, 
                      'password': contrasenya}
            #params_parseados = json.dumps(params)
            response = requests.post(self.rutaPeticiones + '/token', data=params)
            response_parsed = response.json()

            if response.status_code == 401:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText(response_parsed["detail"])
                mensaje.exec_()

            elif response.status_code == 200:
                mensaje.setText("Loggeado")
                mensaje.exec_()
                
    
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
            params = {'username': nombre_usuario, 
                      'email': correo_electronico, 
                      'real_name': nombre_real, 
                      'hashed_password': contrasenya}
            params_parsed = json.dumps(params)
            response = requests.post(self.rutaPeticiones + '/register', data=params_parsed)
            response_parsed = response.json()

            if response.status_code == 200:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText("Registro realizado correctamente")
                mensaje.exec_()
                self.stacked_widget.setCurrentWidget(self.login_widget)
            
            elif response.status_code == 400:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText("Nobre de usuario en uso")
                mensaje.exec_()



def main():
    app = QApplication(sys.argv)
    ventana = login_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()