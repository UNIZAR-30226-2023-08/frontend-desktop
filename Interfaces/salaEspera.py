# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salaEspera.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_salaEspera(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 497)
        MainWindow.setMinimumSize(QtCore.QSize(706, 497))
        MainWindow.setMaximumSize(QtCore.QSize(706, 497))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 711, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_5.setObjectName("widget_5")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 294, 39))
        self.label_2.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_7 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_7.setObjectName("widget_7")
        self.widget = QtWidgets.QWidget(self.widget_7)
        self.widget.setGeometry(QtCore.QRect(0, 10, 709, 331))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setMaximumSize(QtCore.QSize(10, 100))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(200, 360))
        self.widget_3.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Imagenes/cartas1/dorso.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setMaximumSize(QtCore.QSize(10, 100))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(231, 360))
        self.widget_2.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../Imagenes/cartas1/dorso.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setMaximumSize(QtCore.QSize(10, 100))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMaximumSize(QtCore.QSize(231, 360))
        self.widget_4.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget_4.setObjectName("widget_4")
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.label_17.setMinimumSize(QtCore.QSize(152, 315))
        self.label_17.setMaximumSize(QtCore.QSize(152, 315))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("../Imagenes/cartas1/dorso.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setMaximumSize(QtCore.QSize(10, 100))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMaximumSize(QtCore.QSize(231, 360))
        self.widget1.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget1.setObjectName("widget1")
        self.label_18 = QtWidgets.QLabel(self.widget1)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("../Imagenes/cartas1/dorso.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.widget1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setMaximumSize(QtCore.QSize(10, 100))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_6.setMaximumSize(QtCore.QSize(709, 75))
        self.widget_6.setObjectName("widget_6")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(20, 0, 141, 51))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setGeometry(QtCore.QRect(200, 0, 141, 51))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setGeometry(QtCore.QRect(370, 0, 141, 51))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        self.label_9.setGeometry(QtCore.QRect(550, 0, 141, 51))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.widget_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-125, -94, 841, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Imagenes/Tapete_verde.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guiñote"))
        self.label_2.setText(_translate("MainWindow", "Esperando jugadores..."))
        self.label_6.setText(_translate("MainWindow", "Jugador 1"))
        self.label_7.setText(_translate("MainWindow", "Jugador 2"))
        self.label_8.setText(_translate("MainWindow", "Jugador 3"))
        self.label_9.setText(_translate("MainWindow", "Jugador 4"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_salaEspera()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())