# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salaEspera3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sala_espera3(object):
    def setupUi(self, sala_espera3):
        sala_espera3.setObjectName("sala_espera3")
        sala_espera3.setEnabled(True)
        sala_espera3.resize(706, 497)
        self.label = QtWidgets.QLabel(sala_espera3)
        self.label.setGeometry(QtCore.QRect(0, 0, 706, 497))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/Tapete_verde.jpg"))
        self.label.setObjectName("label")
        self.EspJugLabel_3 = QtWidgets.QLabel(sala_espera3)
        self.EspJugLabel_3.setGeometry(QtCore.QRect(210, 20, 294, 39))
        self.EspJugLabel_3.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.EspJugLabel_3.setFont(font)
        self.EspJugLabel_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.EspJugLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.EspJugLabel_3.setObjectName("EspJugLabel_3")
        self.widget_15 = QtWidgets.QWidget(sala_espera3)
        self.widget_15.setGeometry(QtCore.QRect(0, 80, 709, 342))
        self.widget_15.setObjectName("widget_15")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_15)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, -10, 709, 331))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_21.setMaximumSize(QtCore.QSize(10, 100))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_4.addWidget(self.label_21)
        self.widget_16 = QtWidgets.QWidget(self.layoutWidget_3)
        self.widget_16.setMaximumSize(QtCore.QSize(152, 315))
        self.widget_16.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget_16.setObjectName("widget_16")
        self.dorso1_label = QtWidgets.QLabel(self.widget_16)
        self.dorso1_label.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.dorso1_label.setAutoFillBackground(False)
        self.dorso1_label.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.dorso1_label.setText("")
        self.dorso1_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/dorso.png"))
        self.dorso1_label.setScaledContents(True)
        self.dorso1_label.setObjectName("dorso1_label")
        self.horizontalLayout_4.addWidget(self.widget_16)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_22.setMaximumSize(QtCore.QSize(10, 100))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.widget_17 = QtWidgets.QWidget(self.layoutWidget_3)
        self.widget_17.setEnabled(True)
        self.widget_17.setMaximumSize(QtCore.QSize(152, 315))
        self.widget_17.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget_17.setObjectName("widget_17")
        self.dorso2_label = QtWidgets.QLabel(self.widget_17)
        self.dorso2_label.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.dorso2_label.setAutoFillBackground(False)
        self.dorso2_label.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.dorso2_label.setText("")
        self.dorso2_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/dorso.png"))
        self.dorso2_label.setScaledContents(True)
        self.dorso2_label.setObjectName("dorso2_label")
        self.horizontalLayout_4.addWidget(self.widget_17)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setMaximumSize(QtCore.QSize(10, 100))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_4.addWidget(self.label_23)
        self.widget_18 = QtWidgets.QWidget(self.layoutWidget_3)
        self.widget_18.setMaximumSize(QtCore.QSize(152, 315))
        self.widget_18.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.widget_18.setObjectName("widget_18")
        self.dorso3_label = QtWidgets.QLabel(self.widget_18)
        self.dorso3_label.setGeometry(QtCore.QRect(0, 0, 152, 315))
        self.dorso3_label.setMinimumSize(QtCore.QSize(152, 315))
        self.dorso3_label.setMaximumSize(QtCore.QSize(152, 315))
        self.dorso3_label.setAutoFillBackground(False)
        self.dorso3_label.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.dorso3_label.setText("")
        self.dorso3_label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/dorso.png"))
        self.dorso3_label.setScaledContents(True)
        self.dorso3_label.setObjectName("dorso3_label")
        self.horizontalLayout_4.addWidget(self.widget_18)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_25.setMaximumSize(QtCore.QSize(10, 100))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_4.addWidget(self.label_25)
        self.widget_19 = QtWidgets.QWidget(sala_espera3)
        self.widget_19.setGeometry(QtCore.QRect(0, 425, 709, 75))
        self.widget_19.setMaximumSize(QtCore.QSize(709, 75))
        self.widget_19.setObjectName("widget_19")
        self.j1_label = QtWidgets.QLabel(self.widget_19)
        self.j1_label.setGeometry(QtCore.QRect(60, 0, 141, 51))
        self.j1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.j1_label.setObjectName("j1_label")
        self.j2_label = QtWidgets.QLabel(self.widget_19)
        self.j2_label.setGeometry(QtCore.QRect(280, 0, 141, 51))
        self.j2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.j2_label.setObjectName("j2_label")
        self.j3_label = QtWidgets.QLabel(self.widget_19)
        self.j3_label.setGeometry(QtCore.QRect(500, 0, 141, 51))
        self.j3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.j3_label.setObjectName("j3_label")

        self.retranslateUi(sala_espera3)
        QtCore.QMetaObject.connectSlotsByName(sala_espera3)

    def retranslateUi(self, sala_espera3):
        _translate = QtCore.QCoreApplication.translate
        sala_espera3.setWindowTitle(_translate("sala_espera3", "Form"))
        self.EspJugLabel_3.setText(_translate("sala_espera3", "Esperando jugadores..."))
        self.j1_label.setText(_translate("sala_espera3", "Jugador 1"))
        self.j2_label.setText(_translate("sala_espera3", "Jugador 2"))
        self.j3_label.setText(_translate("sala_espera3", "Jugador 3"))
import Imagenes.imagenes_rc
