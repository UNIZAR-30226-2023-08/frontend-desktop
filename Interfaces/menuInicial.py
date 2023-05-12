# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuInicial.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_inicial(object):
    def setupUi(self, menu_inicial):
        menu_inicial.setObjectName("menu_inicial")
        menu_inicial.resize(706, 497)
        self.label = QtWidgets.QLabel(menu_inicial)
        self.label.setGeometry(QtCore.QRect(0, 0, 706, 497))
        self.label.setStyleSheet("border-color: rgb(224, 27, 36);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/Tapete_verde.jpg"))
        self.label.setObjectName("label")
        self.dorso = QtWidgets.QLabel(menu_inicial)
        self.dorso.setGeometry(QtCore.QRect(60, 80, 181, 315))
        self.dorso.setAutoFillBackground(False)
        self.dorso.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.dorso.setText("")
        self.dorso.setPixmap(QtGui.QPixmap(":/cartas/cartas1/oro-1.png"))
        self.dorso.setScaledContents(True)
        self.dorso.setObjectName("dorso")
        self.LabelGuiote = QtWidgets.QLabel(menu_inicial)
        self.LabelGuiote.setGeometry(QtCore.QRect(320, 90, 294, 39))
        self.LabelGuiote.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.LabelGuiote.setFont(font)
        self.LabelGuiote.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LabelGuiote.setStyleSheet("background-color: rgb(255, 204, 0);\n"
"border-color: rgb(224, 27, 36);\n"
"font: 75 italic 26pt \"Sans\";\n"
"")
        self.LabelGuiote.setLineWidth(9)
        self.LabelGuiote.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelGuiote.setObjectName("LabelGuiote")
        self.boton_jugar = QtWidgets.QPushButton(menu_inicial)
        self.boton_jugar.setGeometry(QtCore.QRect(390, 170, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_jugar.setFont(font)
        self.boton_jugar.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_jugar.setObjectName("boton_jugar")
        self.boton_estadisticas = QtWidgets.QPushButton(menu_inicial)
        self.boton_estadisticas.setGeometry(QtCore.QRect(390, 250, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_estadisticas.setFont(font)
        self.boton_estadisticas.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_estadisticas.setObjectName("boton_estadisticas")
        self.boton_tienda = QtWidgets.QPushButton(menu_inicial)
        self.boton_tienda.setGeometry(QtCore.QRect(390, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_tienda.setFont(font)
        self.boton_tienda.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_tienda.setObjectName("boton_tienda")

        self.retranslateUi(menu_inicial)
        QtCore.QMetaObject.connectSlotsByName(menu_inicial)

    def retranslateUi(self, menu_inicial):
        _translate = QtCore.QCoreApplication.translate
        menu_inicial.setWindowTitle(_translate("menu_inicial", "Form"))
        self.LabelGuiote.setText(_translate("menu_inicial", "Guiñote"))
        self.boton_jugar.setText(_translate("menu_inicial", "JUGAR"))
        self.boton_estadisticas.setText(_translate("menu_inicial", "ESTADISTICAS"))
        self.boton_tienda.setText(_translate("menu_inicial", "TIENDA"))
import Imagenes.imagenes_rc
