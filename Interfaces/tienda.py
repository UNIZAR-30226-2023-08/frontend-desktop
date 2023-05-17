# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tienda.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tienda(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 497)
        Form.setMinimumSize(QtCore.QSize(706, 497))
        Form.setMaximumSize(QtCore.QSize(706, 497))
        self.fondo = QtWidgets.QLabel(Form)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 706, 497))
        self.fondo.setText("")
        self.fondo.setPixmap(QtGui.QPixmap(":/logo/Tapete_verde.jpg"))
        self.fondo.setObjectName("fondo")
        self.boton_volver = QtWidgets.QPushButton(Form)
        self.boton_volver.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_volver.setFont(font)
        self.boton_volver.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_volver.setObjectName("boton_volver")
        self.titulotienda = QtWidgets.QLabel(Form)
        self.titulotienda.setGeometry(QtCore.QRect(250, -20, 209, 125))
        self.titulotienda.setMaximumSize(QtCore.QSize(231, 125))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.titulotienda.setFont(font)
        self.titulotienda.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.titulotienda.setAlignment(QtCore.Qt.AlignCenter)
        self.titulotienda.setObjectName("titulotienda")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 571, 291))
        self.label_3.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.titulomonedas_3 = QtWidgets.QLabel(Form)
        self.titulomonedas_3.setGeometry(QtCore.QRect(270, 80, 181, 51))
        self.titulomonedas_3.setMaximumSize(QtCore.QSize(231, 125))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titulomonedas_3.setFont(font)
        self.titulomonedas_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.titulomonedas_3.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.titulomonedas_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titulomonedas_3.setObjectName("titulomonedas_3")
        self.label_monedas = QtWidgets.QLabel(Form)
        self.label_monedas.setGeometry(QtCore.QRect(380, 70, 71, 71))
        self.label_monedas.setMaximumSize(QtCore.QSize(231, 125))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_monedas.setFont(font)
        self.label_monedas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_monedas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_monedas.setObjectName("label_monedas")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 220, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 270, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 320, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 370, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.equipar1 = QtWidgets.QPushButton(Form)
        self.equipar1.setGeometry(QtCore.QRect(480, 230, 97, 29))
        self.equipar1.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.equipar1.setObjectName("equipar1")
        self.comprar2 = QtWidgets.QPushButton(Form)
        self.comprar2.setGeometry(QtCore.QRect(296, 280, 111, 29))
        self.comprar2.setStyleSheet("background-color: rgb(255, 204, 0);")
        self.comprar2.setObjectName("comprar2")
        self.comprar3 = QtWidgets.QPushButton(Form)
        self.comprar3.setGeometry(QtCore.QRect(296, 330, 111, 29))
        self.comprar3.setStyleSheet("background-color: rgb(255, 204, 0);")
        self.comprar3.setObjectName("comprar3")
        self.comprar4 = QtWidgets.QPushButton(Form)
        self.comprar4.setGeometry(QtCore.QRect(296, 380, 111, 29))
        self.comprar4.setStyleSheet("background-color: rgb(255, 204, 0);")
        self.comprar4.setObjectName("comprar4")
        self.equipar2 = QtWidgets.QPushButton(Form)
        self.equipar2.setEnabled(False)
        self.equipar2.setGeometry(QtCore.QRect(480, 280, 97, 29))
        self.equipar2.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.equipar2.setObjectName("equipar2")
        self.equipar3 = QtWidgets.QPushButton(Form)
        self.equipar3.setEnabled(False)
        self.equipar3.setGeometry(QtCore.QRect(480, 330, 97, 29))
        self.equipar3.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.equipar3.setObjectName("equipar3")
        self.equipar4 = QtWidgets.QPushButton(Form)
        self.equipar4.setEnabled(False)
        self.equipar4.setGeometry(QtCore.QRect(480, 380, 97, 29))
        self.equipar4.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.equipar4.setObjectName("equipar4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.boton_volver.setText(_translate("Form", "Volver"))
        self.titulotienda.setText(_translate("Form", "Tienda"))
        self.titulomonedas_3.setText(_translate("Form", "    Monedas: "))
        self.label_monedas.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Estilos de barajas"))
        self.label_2.setText(_translate("Form", "Default"))
        self.label_4.setText(_translate("Form", "Noir"))
        self.label_5.setText(_translate("Form", "Classic"))
        self.label_6.setText(_translate("Form", "Classic-noir"))
        self.equipar1.setText(_translate("Form", "Equipado"))
        self.comprar2.setText(_translate("Form", "Comprar (30)"))
        self.comprar3.setText(_translate("Form", "Comprar(30)"))
        self.comprar4.setText(_translate("Form", "Comprar(30)"))
        self.equipar2.setText(_translate("Form", "Equipar"))
        self.equipar3.setText(_translate("Form", "Equipar"))
        self.equipar4.setText(_translate("Form", "Equipar"))
import Imagenes.imagenes_rc
