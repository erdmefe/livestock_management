# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kiloduzenles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KiloDuzenle(object):
    def setupUi(self, KiloDuzenle):
        KiloDuzenle.setObjectName("KiloDuzenle")
        KiloDuzenle.resize(676, 464)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/keçi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KiloDuzenle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(KiloDuzenle)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(30, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.goatList = QtWidgets.QTableWidget(KiloDuzenle)
        self.goatList.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.goatList.setDragEnabled(True)
        self.goatList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.goatList.setObjectName("goatList")
        self.goatList.setColumnCount(3)
        self.goatList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.goatList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.goatList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.goatList.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.goatList, 0, 0, 5, 1)
        self.result = QtWidgets.QLabel(KiloDuzenle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 2, 1, 1, 1)
        self.goatshow = QtWidgets.QLabel(KiloDuzenle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goatshow.sizePolicy().hasHeightForWidth())
        self.goatshow.setSizePolicy(sizePolicy)
        self.goatshow.setMinimumSize(QtCore.QSize(240, 240))
        self.goatshow.setMaximumSize(QtCore.QSize(240, 240))
        self.goatshow.setAutoFillBackground(False)
        self.goatshow.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.goatshow.setText("")
        self.goatshow.setPixmap(QtGui.QPixmap("icons/keçi.ico"))
        self.goatshow.setScaledContents(True)
        self.goatshow.setObjectName("goatshow")
        self.gridLayout.addWidget(self.goatshow, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptbuton = QtWidgets.QPushButton(KiloDuzenle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptbuton.sizePolicy().hasHeightForWidth())
        self.acceptbuton.setSizePolicy(sizePolicy)
        self.acceptbuton.setMinimumSize(QtCore.QSize(75, 100))
        self.acceptbuton.setMaximumSize(QtCore.QSize(150, 100))
        self.acceptbuton.setStyleSheet("")
        self.acceptbuton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acceptbuton.setIcon(icon1)
        self.acceptbuton.setIconSize(QtCore.QSize(64, 64))
        self.acceptbuton.setObjectName("acceptbuton")
        self.horizontalLayout.addWidget(self.acceptbuton)
        self.mainmenubuton = QtWidgets.QPushButton(KiloDuzenle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainmenubuton.sizePolicy().hasHeightForWidth())
        self.mainmenubuton.setSizePolicy(sizePolicy)
        self.mainmenubuton.setMaximumSize(QtCore.QSize(150, 100))
        self.mainmenubuton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainmenubuton.setIcon(icon2)
        self.mainmenubuton.setIconSize(QtCore.QSize(64, 64))
        self.mainmenubuton.setObjectName("mainmenubuton")
        self.horizontalLayout.addWidget(self.mainmenubuton)
        self.exitbuton = QtWidgets.QPushButton(KiloDuzenle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbuton.sizePolicy().hasHeightForWidth())
        self.exitbuton.setSizePolicy(sizePolicy)
        self.exitbuton.setMaximumSize(QtCore.QSize(150, 100))
        self.exitbuton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/exits.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbuton.setIcon(icon3)
        self.exitbuton.setIconSize(QtCore.QSize(64, 64))
        self.exitbuton.setObjectName("exitbuton")
        self.horizontalLayout.addWidget(self.exitbuton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.refreshbuton = QtWidgets.QPushButton(KiloDuzenle)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshbuton.setIcon(icon4)
        self.refreshbuton.setObjectName("refreshbuton")
        self.gridLayout.addWidget(self.refreshbuton, 1, 1, 1, 1)

        self.retranslateUi(KiloDuzenle)
        QtCore.QMetaObject.connectSlotsByName(KiloDuzenle)
        KiloDuzenle.setTabOrder(self.acceptbuton, self.exitbuton)

    def retranslateUi(self, KiloDuzenle):
        _translate = QtCore.QCoreApplication.translate
        KiloDuzenle.setWindowTitle(_translate("KiloDuzenle", "Kilo Bilgisi Düzenle"))
        self.goatList.setSortingEnabled(True)
        item = self.goatList.horizontalHeaderItem(0)
        item.setText(_translate("KiloDuzenle", "Keçi ID"))
        item = self.goatList.horizontalHeaderItem(1)
        item.setText(_translate("KiloDuzenle", "Kilo"))
        item = self.goatList.horizontalHeaderItem(2)
        item.setText(_translate("KiloDuzenle", "Tarih"))
        self.refreshbuton.setText(_translate("KiloDuzenle", "Yenile"))
