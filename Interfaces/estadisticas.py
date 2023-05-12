# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadisticas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_estadisticas(object):
    def setupUi(self, estadisticas):
        estadisticas.setObjectName("estadisticas")
        estadisticas.resize(706, 497)
        self.formLayoutWidget = QtWidgets.QWidget(estadisticas)
        self.formLayoutWidget.setGeometry(QtCore.QRect(180, 20, 341, 134))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_nombre = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_nombre.setObjectName("label_nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_nombre)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_vicrotias_derrotas = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_vicrotias_derrotas.setObjectName("label_vicrotias_derrotas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_vicrotias_derrotas)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_porcentaje_victorias = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_porcentaje_victorias.setObjectName("label_porcentaje_victorias")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_porcentaje_victorias)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_puntos = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_puntos.setObjectName("label_puntos")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_puntos)
        self.listWidget = QtWidgets.QListWidget(estadisticas)
        self.listWidget.setGeometry(QtCore.QRect(-10, 190, 721, 311))
        self.listWidget.setObjectName("listWidget")
        self.label_5 = QtWidgets.QLabel(estadisticas)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 171, 21))
        self.label_5.setObjectName("label_5")
        self.boton_volver = QtWidgets.QPushButton(estadisticas)
        self.boton_volver.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_volver.setFont(font)
        self.boton_volver.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_volver.setObjectName("boton_volver")

        self.retranslateUi(estadisticas)
        QtCore.QMetaObject.connectSlotsByName(estadisticas)

    def retranslateUi(self, estadisticas):
        _translate = QtCore.QCoreApplication.translate
        estadisticas.setWindowTitle(_translate("estadisticas", "Form"))
        self.label.setText(_translate("estadisticas", "Nombre de usuario:"))
        self.label_nombre.setText(_translate("estadisticas", "TextLabel"))
        self.label_2.setText(_translate("estadisticas", "Victorias/Derrotas:"))
        self.label_vicrotias_derrotas.setText(_translate("estadisticas", "TextLabel"))
        self.label_3.setText(_translate("estadisticas", "% de Victorias:"))
        self.label_porcentaje_victorias.setText(_translate("estadisticas", "TextLabel"))
        self.label_4.setText(_translate("estadisticas", "Puntos:"))
        self.label_puntos.setText(_translate("estadisticas", "TextLabel"))
        self.label_5.setText(_translate("estadisticas", "Ranking de jugadores"))
        self.boton_volver.setText(_translate("estadisticas", "Volver"))
