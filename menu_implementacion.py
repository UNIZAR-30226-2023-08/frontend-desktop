import sys
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QStyleFactory
from PyQt5.QtGui import QColor
from Interfaces.menu_buscar_partida import Ui_menu_buscar_partida
from Interfaces.menuInicial import Ui_menu_inicial
from Interfaces.estadisticas import Ui_estadisticas

class menu_implementacion(QMainWindow):
    def __init__(self, access_token) -> None:
        super().__init__()

        self.inicializarGUI()
        self.token = access_token

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
        
    def rellenar_pantalla_estadisticas(self):
        self.rellenarEstadisticas()
        self.rellenarRanking()

    def rellenarEstadisticas(self):
        headers = {'Authorization': f'Bearer ' + self.token}
        response = requests.get('http://localhost:8000/users/me', headers=headers)
        response_parsed = response.json()
        nombre_usuario = response_parsed['username']
        victorias = int(response_parsed['winMatches'])
        derrotas = int(response_parsed['looseMatches'])
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
        response = requests.get('http://localhost:8000/ranking', headers=headers,params=parametros)
        response_parsed = response.json()

        ranking = response_parsed

        for jugador in ranking:
            self.ui_estadisticas.listWidget.addItem(f" Usuario: {jugador['username']}: {jugador['lp']} puntos  Victorias: {jugador['winMatches']}  Derrotas: {jugador['looseMatches']}")

        
    # def pantalla_tienda(self):
        
def main():
    app = QApplication(sys.argv)
    ventana = menu_implementacion(sys.argv[1])
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()