# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablero.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces.clickableLabel import ClickableLabel


class Ui_Tablero(object):
    def setupUi(self, Tablero):
        Tablero.setObjectName("Tablero")
        Tablero.setEnabled(True)
        Tablero.resize(1400, 900)
        Tablero.setMaximumSize(QtCore.QSize(1500, 1000))
        self.centralwidget = QtWidgets.QWidget(Tablero)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 0, 856, 891))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutCentral = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutCentral.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutCentral.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutCentral.setObjectName("verticalLayoutCentral")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutCentral.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carta_jugada4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.carta_jugada4.setText("")
        self.carta_jugada4.setPixmap(QtGui.QPixmap(":/logo/100x200.png"))
        self.carta_jugada4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carta_jugada4.setObjectName("carta_jugada4")
        self.horizontalLayout_3.addWidget(self.carta_jugada4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.carta_jugada3 = QtWidgets.QLabel(self.verticalLayoutWidget)
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
        self.botonJugar = QtWidgets.QPushButton(self.centralwidget)
        self.botonJugar.setEnabled(False)
        self.botonJugar.setGeometry(QtCore.QRect(1110, 810, 121, 41))
        self.botonJugar.setObjectName("botonJugar")
        self.botonCantar = QtWidgets.QPushButton(self.centralwidget)
        self.botonCantar.setEnabled(False)
        self.botonCantar.setGeometry(QtCore.QRect(1260, 808, 111, 41))
        self.botonCantar.setObjectName("botonCantar")
        Tablero.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tablero)
        QtCore.QMetaObject.connectSlotsByName(Tablero)

    def retranslateUi(self, Tablero):
        _translate = QtCore.QCoreApplication.translate
        Tablero.setWindowTitle(_translate("Tablero", "MainWindow"))
        self.label_2.setText(_translate("Tablero", "TextLabel"))
        self.botonJugar.setText(_translate("Tablero", "Jugar"))
        self.botonCantar.setText(_translate("Tablero", "Cantar"))
import Imagenes.imagenes_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tablero = QtWidgets.QMainWindow()
    ui = Ui_Tablero()
    ui.setupUi(Tablero)
    Tablero.show()
    sys.exit(app.exec_())
