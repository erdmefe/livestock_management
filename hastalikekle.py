# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hastalikekles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HastalikEkle(object):
    def setupUi(self, HastalikEkle):
        HastalikEkle.setObjectName("HastalikEkle")
        HastalikEkle.resize(350, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HastalikEkle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(HastalikEkle)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HastalikEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.result = QtWidgets.QLabel(HastalikEkle)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 4, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptbuton = QtWidgets.QPushButton(HastalikEkle)
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
        self.refreshbuton = QtWidgets.QPushButton(HastalikEkle)
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
        self.mainmenubuton = QtWidgets.QPushButton(HastalikEkle)
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
        self.exitbuton = QtWidgets.QPushButton(HastalikEkle)
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
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(HastalikEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(HastalikEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.kimlikno = QtWidgets.QLineEdit(HastalikEkle)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kimlikno.setFont(font)
        self.kimlikno.setObjectName("kimlikno")
        self.gridLayout.addWidget(self.kimlikno, 0, 1, 1, 1)
        self.hastalikdate = QtWidgets.QDateEdit(HastalikEkle)
        self.hastalikdate.setCalendarPopup(True)
        self.hastalikdate.setObjectName("hastalikdate")
        self.gridLayout.addWidget(self.hastalikdate, 2, 1, 1, 1)
        self.hastaliklar = QtWidgets.QComboBox(HastalikEkle)
        self.hastaliklar.setObjectName("hastaliklar")
        self.gridLayout.addWidget(self.hastaliklar, 1, 1, 1, 1)

        self.retranslateUi(HastalikEkle)
        QtCore.QMetaObject.connectSlotsByName(HastalikEkle)
        HastalikEkle.setTabOrder(self.kimlikno, self.hastaliklar)
        HastalikEkle.setTabOrder(self.hastaliklar, self.hastalikdate)
        HastalikEkle.setTabOrder(self.hastalikdate, self.acceptbuton)
        HastalikEkle.setTabOrder(self.acceptbuton, self.refreshbuton)
        HastalikEkle.setTabOrder(self.refreshbuton, self.mainmenubuton)
        HastalikEkle.setTabOrder(self.mainmenubuton, self.exitbuton)

    def retranslateUi(self, HastalikEkle):
        _translate = QtCore.QCoreApplication.translate
        HastalikEkle.setWindowTitle(_translate("HastalikEkle", "Hastalık Durumu Ekle"))
        self.label.setText(_translate("HastalikEkle", "Keçi Kimlik No:"))
        self.label_4.setText(_translate("HastalikEkle", "Başlangıç Tarihi :"))
        self.label_5.setText(_translate("HastalikEkle", "Hastalık Seçin"))
