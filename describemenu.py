# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'describemenus.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TanimlaMenu(object):
    def setupUi(self, TanimlaMenu):
        TanimlaMenu.setObjectName("TanimlaMenu")
        TanimlaMenu.resize(300, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TanimlaMenu.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(TanimlaMenu)
        self.verticalLayout.setContentsMargins(-1, 30, -1, 30)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hastaliktanimla = QtWidgets.QPushButton(TanimlaMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hastaliktanimla.sizePolicy().hasHeightForWidth())
        self.hastaliktanimla.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hastaliktanimla.setFont(font)
        self.hastaliktanimla.setObjectName("hastaliktanimla")
        self.verticalLayout.addWidget(self.hastaliktanimla)
        self.kecitanimla = QtWidgets.QPushButton(TanimlaMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kecitanimla.sizePolicy().hasHeightForWidth())
        self.kecitanimla.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.kecitanimla.setFont(font)
        self.kecitanimla.setObjectName("kecitanimla")
        self.verticalLayout.addWidget(self.kecitanimla)
        self.asitanimla = QtWidgets.QPushButton(TanimlaMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asitanimla.sizePolicy().hasHeightForWidth())
        self.asitanimla.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.asitanimla.setFont(font)
        self.asitanimla.setObjectName("asitanimla")
        self.verticalLayout.addWidget(self.asitanimla)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainmenubuton = QtWidgets.QPushButton(TanimlaMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainmenubuton.sizePolicy().hasHeightForWidth())
        self.mainmenubuton.setSizePolicy(sizePolicy)
        self.mainmenubuton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenubuton.setIcon(icon1)
        self.mainmenubuton.setIconSize(QtCore.QSize(32, 32))
        self.mainmenubuton.setObjectName("mainmenubuton")
        self.horizontalLayout.addWidget(self.mainmenubuton)
        self.exitbuton = QtWidgets.QPushButton(TanimlaMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbuton.sizePolicy().hasHeightForWidth())
        self.exitbuton.setSizePolicy(sizePolicy)
        self.exitbuton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/exits.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbuton.setIcon(icon2)
        self.exitbuton.setIconSize(QtCore.QSize(32, 32))
        self.exitbuton.setObjectName("exitbuton")
        self.horizontalLayout.addWidget(self.exitbuton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TanimlaMenu)
        QtCore.QMetaObject.connectSlotsByName(TanimlaMenu)

    def retranslateUi(self, TanimlaMenu):
        _translate = QtCore.QCoreApplication.translate
        TanimlaMenu.setWindowTitle(_translate("TanimlaMenu", "Tanımla Menüsü"))
        self.hastaliktanimla.setText(_translate("TanimlaMenu", "Hastalık Tanımla"))
        self.kecitanimla.setText(_translate("TanimlaMenu", "Keçi Türü Tanımla"))
        self.asitanimla.setText(_translate("TanimlaMenu", "Aşı Tanımla"))
