# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sutekles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SutEkle(object):
    def setupUi(self, SutEkle):
        SutEkle.setObjectName("SutEkle")
        SutEkle.resize(350, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SutEkle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SutEkle)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SutEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.kimlikno = QtWidgets.QLineEdit(SutEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kimlikno.setFont(font)
        self.kimlikno.setObjectName("kimlikno")
        self.gridLayout.addWidget(self.kimlikno, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(SutEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.sutmiktar = QtWidgets.QLineEdit(SutEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sutmiktar.setFont(font)
        self.sutmiktar.setObjectName("sutmiktar")
        self.gridLayout.addWidget(self.sutmiktar, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(SutEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.sutdate = QtWidgets.QDateEdit(SutEkle)
        self.sutdate.setCalendarPopup(True)
        self.sutdate.setObjectName("sutdate")
        self.gridLayout.addWidget(self.sutdate, 2, 1, 1, 1)
        self.result = QtWidgets.QLabel(SutEkle)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptbuton = QtWidgets.QPushButton(SutEkle)
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
        self.mainmenubuton = QtWidgets.QPushButton(SutEkle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainmenubuton.sizePolicy().hasHeightForWidth())
        self.mainmenubuton.setSizePolicy(sizePolicy)
        self.mainmenubuton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenubuton.setIcon(icon2)
        self.mainmenubuton.setIconSize(QtCore.QSize(64, 64))
        self.mainmenubuton.setObjectName("mainmenubuton")
        self.horizontalLayout.addWidget(self.mainmenubuton)
        self.exitbuton = QtWidgets.QPushButton(SutEkle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbuton.sizePolicy().hasHeightForWidth())
        self.exitbuton.setSizePolicy(sizePolicy)
        self.exitbuton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/exits.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbuton.setIcon(icon3)
        self.exitbuton.setIconSize(QtCore.QSize(64, 64))
        self.exitbuton.setObjectName("exitbuton")
        self.horizontalLayout.addWidget(self.exitbuton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.retranslateUi(SutEkle)
        QtCore.QMetaObject.connectSlotsByName(SutEkle)
        SutEkle.setTabOrder(self.kimlikno, self.sutdate)
        SutEkle.setTabOrder(self.sutdate, self.acceptbuton)
        SutEkle.setTabOrder(self.acceptbuton, self.exitbuton)

    def retranslateUi(self, SutEkle):
        _translate = QtCore.QCoreApplication.translate
        SutEkle.setWindowTitle(_translate("SutEkle", "Süt Verimi Bilgisi Ekle"))
        self.label.setText(_translate("SutEkle", "Keçi Kimlik No:"))
        self.label_5.setText(_translate("SutEkle", "Süt Miktarı (KG)"))
        self.label_4.setText(_translate("SutEkle", "Tarih"))