# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pruebalogin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prueba_login(object):
    def setupUi(self, prueba_login):
        prueba_login.setObjectName("prueba_login")
        prueba_login.resize(706, 497)
        prueba_login.setMinimumSize(QtCore.QSize(706, 497))
        prueba_login.setMaximumSize(QtCore.QSize(706, 497))
        prueba_login.setStyleSheet("#centralwidget{\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"#formLayout{\n"
"background-color: rgb(255,255,255)\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(prueba_login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayoutWidget = QtWidgets.QWidget(prueba_login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 290, 611, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(40, 0, 40, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_nombre_usuario = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre_usuario.setFont(font)
        self.label_nombre_usuario.setObjectName("label_nombre_usuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nombre_usuario)
        self.text_nombre_usuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.text_nombre_usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_nombre_usuario.setObjectName("text_nombre_usuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.text_nombre_usuario)
        self.label_contrasenya = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_contrasenya.setFont(font)
        self.label_contrasenya.setObjectName("label_contrasenya")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_contrasenya)
        self.text_contrasenya = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.text_contrasenya.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_contrasenya.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_contrasenya.setObjectName("text_contrasenya")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.text_contrasenya)
        self.boton_login = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton_login.setFont(font)
        self.boton_login.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.boton_login.setObjectName("boton_login")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.boton_login)
        self.label_foto_login = QtWidgets.QLabel(prueba_login)
        self.label_foto_login.setEnabled(True)
        self.label_foto_login.setGeometry(QtCore.QRect(93, 90, 521, 71))
        self.label_foto_login.setText("")
        self.label_foto_login.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.label_foto_login.setObjectName("label_foto_login")
        self.boton_registrarse = QtWidgets.QCommandLinkButton(prueba_login)
        self.boton_registrarse.setGeometry(QtCore.QRect(360, 380, 261, 30))
        self.boton_registrarse.setMaximumSize(QtCore.QSize(300, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(7, 64, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 28, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 64, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 28, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(7, 64, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 28, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.boton_registrarse.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.boton_registrarse.setFont(font)
        icon = QtGui.QIcon.fromTheme("network-receive")
        self.boton_registrarse.setIcon(icon)
        self.boton_registrarse.setIconSize(QtCore.QSize(0, 0))
        self.boton_registrarse.setObjectName("boton_registrarse")

        self.retranslateUi(prueba_login)
        QtCore.QMetaObject.connectSlotsByName(prueba_login)

    def retranslateUi(self, prueba_login):
        _translate = QtCore.QCoreApplication.translate
        self.label_nombre_usuario.setText(_translate("prueba_login", "Nombre de usuario:"))
        self.label_contrasenya.setText(_translate("prueba_login", "Contraseña:"))
        self.boton_login.setText(_translate("prueba_login", "Login"))
        self.boton_registrarse.setText(_translate("prueba_login", "¿No tienes cuenta? ¡Registrate gratis!"))
import Imagenes.imagenes_rc
