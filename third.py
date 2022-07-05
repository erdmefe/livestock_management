from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from datetime import date
from delmenu import Ui_SilMenu
from kecisilme import Ui_KeciSilme
from hastaliksilme import Ui_HastalikSilme
import sqlite3
from dbconnection import cursor, connection

class DelMenu(QtWidgets.QWidget):
    def __init__(self):
        super(DelMenu, self).__init__()
        self.ui = Ui_SilMenu()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.kecisil.clicked.connect(self.ClickControl)
        self.ui.hastaliksil.clicked.connect(self.ClickControl)
        self.del_goat = KeciSilme()
        self.del_sick = HastalikSilme()

    def ClickControl(self):
        sender = self.sender().text()
        if sender == "Keçi Sil":
            self.del_goat.show()
            self.hide()
        elif sender == "Hastalık Durumu Sil":
            self.del_sick.show()
            self.hide()
    def ExitClickControl(self):
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.hide()
        win.show()
### Sub Classes ###       
class KeciSilme(QtWidgets.QWidget):
    def __init__(self):
        super(KeciSilme, self).__init__()
        self.ui = Ui_KeciSilme()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.goatList.itemSelectionChanged.connect(self.Checking)
        self.ui.refreshbuton.clicked.connect(self.LoadData)
        self.LoadData()
        self.ui.result.clear()
    
    def LoadData(self):
        self.ui.goatList.clear()
        cursor.execute("SELECT keci_id FROM goats_table")
        goatList = []
        for i in cursor.fetchall():
            goatList.append(i[0])
        self.ui.goatList.addItems(goatList)
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        

    def Checking(self):
        try:
            currentText = self.ui.goatList.currentItem().text()
            self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
        except:
            pass
    def AcceptClickControl(self):
        try:
            currentText = self.ui.goatList.currentItem().text()
            cursor.execute(f"SELECT keci_id,baba_id,anne_id,dogum_tarihi,cinsiyeti,cinsi,asim_zamani FROM goats_table WHERE keci_id = '{currentText}'")
            goat = cursor.fetchone()
            reason = self.ui.reason.currentText()
            sql = f"INSERT INTO deleted_goats (keci_id,baba_id,anne_id,dogum_tarihi,cinsiyeti,cinsi,asim_zamani,delete_reason,delete_date) VALUES (?,?,?,?,?,?,?,?,?)"
            listed = [reason,date.today()]
            counter = 0
            for i in goat:
                listed.insert(counter,i)
                counter += 1
            print(listed)
            cursor.execute(sql,listed)
            self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
            self.ui.result.setText(f"{currentText} ID numaralı Keçi\nBaşarıyla Silindi")
            cursor.execute(f"DELETE FROM goats_table WHERE keci_id = '{currentText}'")
            connection.commit()
            item = self.ui.goatList.takeItem(self.ui.goatList.currentRow())
            del item
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

class HastalikSilme(QtWidgets.QWidget):
    def __init__(self):
        super(HastalikSilme, self).__init__()
        self.ui = Ui_HastalikSilme()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.goatList.itemSelectionChanged.connect(self.Checking)
        self.ui.refreshbuton.clicked.connect(self.LoadData)
        self.LoadData()
        self.ui.result.clear()
    
    def LoadData(self):
        self.ui.goatList.clear()
        cursor.execute(f"SELECT keci_id, sick_id, start_date FROM sick_report WHERE end_date is NULL")
        self.ui.goatList.setColumnCount(3)
        liste = cursor.fetchall()
        self.ui.goatList.setRowCount(len(liste))
        self.ui.goatList.setHorizontalHeaderLabels(("KEÇİ ID","HASTALIK","BAŞLANGIÇ"))
        for i in range(len(liste)):
            cursor.execute(f"SELECT keci_id from goats_table WHERE ID = {liste[i][0]}")
            x = cursor.fetchone()
            self.ui.goatList.setItem(i,0,QtWidgets.QTableWidgetItem(str(x[0])))

            cursor.execute(f"SELECT sicks from sicks WHERE ID = {liste[i][1]}")
            y = cursor.fetchone()
            self.ui.goatList.setItem(i,1,QtWidgets.QTableWidgetItem(str(y[0])))

            self.ui.goatList.setItem(i,2,QtWidgets.QTableWidgetItem(str(liste[i][2])))

        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        
      
    def Checking(self):
        currentTextRow = self.ui.goatList.currentRow()
        currentText = self.ui.goatList.item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
    
    def AcceptClickControl(self):
        try:
            currentTextRow = self.ui.goatList.currentRow()
            currentText = self.ui.goatList.item(currentTextRow,0).text()
            currentSick = self.ui.goatList.item(currentTextRow,1).text()
            currentDate = self.ui.goatList.item(currentTextRow,2).text()
            self.ui.result.setText(f"{currentText} ID numaralı Keçi\nBaşarıyla Silindi")
            cursor.execute(f"SELECT ID from goats_table WHERE keci_id = '{currentText}'")
            idNum = int(cursor.fetchone()[0])
            cursor.execute(f"SELECT ID from sicks WHERE sicks = '{currentSick}'")
            sickNum = int(cursor.fetchone()[0])
            cursor.execute(f"UPDATE sick_report SET end_date = '{date.today()}' WHERE keci_id = '{idNum}' AND sick_id = '{sickNum}' AND start_date = '{currentDate}'")
            connection.commit()
            self.ui.goatList.removeRow(self.ui.goatList.currentRow())
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