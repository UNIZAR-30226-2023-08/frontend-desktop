# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pruebaregistro.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prueba_registro(object):
    def setupUi(self, prueba_registro):
        prueba_registro.setObjectName("prueba_registro")
        prueba_registro.resize(706, 497)
        prueba_registro.setMinimumSize(QtCore.QSize(706, 497))
        prueba_registro.setMaximumSize(QtCore.QSize(706, 497))
        prueba_registro.setStyleSheet("#centralwidget{\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"#formLayout{\n"
"background-color: rgb(255,255,255)\n"
"}")
        self.formLayoutWidget = QtWidgets.QWidget(prueba_registro)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 242, 581, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(40, 0, 40, 0)
        self.formLayout.setSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label_nombre_real = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre_real.setFont(font)
        self.label_nombre_real.setObjectName("label_nombre_real")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nombre_real)
        self.text_nombre_real = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.text_nombre_real.setObjectName("text_nombre_real")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.text_nombre_real)
        self.label_nombre_usuario_registro = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre_usuario_registro.setFont(font)
        self.label_nombre_usuario_registro.setObjectName("label_nombre_usuario_registro")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_nombre_usuario_registro)
        self.text_nombre_usuario_registro = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.text_nombre_usuario_registro.setObjectName("text_nombre_usuario_registro")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.text_nombre_usuario_registro)
        self.label_correo = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_correo.setFont(font)
        self.label_correo.setObjectName("label_correo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_correo)
        self.text_correo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.text_correo.setObjectName("text_correo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.text_correo)
        self.boton_terminos = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_terminos.setFont(font)
        self.boton_terminos.setObjectName("boton_terminos")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.boton_terminos)
        self.boton_confirmar_registro = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_confirmar_registro.setFont(font)
        self.boton_confirmar_registro.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_confirmar_registro.setObjectName("boton_confirmar_registro")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.boton_confirmar_registro)
        self.text_contrasenya_registro = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.text_contrasenya_registro.setObjectName("text_contrasenya_registro")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.text_contrasenya_registro)
        self.label_contrasenya_registro = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_contrasenya_registro.setFont(font)
        self.label_contrasenya_registro.setObjectName("label_contrasenya_registro")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_contrasenya_registro)
        self.label = QtWidgets.QLabel(prueba_registro)
        self.label.setGeometry(QtCore.QRect(93, 90, 521, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.label.setObjectName("label")

        self.retranslateUi(prueba_registro)
        QtCore.QMetaObject.connectSlotsByName(prueba_registro)

    def retranslateUi(self, prueba_registro):
        _translate = QtCore.QCoreApplication.translate
        self.label_nombre_real.setText(_translate("prueba_registro", "Nombre real:"))
        self.label_nombre_usuario_registro.setText(_translate("prueba_registro", "Nombre de usuario:"))
        self.label_correo.setText(_translate("prueba_registro", "Correo electrónico:"))
        self.boton_terminos.setText(_translate("prueba_registro", "Acepto los términos y condiciones"))
        self.boton_confirmar_registro.setText(_translate("prueba_registro", "Registrarse"))
        self.label_contrasenya_registro.setText(_translate("prueba_registro", "Contraseña:"))
import Imagenes.imagenes_rc
