import sys
import requests
import subprocess

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QStyleFactory
from Interfaces.menu_buscar_partida import Ui_menu_buscar_partida
from Interfaces.menuInicial import Ui_menu_inicial
from Interfaces.estadisticas import Ui_estadisticas
from Interfaces.tienda import Ui_Tienda

class menu_implementacion(QMainWindow):
    def __init__(self, access_token, username) -> None:
        super().__init__()

        self.token = access_token
        self.username = username
        self.baraja = "default"
        self.inicializarGUI()

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

        self.tienda_widget = QWidget()
        self.ui_tienda = Ui_Tienda()
        self.ui_tienda.setupUi(self.tienda_widget)

        #Agrega los widgets al QstackedWidget
        self.stacked_widget.addWidget(self.menu_inicial_widget)
        self.stacked_widget.addWidget(self.buscar_partida_widget)
        self.stacked_widget.addWidget(self.estadisticas_widget)
        self.stacked_widget.addWidget(self.tienda_widget)

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
        self.ui_menu_inicial.boton_tienda.clicked.connect(self.pantalla_tienda)
        self.ui_buscar_partida.boton_volver.clicked.connect(self.pantalla_inicial)
        self.ui_estadisticas.boton_volver.clicked.connect(self.pantalla_inicial)
        self.ui_tienda.boton_volver.clicked.connect(self.pantalla_inicial)
        self.ui_buscar_partida.comboBox.currentIndexChanged.connect(self.seleccionar_tipo_partida)
        self.ui_buscar_partida.boton_buscar_publica.clicked.connect(self.buscar_partida_publica)
        self.ui_buscar_partida.boton_crear_privada.clicked.connect(self.crear_partida_privada)
        self.ui_buscar_partida.boton_ingresar_privada.clicked.connect(self.ingresar_partida_privada)
        self.ui_buscar_partida.boton_crear_torneo.clicked.connect(self.crear_torneo)
        self.ui_buscar_partida.boton_ingresar_torneo.clicked.connect(self.ingresar_torneo)
        self.ui_buscar_partida.boton_ia.clicked.connect(self.buscar_partida_ia)
        self.ui_tienda.comprar2.clicked.connect(self.comprar_baraja2)
        self.ui_tienda.comprar3.clicked.connect(self.comprar_baraja3)
        self.ui_tienda.comprar4.clicked.connect(self.comprar_baraja4)
        self.ui_tienda.equipar1.clicked.connect(self.equipar_baraja1)
        self.ui_tienda.equipar2.clicked.connect(self.equipar_baraja2)
        self.ui_tienda.equipar3.clicked.connect(self.equipar_baraja3)
        self.ui_tienda.equipar4.clicked.connect(self.equipar_baraja4)

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

    def pantalla_tienda(self):
        self.stacked_widget.setCurrentWidget(self.tienda_widget)
        self.inicializar_botones_tienda()

    def pantalla_inicial(self):
        self.stacked_widget.setCurrentWidget(self.menu_inicial_widget)
        self.ui_estadisticas.listWidget.clear()
        
    def rellenar_pantalla_estadisticas(self):
        self.rellenarEstadisticas()
        self.rellenarRanking()

    def rellenarEstadisticas(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        response = requests.get('https://guinote-unizar.onrender.com/users/me', headers=headers)
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
        response = requests.get('https://guinote-unizar.onrender.com/ranking', headers=headers,params=parametros)
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
            self.ui_buscar_partida.boton_ia.setEnabled(False)
        elif text == "Partida 3 jugadores":
            self.activar_botones_menu(True)
            self.ui_buscar_partida.boton_crear_torneo.setEnabled(False)
            self.ui_buscar_partida.boton_ingresar_torneo.setEnabled(False)
            self.ui_buscar_partida.boton_ia.setEnabled(False)
        elif text == "Partida 4 jugadores":
            self.activar_botones_menu(True)
            self.ui_buscar_partida.boton_crear_torneo.setEnabled(False)
            self.ui_buscar_partida.boton_ingresar_torneo.setEnabled(False)
            self.ui_buscar_partida.boton_ia.setEnabled(True)
    
    def activar_botones_menu(self, activar):
        self.ui_buscar_partida.boton_ia.setEnabled(activar)
        self.ui_buscar_partida.boton_buscar_publica.setEnabled(activar)
        self.ui_buscar_partida.boton_crear_privada.setEnabled(activar)
        self.ui_buscar_partida.boton_ingresar_privada.setEnabled(activar)
        self.ui_buscar_partida.boton_crear_torneo.setEnabled(activar)
        self.ui_buscar_partida.boton_ingresar_torneo.setEnabled(activar)

    def buscar_partida_publica(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        if text == "Partida 2 jugadores":
            subprocess.call(["python", "tablero2_implementacion.py", self.username, "publica", "", self.baraja])
        elif text == "Partida 3 jugadores":
            subprocess.call(["python", "tablero3_implementacion.py", self.username, "publica", "", self.baraja])
        elif text == "Partida 4 jugadores":
            subprocess.call(["python", "tablero4_implementacion.py", self.username, "publica", "", self.baraja])

    def crear_partida_privada(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        if text == "Partida 2 jugadores":
            subprocess.call(["python", "tablero2_implementacion.py", self.username, "privada", "crear", self.baraja])
        elif text == "Partida 3 jugadores":
            subprocess.call(["python", "tablero3_implementacion.py", self.username, "privada", "crear", self.baraja])
        elif text == "Partida 4 jugadores":
            subprocess.call(["python", "tablero4_implementacion.py", self.username, "privada", "crear", self.baraja])
            
    def ingresar_partida_privada(self):
        text = self.ui_buscar_partida.comboBox.currentText()
        codigo = self.ui_buscar_partida.codigo_privada.text()
        if text == "Partida 2 jugadores":
            subprocess.call(["python", "tablero2_implementacion.py", self.username, "privada", codigo, self.baraja])
        elif text == "Partida 3 jugadores":
            subprocess.call(["python", "tablero3_implementacion.py", self.username, "privada", codigo, self.baraja])
        elif text == "Partida 4 jugadores":
            subprocess.call(["python", "tablero4_implementacion.py", self.username, "privada", codigo, self.baraja])

    def buscar_partida_ia(self):
        subprocess.call(["python", "tablero4_implementacion.py", self.username, "ia", "", self.baraja])

    def inicializar_botones_tienda(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        response = requests.get('https://guinote-unizar.onrender.com/users/me', headers=headers)
        response_parsed = response.json()
        monedas = str(response_parsed['coins'])
        self.ui_tienda.label_monedas.setText(monedas)

        parametros = {'username': self.username}
        response2 = requests.get('https://guinote-unizar.onrender.com/tienda/barajas', headers=headers, params=parametros)
        response_parsed2 = response2.json()
        baraja2 = response_parsed2[1][1]
        baraja3 = response_parsed2[2][1]
        baraja4 = response_parsed2[3][1]
        self.botones_comprar(baraja2, baraja3, baraja4)

    def botones_comprar(self, baraja2, baraja3, baraja4):
        self.ui_tienda.equipar1.setEnabled(True)
        self.ui_tienda.equipar1.setText("Equipar")
        if baraja2 == 0:
            self.ui_tienda.comprar2.setEnabled(True)
            self.ui_tienda.comprar2.setText("Comprar(30)")
        else:
            self.ui_tienda.comprar2.setEnabled(False)
            self.ui_tienda.comprar2.setText("Comprado")
            self.ui_tienda.equipar2.setEnabled(True)
            self.ui_tienda.equipar2.setText("Equipar")

        if baraja3 == 0:
            self.ui_tienda.comprar3.setEnabled(True)
            self.ui_tienda.comprar3.setText("Comprar(30)")
        else:
            self.ui_tienda.comprar3.setEnabled(False)
            self.ui_tienda.comprar3.setText("Comprado")
            self.ui_tienda.equipar3.setEnabled(True)
            self.ui_tienda.equipar3.setText("Equipar")

        if baraja4 == 0:
            self.ui_tienda.comprar4.setEnabled(True)
            self.ui_tienda.comprar4.setText("Comprar(30)")
        else:
            self.ui_tienda.comprar4.setEnabled(False)
            self.ui_tienda.comprar4.setText("Comprado")
            self.ui_tienda.equipar4.setEnabled(True)
            self.ui_tienda.equipar4.setText("Equipar")

        if self.baraja == "default":
            self.ui_tienda.equipar1.setEnabled(False)
            self.ui_tienda.equipar1.setText("Equipado")
        elif self.baraja == "noir":
            self.ui_tienda.equipar2.setEnabled(False)
            self.ui_tienda.equipar2.setText("Equipado")
        elif self.baraja == "classic":
            self.ui_tienda.equipar3.setEnabled(False)
            self.ui_tienda.equipar3.setText("Equipado")
        else:
            self.ui_tienda.equipar4.setEnabled(False)
            self.ui_tienda.equipar4.setText("Equipado")

    def comprar_baraja2(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        parametros = {'username': self.username, 'baraja': 'noir'}
        response = requests.get('https://guinote-unizar.onrender.com/tienda/barajas/comprar', headers=headers, params=parametros)
        response_js = response.json()
        print(response_js)
        self.inicializar_botones_tienda()

    def comprar_baraja3(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        parametros = {'username': self.username, 'baraja': "classic"}
        requests.get('https://guinote-unizar.onrender.com/tienda/barajas/comprar', headers=headers, params=parametros)
        self.inicializar_botones_tienda()

    def comprar_baraja4(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        parametros = {'username': self.username, 'baraja': "classic-noir"}
        requests.get('https://guinote-unizar.onrender.com/tienda/barajas/comprar', headers=headers, params=parametros)
        self.inicializar_botones_tienda()

    def equipar_baraja1(self):
        self.baraja = "default"
        self.inicializar_botones_tienda()

    def equipar_baraja2(self):
        self.baraja = "noir"
        self.inicializar_botones_tienda()

    def equipar_baraja3(self):
        self.baraja = "classic"
        self.inicializar_botones_tienda()

    def equipar_baraja4(self):
        self.baraja = "classic-noir"
        self.inicializar_botones_tienda()


    def crear_torneo(self):
        pass
    def ingresar_torneo(self):
        pass

        
def main(): 
    app = QApplication(sys.argv)
    token = sys.argv[1]
    username = sys.argv[2]
    ventana = menu_implementacion(token, username)
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()