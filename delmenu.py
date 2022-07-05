# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delmenus.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SilMenu(object):
    def setupUi(self, SilMenu):
        SilMenu.setObjectName("SilMenu")
        SilMenu.resize(300, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SilMenu.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(SilMenu)
        self.verticalLayout.setContentsMargins(9, 40, -1, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kecisil = QtWidgets.QPushButton(SilMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kecisil.sizePolicy().hasHeightForWidth())
        self.kecisil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.kecisil.setFont(font)
        self.kecisil.setObjectName("kecisil")
        self.verticalLayout.addWidget(self.kecisil)
        self.hastaliksil = QtWidgets.QPushButton(SilMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hastaliksil.sizePolicy().hasHeightForWidth())
        self.hastaliksil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.hastaliksil.setFont(font)
        self.hastaliksil.setObjectName("hastaliksil")
        self.verticalLayout.addWidget(self.hastaliksil)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainmenubuton = QtWidgets.QPushButton(SilMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainmenubuton.sizePolicy().hasHeightForWidth())
        self.mainmenubuton.setSizePolicy(sizePolicy)
        self.mainmenubuton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenubuton.setIcon(icon1)
        self.mainmenubuton.setIconSize(QtCore.QSize(64, 64))
        self.mainmenubuton.setObjectName("mainmenubuton")
        self.horizontalLayout.addWidget(self.mainmenubuton)
        self.exitbuton = QtWidgets.QPushButton(SilMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbuton.sizePolicy().hasHeightForWidth())
        self.exitbuton.setSizePolicy(sizePolicy)
        self.exitbuton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/exits.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbuton.setIcon(icon2)
        self.exitbuton.setIconSize(QtCore.QSize(64, 64))
        self.exitbuton.setObjectName("exitbuton")
        self.horizontalLayout.addWidget(self.exitbuton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SilMenu)
        QtCore.QMetaObject.connectSlotsByName(SilMenu)

    def retranslateUi(self, SilMenu):
        _translate = QtCore.QCoreApplication.translate
        SilMenu.setWindowTitle(_translate("SilMenu", "Sil Menüsü"))
        self.kecisil.setText(_translate("SilMenu", "Keçi Sil"))
        self.hastaliksil.setText(_translate("SilMenu", "Hastalık Durumu Sil"))
