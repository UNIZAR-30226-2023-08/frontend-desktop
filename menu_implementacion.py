import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QStyleFactory
from PyQt5.QtGui import QColor
from Interfaces.menu_buscar_partida import Ui_menu_buscar_partida
from Interfaces.menuInicial import Ui_menu_inicial
from Interfaces.estadisticas import Ui_estadisticas

class menu_implementacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

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

        self.ui_menu_inicial.boton_jugar.clicked.connect(self.pantalla_buscar_partida)
        self.ui_menu_inicial.boton_estadisticas.clicked.connect(self.pantalla_estadisticas)
        
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
        self.rellenarRanking()
        

    def rellenarRanking(self):
        ranking = [
            {'nombre': 'Jugador 1', 'puntos': 100},
            {'nombre': 'Jugador 2', 'puntos': 80},
            {'nombre': 'Jugador 3', 'puntos': 70},
            {'nombre': 'Jugador 4', 'puntos': 50},
            {'nombre': 'Jugador 1', 'puntos': 100},
            {'nombre': 'Jugador 2', 'puntos': 80},
            {'nombre': 'Jugador 3', 'puntos': 70},
            {'nombre': 'Jugador 4', 'puntos': 50},
            {'nombre': 'Jugador 1', 'puntos': 100},
            {'nombre': 'Jugador 2', 'puntos': 80},
            {'nombre': 'Jugador 3', 'puntos': 70},
            {'nombre': 'Jugador 4', 'puntos': 50},
            {'nombre': 'Jugador 1', 'puntos': 100},
            {'nombre': 'Jugador 2', 'puntos': 80},
            {'nombre': 'Jugador 3', 'puntos': 70},
            {'nombre': 'Jugador 4', 'puntos': 50},
            {'nombre': 'Jugador 1', 'puntos': 100},
            {'nombre': 'Jugador 2', 'puntos': 80},
            {'nombre': 'Jugador 3', 'puntos': 70},
            {'nombre': 'Jugador 4', 'puntos': 50},
        ]

        for jugador in ranking:
            self.ui_estadisticas.listWidget.addItem(f"  {jugador['nombre']}: {jugador['puntos']} puntos")

    # def pantalla_tienda(self):
        
def main():
    app = QApplication(sys.argv)
    ventana = menu_implementacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()