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
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 711, 111))
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
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_porcentaje_victorias = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_porcentaje_victorias.setObjectName("label_porcentaje_victorias")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_porcentaje_victorias)
        self.label_puntos = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_puntos.setObjectName("label_puntos")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_puntos)
        self.listWidget = QtWidgets.QListWidget(estadisticas)
        self.listWidget.setGeometry(QtCore.QRect(-10, 140, 721, 361))
        self.listWidget.setObjectName("listWidget")
        self.label_5 = QtWidgets.QLabel(estadisticas)
        self.label_5.setGeometry(QtCore.QRect(0, 120, 151, 17))
        self.label_5.setObjectName("label_5")

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
        self.label_4.setText(_translate("estadisticas", "Puntos:"))
        self.label_porcentaje_victorias.setText(_translate("estadisticas", "TextLabel"))
        self.label_puntos.setText(_translate("estadisticas", "TextLabel"))
        self.label_5.setText(_translate("estadisticas", "Ranking de jugadores"))
