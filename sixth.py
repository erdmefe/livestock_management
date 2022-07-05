from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from describemenu import Ui_TanimlaMenu
from hastaliktanimla import Ui_HastalikTanimla
from asitanimla import Ui_AsiTanimla
from turtanimla import Ui_TurTanimla
import sqlite3
from dbconnection import cursor, connection

class DescMenu(QtWidgets.QWidget):
    def __init__(self):
        super(DescMenu, self).__init__()
        self.ui = Ui_TanimlaMenu()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)        
        self.ui.asitanimla.clicked.connect(self.ClickControl)
        self.ui.hastaliktanimla.clicked.connect(self.ClickControl)
        self.ui.kecitanimla.clicked.connect(self.ClickControl)
        self.hastalik_tanimla = HastalikTanimla()
        self.tur_tanimla = TurTanimla()
        self.asi_tanimla = AsiTanimla()
    def ClickControl(self):
        sender = self.sender().text()
        if sender == "Hastalık Tanımla":
            self.hastalik_tanimla.show()
            self.hide()
        elif sender == "Keçi Türü Tanımla":
            self.tur_tanimla.show()
            self.hide()
        elif sender == "Aşı Tanımla":
            self.asi_tanimla.show()
            self.hide()

    def ExitClickControl(self):
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.hide()
        win.show()
### Sub Classes ###
class HastalikTanimla(QtWidgets.QWidget):
    def __init__(self):
        super(HastalikTanimla, self).__init__()
        self.ui = Ui_HastalikTanimla()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
    
    def AcceptClickControl(self):
        try:
            hastalik = self.ui.hastalik.text()
            cursor.execute(f"INSERT INTO sicks (sicks) VALUES ('{hastalik}')")
            connection.commit()
            self.ui.result.setText(f"{hastalik} Başarıyla Tanımlandı")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()

class AsiTanimla(QtWidgets.QWidget):
    def __init__(self):
        super(AsiTanimla, self).__init__()
        self.ui = Ui_AsiTanimla()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
    
    def AcceptClickControl(self):
        try:
            vaccine = self.ui.hastalik.text()
            cursor.execute(f"INSERT INTO vaccines (vaccines) VALUES ('{vaccine}')")
            connection.commit()
            self.ui.result.setText(f"{vaccine} Başarıyla Tanımlandı")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()

class TurTanimla(QtWidgets.QWidget):
    def __init__(self):
        super(TurTanimla, self).__init__()
        self.ui = Ui_TurTanimla()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
    
    def AcceptClickControl(self):
        try:
            goat_type = self.ui.hastalik.text()
            cursor.execute(f"INSERT INTO types (type) VALUES ('{goat_type}')")
            connection.commit()
            self.ui.result.setText(f"{goat_type} Başarıyla Tanımlandı")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()