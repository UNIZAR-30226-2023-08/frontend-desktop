import sys
import requests
import subprocess

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QStyleFactory
from PyQt5.QtGui import QColor
from Interfaces.menu_buscar_partida import Ui_menu_buscar_partida
from Interfaces.menuInicial import Ui_menu_inicial
from Interfaces.estadisticas import Ui_estadisticas

class menu_implementacion(QMainWindow):
    def __init__(self, access_token, username) -> None:
        super().__init__()

        self.inicializarGUI()
        self.token = access_token
        self.username = username

    def inicializarGUI(self):
        #Crear un objeto QStackedWidget
        self.stacked_widget = QStackedWidget()

        #Crear los widgets que se desean agregar al QStacketWidget
        self.menu_inicial_widget = QWidget()
        self.ui_menu_inicial = Ui_menu_inicial()
        self.ui_menu_inicial.setupUi(self.menu_inicial_widget)

        self.buscar_partida_widget = QWidget()
        self.ui_buscar_partida = Ui_menu_buscar_partida()
        self.ui_buscar_partida.setupUi(self.buscar_partida_widget)

        self.estadisticas_widget = QWidget()
        self.ui_estadisticas = Ui_estadisticas()
        self.ui_estadisticas.setupUi(self.estadisticas_widget)

        #Agrega los widgets al QstackedWidget
        self.stacked_widget.addWidget(self.menu_inicial_widget)
        self.stacked_widget.addWidget(self.buscar_partida_widget)
        self.stacked_widget.addWidget(self.estadisticas_widget)

        # Crear un objeto QWidget que contendrá el QStackedWidget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Crear un objeto QVBoxLayout para el layout del QWidget
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        # Agregar el QStackedWidget al layout
        layout.addWidget(self.stacked_widget)

        #Conectar señales de los botones
        self.ui_menu_inicial.boton_jugar.clicked.connect(self.pantalla_buscar_partida)
        self.ui_menu_inicial.boton_estadisticas.clicked.connect(self.pantalla_estadisticas)
        self.ui_buscar_partida.boton_volver.clicked.connect(self.pantalla_inicial)
        self.ui_estadisticas.boton_volver.clicked.connect(self.pantalla_inicial)
        self.ui_buscar_partida.comboBox.currentIndexChanged.connect(self.seleccionar_tipo_partida)
        self.ui_buscar_partida.boton_buscar_publica.clicked.connect(self.buscar_partida_publica)
        self.ui_buscar_partida.boton_crear_privada.clicked.connect(self.crear_partida_privada)
        self.ui_buscar_partida.boton_ingresar_privada.clicked.connect(self.ingresar_partida_privada)
        self.ui_buscar_partida.boton_crear_torneo.clicked.connect(self.crear_torneo)
        self.ui_buscar_partida.boton_ingresar_torneo.clicked.connect(self.ingresar_torneo)

        #Inicializar estado botones
        self.activar_botones_menu(False)
        
        # Aplicar estilo Fusion
        style = QStyleFactory.create('Fusion')
        self.ui_estadisticas.listWidget.setStyle(style)

        self.ui_estadisticas.listWidget.setStyleSheet("""
        QListWidget {
            background-color: #F2F2F2;
            border: none;
            font-size: 14px;
        }
        QListWidget::item {
            padding: 5px 10px;
            border-bottom: 1px solid #CCCCCC;
        }
        QListWidget::item:hover {
            background-color: #E6E6E6;
        }
    """)

    def pantalla_buscar_partida(self):
        self.stacked_widget.setCurrentWidget(self.buscar_partida_widget)
    
    def pantalla_estadisticas(self):
        self.stacked_widget.setCurrentWidget(self.estadisticas_widget)
        self.rellenar_pantalla_estadisticas()

    def pantalla_inicial(self):
        self.stacked_widget.setCurrentWidget(self.menu_inicial_widget)
        self.ui_estadisticas.listWidget.clear()
        
    def rellenar_pantalla_estadisticas(self):
        self.rellenarEstadisticas()
        self.rellenarRanking()

    def rellenarEstadisticas(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        response = requests.get('http://guinote-unizar.onrender.com/users/me', headers=headers)
        response_parsed = response.json()
        nombre_usuario = response_parsed['username']
        victorias = int(response_parsed['wonMatches'])
        derrotas = int(response_parsed['lostMatches'])
        lp = response_parsed['lp']
        if victorias == 0 and derrotas == 0:
            ratio = "N/A"
        elif derrotas == 0:
            ratio = "100%"
        else:
            ratio = str((victorias/(victorias + derrotas) * 100).__round__(2)) + "%"
        
        self.ui_estadisticas.label_nombre.setText(nombre_usuario)
        self.ui_estadisticas.label_vicrotias_derrotas.setText(str(victorias) + "/" + str(derrotas))
        self.ui_estadisticas.label_porcentaje_victorias.setText(ratio)
        self.ui_estadisticas.label_puntos.setText(str(lp))

    def rellenarRanking(self):
        parametros = {'limite_lista': 10}
        headers = {'Authorization': f'Bearer ' + self.token}
        response = requests.get('http://guinote-unizar.onrender.com/ranking', headers=headers,params=parametros)
        response_parsed = response.json()

        ranking = response_parsed

        for jugador in ranking:
            self.ui_estadisticas.listWidget.addItem(f" Usuario: {jugador['username']}: {jugador['lp']} puntos  Victorias: {jugador['wonMatches']}  Derrotas: {jugador['lostMatches']}")

    def seleccionar_tipo_partida(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        if text == "Elige tipo de partida":
            self.activar_botones_menu(False)
        elif text == "Partida 2 jugadores":
            self.activar_botones_menu(True)
        elif text == "Partida 3 jugadores":
            self.activar_botones_menu(True)
            self.ui_buscar_partida.boton_crear_torneo.setEnabled(False)
            self.ui_buscar_partida.boton_ingresar_torneo.setEnabled(False)
        elif text == "Partida 4 jugadores":
            self.activar_botones_menu(True)
            self.ui_buscar_partida.boton_crear_torneo.setEnabled(False)
            self.ui_buscar_partida.boton_ingresar_torneo.setEnabled(False)
    
    def activar_botones_menu(self, activar):
        self.ui_buscar_partida.boton_buscar_publica.setEnabled(activar)
        self.ui_buscar_partida.boton_crear_privada.setEnabled(activar)
        self.ui_buscar_partida.boton_ingresar_privada.setEnabled(activar)
        self.ui_buscar_partida.boton_crear_torneo.setEnabled(activar)
        self.ui_buscar_partida.boton_ingresar_torneo.setEnabled(activar)

    def buscar_partida_publica(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        if text == "Partida 2 jugadores":
            subprocess.call(["python", "tablero2_implementacion.py", self.username, "publica", ""])
        elif text == "Partida 3 jugadores":
            subprocess.call(["python", "tablero3_implementacion.py", self.username, "publica", ""])
        elif text == "Partida 4 jugadores":
            subprocess.call(["python", "tablero4_implementacion.py", self.username, "publica", ""])

    def crear_partida_privada(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        if text == "Partida 2 jugadores":
            subprocess.call(["python", "tablero2_implementacion.py", self.username, "privada", "crear"])
        elif text == "Partida 3 jugadores":
            subprocess.call(["python", "tablero3_implementacion.py", self.username, "privada", "crear"])
        elif text == "Partida 4 jugadores":
            subprocess.call(["python", "tablero4_implementacion.py", self.username, "privada", "crear"])
            
    def ingresar_partida_privada(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        codigo = self.ui_buscar_partida.codigo_privada.text()
        if text == "Partida 2 jugadores":
            subprocess.call(["python", "tablero2_implementacion.py", self.username, "privada", codigo])
        elif text == "Partida 3 jugadores":
            subprocess.call(["python", "tablero3_implementacion.py", self.username, "privada", codigo])
        elif text == "Partida 4 jugadores":
            subprocess.call(["python", "tablero4_implementacion.py", self.username, "privada", codigo])

    def crear_torneo(self):
        pass
    def ingresar_torneo(self):
        pass

        
    # def pantalla_tienda(self):
        
def main():
    app = QApplication(sys.argv)
    token = sys.argv[1]
    username = sys.argv[2]
    ventana = menu_implementacion(token, username)
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()