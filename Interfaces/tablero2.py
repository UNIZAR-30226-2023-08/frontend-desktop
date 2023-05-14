# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablero2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces.clickableLabel import ClickableLabel


class Ui_tablero2(object):
    def setupUi(self, tablero2):
        tablero2.setObjectName("tablero2")
        tablero2.resize(1500, 1000)
        tablero2.setMinimumSize(QtCore.QSize(1500, 1000))
        tablero2.setMaximumSize(QtCore.QSize(1500, 1000))
        tablero2.setAutoFillBackground(False)
        tablero2.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(tablero2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(tablero2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 0, 911, 949))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutCentral = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutCentral.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutCentral.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutCentral.setObjectName("verticalLayoutCentral")
        self.nombre_jugador1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nombre_jugador1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.nombre_jugador1.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre_jugador1.setObjectName("nombre_jugador1")
        self.verticalLayoutCentral.addWidget(self.nombre_jugador1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/cartas/cartas1/cartasRivalesHor.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutCentral.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/cartas/cartas1/dorso.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.carta_jugada2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada2.setEnabled(True)
        self.carta_jugada2.setAutoFillBackground(False)
        self.carta_jugada2.setText("")
        self.carta_jugada2.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada2.setAlignment(QtCore.Qt.AlignCenter)
        self.carta_jugada2.setObjectName("carta_jugada2")
        self.verticalLayout.addWidget(self.carta_jugada2)
        self.carta_jugada1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada1.setText("")
        self.carta_jugada1.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada1.setAlignment(QtCore.Qt.AlignCenter)
        self.carta_jugada1.setObjectName("carta_jugada1")
        self.verticalLayout.addWidget(self.carta_jugada1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.vacio = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.vacio.setText("")
        self.vacio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vacio.setObjectName("vacio")
        self.horizontalLayout_3.addWidget(self.vacio)
        self.verticalLayoutCentral.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.carta1 = ClickableLabel(self.verticalLayoutWidget)
        self.carta1.setPixmap(QtGui.QPixmap(":/logo/118x260.png"))
        self.carta1.setScaledContents(False)
        self.carta1.setAlignment(QtCore.Qt.AlignCenter)
        self.carta1.setWordWrap(False)
        self.carta1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.carta1.setObjectName("carta1")
        self.horizontalLayout_2.addWidget(self.carta1)
        self.carta2 = ClickableLabel(self.verticalLayoutWidget)
        self.carta2.setPixmap(QtGui.QPixmap(":/logo/118x260.png"))
        self.carta2.setAlignment(QtCore.Qt.AlignCenter)
        self.carta2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.carta2.setObjectName("carta2")
        self.horizontalLayout_2.addWidget(self.carta2)
        self.carta3 = ClickableLabel(self.verticalLayoutWidget)
        self.carta3.setPixmap(QtGui.QPixmap(":/logo/118x260.png"))
        self.carta3.setAlignment(QtCore.Qt.AlignCenter)
        self.carta3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.carta3.setObjectName("carta3")
        self.horizontalLayout_2.addWidget(self.carta3)
        self.carta4 = ClickableLabel(self.verticalLayoutWidget)
        self.carta4.setPixmap(QtGui.QPixmap(":/logo/118x260.png"))
        self.carta4.setAlignment(QtCore.Qt.AlignCenter)
        self.carta4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.carta4.setObjectName("carta4")
        self.horizontalLayout_2.addWidget(self.carta4)
        self.carta5 = ClickableLabel(self.verticalLayoutWidget)
        self.carta5.setPixmap(QtGui.QPixmap(":/logo/118x260.png"))
        self.carta5.setAlignment(QtCore.Qt.AlignCenter)
        self.carta5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.carta5.setObjectName("carta5")
        self.horizontalLayout_2.addWidget(self.carta5)
        self.carta6 = ClickableLabel(self.verticalLayoutWidget)
        self.carta6.setPixmap(QtGui.QPixmap(":/logo/118x260.png"))
        self.carta6.setAlignment(QtCore.Qt.AlignCenter)
        self.carta6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.carta6.setObjectName("carta6")
        self.horizontalLayout_2.addWidget(self.carta6)
        self.verticalLayoutCentral.addLayout(self.horizontalLayout_2)
        self.botonJugar = QtWidgets.QPushButton(tablero2)
        self.botonJugar.setEnabled(False)
        self.botonJugar.setGeometry(QtCore.QRect(1220, 810, 121, 41))
        self.botonJugar.setAutoFillBackground(False)
        self.botonJugar.setAutoDefault(False)
        self.botonJugar.setFlat(False)
        self.botonJugar.setObjectName("botonJugar")
        self.botonCambiar7 = QtWidgets.QPushButton(tablero2)
        self.botonCambiar7.setEnabled(False)
        self.botonCambiar7.setGeometry(QtCore.QRect(1370, 810, 111, 41))
        self.botonCambiar7.setObjectName("botonCambiar7")
        self.carta_triunfo = QtWidgets.QLabel(tablero2)
        self.carta_triunfo.setGeometry(QtCore.QRect(190, 320, 100, 200))
        self.carta_triunfo.setText("")
        self.carta_triunfo.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_triunfo.setScaledContents(False)
        self.carta_triunfo.setWordWrap(False)
        self.carta_triunfo.setObjectName("carta_triunfo")
        self.label_5 = QtWidgets.QLabel(tablero2)
        self.label_5.setGeometry(QtCore.QRect(0, -91, 1500, 1200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/logo/Tapete_verde.jpg"))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.boton_enviar_chat = QtWidgets.QPushButton(tablero2)
        self.boton_enviar_chat.setGeometry(QtCore.QRect(190, 900, 89, 25))
        self.boton_enviar_chat.setObjectName("boton_enviar_chat")
        self.chat_box = QtWidgets.QTextEdit(tablero2)
        self.chat_box.setGeometry(QtCore.QRect(20, 689, 261, 171))
        self.chat_box.setReadOnly(True)
        self.chat_box.setObjectName("chat_box")
        self.text_chat = QtWidgets.QLineEdit(tablero2)
        self.text_chat.setGeometry(QtCore.QRect(20, 860, 261, 25))
        self.text_chat.setObjectName("text_chat")
        self.nombre_jugador0 = QtWidgets.QLabel(tablero2)
        self.nombre_jugador0.setGeometry(QtCore.QRect(650, 960, 200, 17))
        self.nombre_jugador0.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre_jugador0.setObjectName("nombre_jugador0")
        self.label_5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.botonJugar.raise_()
        self.botonCambiar7.raise_()
        self.carta_triunfo.raise_()
        self.boton_enviar_chat.raise_()
        self.chat_box.raise_()
        self.text_chat.raise_()
        self.nombre_jugador0.raise_()

        self.retranslateUi(tablero2)
        QtCore.QMetaObject.connectSlotsByName(tablero2)

    def retranslateUi(self, tablero2):
        _translate = QtCore.QCoreApplication.translate
        self.nombre_jugador1.setText(_translate("tablero2", "TextLabel"))
        self.botonJugar.setText(_translate("tablero2", "Jugar"))
        self.botonCambiar7.setText(_translate("tablero2", "Cambiar 7"))
        self.boton_enviar_chat.setText(_translate("tablero2", "Enviar"))
        self.text_chat.setPlaceholderText(_translate("tablero2", "Escribe aquí"))
        self.nombre_jugador0.setText(_translate("tablero2", "TextLabel"))
import Imagenes.imagenes_rc
