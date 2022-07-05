# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asimekles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AsimEkle(object):
    def setupUi(self, AsimEkle):
        AsimEkle.setObjectName("AsimEkle")
        AsimEkle.resize(350, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AsimEkle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AsimEkle)
        self.gridLayout.setContentsMargins(-1, 20, -1, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(AsimEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptbuton = QtWidgets.QPushButton(AsimEkle)
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
        self.mainmenubuton = QtWidgets.QPushButton(AsimEkle)
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
        self.exitbuton = QtWidgets.QPushButton(AsimEkle)
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
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(AsimEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.kimlikno = QtWidgets.QLineEdit(AsimEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kimlikno.setFont(font)
        self.kimlikno.setObjectName("kimlikno")
        self.gridLayout.addWidget(self.kimlikno, 0, 1, 1, 2)
        self.asimdate = QtWidgets.QDateEdit(AsimEkle)
        self.asimdate.setCalendarPopup(True)
        self.asimdate.setObjectName("asimdate")
        self.gridLayout.addWidget(self.asimdate, 1, 1, 2, 2)
        self.result = QtWidgets.QLabel(AsimEkle)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 4, 0, 2, 3)

        self.retranslateUi(AsimEkle)
        QtCore.QMetaObject.connectSlotsByName(AsimEkle)
        AsimEkle.setTabOrder(self.kimlikno, self.asimdate)
        AsimEkle.setTabOrder(self.asimdate, self.acceptbuton)
        AsimEkle.setTabOrder(self.acceptbuton, self.mainmenubuton)
        AsimEkle.setTabOrder(self.mainmenubuton, self.exitbuton)

    def retranslateUi(self, AsimEkle):
        _translate = QtCore.QCoreApplication.translate
        AsimEkle.setWindowTitle(_translate("AsimEkle", "Aşım Tarihi Ekle"))
        self.label_4.setText(_translate("AsimEkle", "Aşım Tarihi"))
        self.label.setText(_translate("AsimEkle", "Keçi Kimlik No:"))
