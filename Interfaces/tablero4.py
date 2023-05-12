# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablero4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces.clickableLabel import ClickableLabel


class Ui_tablero4(object):
    def setupUi(self, tablero4):
        tablero4.setObjectName("tablero4")
        tablero4.resize(1500, 1000)
        tablero4.setMinimumSize(QtCore.QSize(1500, 1000))
        tablero4.setMaximumSize(QtCore.QSize(1500, 1000))
        tablero4.setAutoFillBackground(False)
        tablero4.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(tablero4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(tablero4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 0, 911, 949))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutCentral = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutCentral.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutCentral.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutCentral.setObjectName("verticalLayoutCentral")
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
        self.carta_jugada4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada4.setAutoFillBackground(False)
        self.carta_jugada4.setText("")
        self.carta_jugada4.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carta_jugada4.setObjectName("carta_jugada4")
        self.horizontalLayout_4.addWidget(self.carta_jugada4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.carta_jugada3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada3.setEnabled(True)
        self.carta_jugada3.setAutoFillBackground(False)
        self.carta_jugada3.setText("")
        self.carta_jugada3.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada3.setAlignment(QtCore.Qt.AlignCenter)
        self.carta_jugada3.setObjectName("carta_jugada3")
        self.verticalLayout.addWidget(self.carta_jugada3)
        self.carta_jugada1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada1.setText("")
        self.carta_jugada1.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada1.setAlignment(QtCore.Qt.AlignCenter)
        self.carta_jugada1.setObjectName("carta_jugada1")
        self.verticalLayout.addWidget(self.carta_jugada1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.carta_jugada2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada2.setText("")
        self.carta_jugada2.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.carta_jugada2.setObjectName("carta_jugada2")
        self.horizontalLayout_3.addWidget(self.carta_jugada2)
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
        self.botonJugar = QtWidgets.QPushButton(tablero4)
        self.botonJugar.setEnabled(False)
        self.botonJugar.setGeometry(QtCore.QRect(1220, 810, 121, 41))
        self.botonJugar.setAutoFillBackground(False)
        self.botonJugar.setAutoDefault(False)
        self.botonJugar.setFlat(False)
        self.botonJugar.setObjectName("botonJugar")
        self.botonCambiar7 = QtWidgets.QPushButton(tablero4)
        self.botonCambiar7.setEnabled(False)
        self.botonCambiar7.setGeometry(QtCore.QRect(1370, 810, 111, 41))
        self.botonCambiar7.setObjectName("botonCambiar7")
        self.carta_triunfo = QtWidgets.QLabel(tablero4)
        self.carta_triunfo.setGeometry(QtCore.QRect(190, 320, 100, 200))
        self.carta_triunfo.setText("")
        self.carta_triunfo.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_triunfo.setScaledContents(False)
        self.carta_triunfo.setWordWrap(False)
        self.carta_triunfo.setObjectName("carta_triunfo")
        self.label = QtWidgets.QLabel(tablero4)
        self.label.setGeometry(QtCore.QRect(0, 50, 121, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cartas/cartas1/cartasRivalesVer.png"))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(tablero4)
        self.label_4.setGeometry(QtCore.QRect(1310, 50, 121, 611))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/cartas/cartas1/cartasRivalesVer.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(tablero4)
        self.label_5.setGeometry(QtCore.QRect(0, -91, 1500, 1200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/logo/Tapete_verde.jpg"))
        self.label_5.setObjectName("label_5")
        self.boton_enviar_chat = QtWidgets.QPushButton(tablero4)
        self.boton_enviar_chat.setGeometry(QtCore.QRect(190, 900, 89, 25))
        self.boton_enviar_chat.setObjectName("boton_enviar_chat")
        self.chat_box = QtWidgets.QTextEdit(tablero4)
        self.chat_box.setGeometry(QtCore.QRect(20, 689, 261, 171))
        self.chat_box.setReadOnly(True)
        self.chat_box.setObjectName("chat_box")
        self.text_chat = QtWidgets.QLineEdit(tablero4)
        self.text_chat.setGeometry(QtCore.QRect(20, 860, 261, 25))
        self.text_chat.setObjectName("text_chat")
        self.label_5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.botonJugar.raise_()
        self.botonCambiar7.raise_()
        self.carta_triunfo.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.boton_enviar_chat.raise_()
        self.chat_box.raise_()
        self.text_chat.raise_()

        self.retranslateUi(tablero4)
        QtCore.QMetaObject.connectSlotsByName(tablero4)

    def retranslateUi(self, tablero4):
        _translate = QtCore.QCoreApplication.translate
        self.botonJugar.setText(_translate("tablero4", "Jugar"))
        self.botonCambiar7.setText(_translate("tablero4", "Cambiar 7"))
        self.boton_enviar_chat.setText(_translate("tablero4", "Enviar"))
        self.text_chat.setPlaceholderText(_translate("tablero4", "Escribe aquí"))
import Imagenes.imagenes_rc
