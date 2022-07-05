# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kecisilmes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeciSilme(object):
    def setupUi(self, KeciSilme):
        KeciSilme.setObjectName("KeciSilme")
        KeciSilme.resize(400, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KeciSilme.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(KeciSilme)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(KeciSilme)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(KeciSilme)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.result = QtWidgets.QLabel(KeciSilme)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 7, 0, 1, 2)
        self.goatshow = QtWidgets.QLabel(KeciSilme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goatshow.sizePolicy().hasHeightForWidth())
        self.goatshow.setSizePolicy(sizePolicy)
        self.goatshow.setMinimumSize(QtCore.QSize(100, 100))
        self.goatshow.setAutoFillBackground(False)
        self.goatshow.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.goatshow.setText("")
        self.goatshow.setPixmap(QtGui.QPixmap("icons/keçi.ico"))
        self.goatshow.setScaledContents(True)
        self.goatshow.setObjectName("goatshow")
        self.gridLayout.addWidget(self.goatshow, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptbuton = QtWidgets.QPushButton(KeciSilme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptbuton.sizePolicy().hasHeightForWidth())
        self.acceptbuton.setSizePolicy(sizePolicy)
        self.acceptbuton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acceptbuton.setIcon(icon1)
        self.acceptbuton.setIconSize(QtCore.QSize(64, 64))
        self.acceptbuton.setObjectName("acceptbuton")
        self.horizontalLayout.addWidget(self.acceptbuton)
        self.refreshbuton = QtWidgets.QPushButton(KeciSilme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshbuton.sizePolicy().hasHeightForWidth())
        self.refreshbuton.setSizePolicy(sizePolicy)
        self.refreshbuton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshbuton.setIcon(icon2)
        self.refreshbuton.setIconSize(QtCore.QSize(64, 64))
        self.refreshbuton.setObjectName("refreshbuton")
        self.horizontalLayout.addWidget(self.refreshbuton)
        self.mainmenubuton = QtWidgets.QPushButton(KeciSilme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainmenubuton.sizePolicy().hasHeightForWidth())
        self.mainmenubuton.setSizePolicy(sizePolicy)
        self.mainmenubuton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenubuton.setIcon(icon3)
        self.mainmenubuton.setIconSize(QtCore.QSize(64, 64))
        self.mainmenubuton.setObjectName("mainmenubuton")
        self.horizontalLayout.addWidget(self.mainmenubuton)
        self.exitbuton = QtWidgets.QPushButton(KeciSilme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbuton.sizePolicy().hasHeightForWidth())
        self.exitbuton.setSizePolicy(sizePolicy)
        self.exitbuton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/exits.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbuton.setIcon(icon4)
        self.exitbuton.setIconSize(QtCore.QSize(64, 64))
        self.exitbuton.setObjectName("exitbuton")
        self.horizontalLayout.addWidget(self.exitbuton)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 3)
        self.reason = QtWidgets.QComboBox(KeciSilme)
        self.reason.setObjectName("reason")
        self.reason.addItem("")
        self.reason.addItem("")
        self.gridLayout.addWidget(self.reason, 3, 2, 1, 1)
        self.goatList = QtWidgets.QListWidget(KeciSilme)
        self.goatList.setObjectName("goatList")
        self.gridLayout.addWidget(self.goatList, 1, 0, 3, 2)

        self.retranslateUi(KeciSilme)
        QtCore.QMetaObject.connectSlotsByName(KeciSilme)
        KeciSilme.setTabOrder(self.goatList, self.reason)
        KeciSilme.setTabOrder(self.reason, self.acceptbuton)
        KeciSilme.setTabOrder(self.acceptbuton, self.mainmenubuton)
        KeciSilme.setTabOrder(self.mainmenubuton, self.exitbuton)

    def retranslateUi(self, KeciSilme):
        _translate = QtCore.QCoreApplication.translate
        KeciSilme.setWindowTitle(_translate("KeciSilme", "Keçi Sil"))
        self.label.setText(_translate("KeciSilme", "Silinecek Keçiyi Seçin:"))
        self.label_5.setText(_translate("KeciSilme", "Silme Sebebi"))
        self.reason.setItemText(0, _translate("KeciSilme", "Ölüm"))
        self.reason.setItemText(1, _translate("KeciSilme", "Satış"))
