from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from editmenu import Ui_DuzenleMenu
from keciduzenle import Ui_KeciDuzenle
from kiloduzenle import Ui_KiloDuzenle
from sutverimiduzenle import Ui_SutVerimiDuzenle
from hastalikduzenle import Ui_HastalikDuzenle
from asiduzenle import Ui_AsiDuzenle
import sqlite3
from dbconnection import cursor, connection

class EditMenu(QtWidgets.QWidget):
    def __init__(self):
        super(EditMenu, self).__init__()
        self.ui = Ui_DuzenleMenu()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)        
        self.ui.asiduzenle.clicked.connect(self.ClickControl)
        self.ui.hastalikduzenle.clicked.connect(self.ClickControl)
        self.ui.keciduzenle.clicked.connect(self.ClickControl)
        self.ui.kiloduzenle.clicked.connect(self.ClickControl)
        self.ui.sutduzenle.clicked.connect(self.ClickControl)
        self.keci_duzenle = KeciDuzenle()
        self.verim_duzenle = SutVerimiDuzenle()
        self.kilo_duzenle = KiloDuzenle()        
        self.hastalik_duzenle = HastalikDuzenle()
        self.asi_duzenle = AsiDuzenle()

    def ClickControl(self):
        sender = self.sender().text()
        if sender == "Keçi Bilgileri Düzenle":
            self.keci_duzenle.show()
            self.hide()
        elif sender == "Süt Verimi Düzenle":
            self.verim_duzenle.show()
            self.hide()
        elif sender == "Kilo Bilgisi Düzenle":
            self.kilo_duzenle.show()
            self.hide()
        elif sender == "Hastalık Bilgisi Düzenle":
            self.hastalik_duzenle.show()
            self.hide()
        elif sender == "Aşı Durumu Düzenle":
            self.asi_duzenle.show()
            self.hide()
    def ExitClickControl(self):
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.hide()
        win.show()
### Sub Classes ###
class KeciDuzenle(QtWidgets.QWidget):
    def __init__(self):
        super(KeciDuzenle, self).__init__()
        self.ui = Ui_KeciDuzenle()
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
        self.ui.goatList.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
        cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table")
        liste = cursor.fetchall()
        self.liste = liste
        self.ui.goatList.setRowCount(len(liste))
        for i in range(len(liste)):   
            self.ui.goatList.setItem(i,0,QtWidgets.QTableWidgetItem(str(liste[i][0])))
            try:
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][1]}'")
                self.ui.goatList.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            except:
                pass 
            try:   
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][2]}'")
                self.ui.goatList.setItem(i,2,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            except:
                pass
            try:
                cursor.execute(f"SELECT type from types where ID = '{liste[i][5]}'")            
                self.ui.goatList.setItem(i,5,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            except:
                pass
            self.ui.goatList.setItem(i,3,QtWidgets.QTableWidgetItem(str(liste[i][3])))
            self.ui.goatList.setItem(i,4,QtWidgets.QTableWidgetItem(str(liste[i][4])))            
            self.ui.goatList.setItem(i,6,QtWidgets.QTableWidgetItem(str(liste[i][6])))
            
        self.ui.goatList.cellChanged.connect(self.Changing)
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        
    def AcceptClickControl(self):
        self.ui.result.setText("Kaydedildi")       

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()    
    def Checking(self):
        currentTextRow = self.ui.goatList.currentRow()
        currentText = self.ui.goatList.item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
    def Changing(self,row,column):
        try:
            data = self.ui.goatList.item(row,column).text()
            keci = self.ui.goatList.item(row,0).text()
            previous_id = self.liste[row][0]
            if column == 0:
                cursor.execute(f"UPDATE goats_table SET keci_id ='{data}' WHERE keci_id = '{previous_id}' ") ##keci yerine önceki değer
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table")
                self.liste = cursor.fetchall()
            elif column == 1:
                cursor.execute(f"SELECT ID from goats_table where keci_id = '{data}'")
                data = cursor.fetchone()[0]
                cursor.execute(f"UPDATE goats_table SET baba_id ='{data}' WHERE keci_id = '{keci}' ")
            elif column == 2:
                cursor.execute(f"SELECT ID from goats_table where keci_id = '{data}'")
                data = cursor.fetchone()[0]
                cursor.execute(f"UPDATE goats_table SET anne_id ='{data}' WHERE keci_id = '{keci}' ")
            elif column == 3:
                cursor.execute(f"UPDATE goats_table SET dogum_tarihi ='{data}' WHERE keci_id = '{keci}' ")
            elif column == 4:
                cursor.execute(f"UPDATE goats_table SET cinsiyeti ='{data}'WHERE keci_id = '{keci}' ")
            elif column == 5:
                cursor.execute(f"SELECT ID from types where type = '{data}'")
                data = cursor.fetchone()[0]
                cursor.execute(f"UPDATE goats_table SET cinsi ='{data}' WHERE keci_id = '{keci}' ")
            elif column == 6:   
                cursor.execute(f"UPDATE goats_table SET asim_zamani ='{data}' WHERE keci_id = '{keci}' ")  
            connection.commit()
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")

class SutVerimiDuzenle(QtWidgets.QWidget):
    def __init__(self):
        super(SutVerimiDuzenle, self).__init__()
        self.ui = Ui_SutVerimiDuzenle()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.goatList.itemSelectionChanged.connect(self.Checking)
        self.ui.refreshbutton.clicked.connect(self.LoadData)
        self.LoadData()
        self.ui.result.clear()
    
    def LoadData(self):        
        self.ui.goatList.clear()
        self.ui.goatList.setHorizontalHeaderLabels(("Keçi ID","Süt Miktarı (KG)","Tarih"))
        cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency")
        liste = cursor.fetchall()
        self.liste = liste
        self.ui.goatList.setRowCount(len(liste)) 
        for i in range(len(liste)):   
            cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][0]}'")
            self.ui.goatList.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
            self.ui.goatList.setItem(i,1,QtWidgets.QTableWidgetItem(str(liste[i][1])))
            self.ui.goatList.setItem(i,2,QtWidgets.QTableWidgetItem(liste[i][2]))
        self.ui.goatList.cellChanged.connect(self.Changing)
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        

    def AcceptClickControl(self):
        self.ui.result.setText("Kaydedildi")       

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()    
    def Checking(self):
        currentTextRow = self.ui.goatList.currentRow()
        currentText = self.ui.goatList.item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
    
    def Changing(self,row,column):
        try:
            changed_data = self.ui.goatList.item(row,column).text()
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{changed_data}'")
            try:    
                changed_data = cursor.fetchone()[0]
            except:
                pass    
            keci = self.ui.goatList.item(row,0).text()
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{keci}'")
            keci = cursor.fetchone()[0]
            previous_id = self.liste[row][0]
            previous_date = self.liste[row][2]
            if column == 0:
                cursor.execute(f"UPDATE milk_efficency SET keci_id = '{changed_data}' WHERE keci_id = '{previous_id}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency")
                self.liste = cursor.fetchall()
            elif column == 1:
                cursor.execute(f"UPDATE milk_efficency SET kilo = '{changed_data}' WHERE keci_id = '{previous_id}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency")
                self.liste = cursor.fetchall()
            elif column == 2:
                cursor.execute(f"UPDATE milk_efficency SET tarih = '{changed_data}' WHERE keci_id = '{previous_id}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency")
                self.liste = cursor.fetchall()        
            connection.commit()
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")

class KiloDuzenle(QtWidgets.QWidget):
    def __init__(self):
        super(KiloDuzenle, self).__init__()
        self.ui = Ui_KiloDuzenle()
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
        self.ui.goatList.setHorizontalHeaderLabels(("Keçi ID","Kütle (KG)","Tarih"))
        cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report")
        liste = cursor.fetchall()
        self.liste = liste
        self.ui.goatList.setRowCount(len(liste)) 
        for i in range(len(liste)):   
            cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][0]}'")
            self.ui.goatList.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
            self.ui.goatList.setItem(i,1,QtWidgets.QTableWidgetItem(str(liste[i][1])))
            self.ui.goatList.setItem(i,2,QtWidgets.QTableWidgetItem(liste[i][2]))
        self.ui.goatList.cellChanged.connect(self.Changing)
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        

    def AcceptClickControl(self):
        self.ui.result.setText("Kaydedildi")       

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()    
    def Checking(self):
        currentTextRow = self.ui.goatList.currentRow()
        currentText = self.ui.goatList.item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
    
    def Changing(self,row,column):
        try:
            changed_data = self.ui.goatList.item(row,column).text()
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{changed_data}'")
            try:    
                changed_data = cursor.fetchone()[0]
            except:
                pass    
            keci = self.ui.goatList.item(row,0).text()
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{keci}'")
            keci = cursor.fetchone()[0]
            previous_id = self.liste[row][0]
            previous_date = self.liste[row][2]
            if column == 0:
                cursor.execute(f"UPDATE weight_report SET keci_id = '{changed_data}' WHERE keci_id = '{previous_id}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report")
                self.liste = cursor.fetchall()
            elif column == 1:
                cursor.execute(f"UPDATE weight_report SET kilo = '{changed_data}' WHERE keci_id = '{previous_id}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report")
                self.liste = cursor.fetchall()
            elif column == 2:
                cursor.execute(f"UPDATE weight_report SET tarih = '{changed_data}' WHERE keci_id = '{previous_id}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report")
                self.liste = cursor.fetchall()
            
            connection.commit()
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")

class HastalikDuzenle(QtWidgets.QWidget):
    def __init__(self):
        super(HastalikDuzenle, self).__init__()
        self.ui = Ui_HastalikDuzenle()
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
        self.ui.goatList.setHorizontalHeaderLabels(("Keçi ID","Hastalık","Başlangıç Tarihi","Bitiş Tarihi"))
        cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report")
        liste = cursor.fetchall()
        self.liste = liste
        self.ui.goatList.setRowCount(len(liste)) 
        for i in range(len(liste)):   
            cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][0]}'")
            self.ui.goatList.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
            cursor.execute(f"SELECT sicks from sicks where ID = '{liste[i][1]}'")
            self.ui.goatList.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            self.ui.goatList.setItem(i,2,QtWidgets.QTableWidgetItem(liste[i][2]))
            self.ui.goatList.setItem(i,3,QtWidgets.QTableWidgetItem(liste[i][3]))
        self.ui.goatList.cellChanged.connect(self.Changing)
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        

    def AcceptClickControl(self):
        self.ui.result.setText("Kaydedildi")       

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()    
    def Checking(self):
        currentTextRow = self.ui.goatList.currentRow()
        currentText = self.ui.goatList.item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
    
    def Changing(self,row,column):
        changed_data = self.ui.goatList.item(row,column).text()
        cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{changed_data}'")
        try:    
            changed_data = cursor.fetchone()[0]
        except:
            pass    
        changed_sick = self.ui.goatList.item(row,column).text()
        cursor.execute(f"SELECT ID FROM sicks WHERE sicks = '{changed_sick}'")
        try:    
            changed_sick = cursor.fetchone()[0]
        except:
            pass   
        try:
            keci = self.ui.goatList.item(row,0).text()
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{keci}'")
            keci = cursor.fetchone()[0]
            sick = self.ui.goatList.item(row,1).text()
            cursor.execute(f"SELECT ID FROM sicks WHERE sicks = '{sick}'")
            previous_id = self.liste[row][0]
            previous_sick = self.liste[row][1]
            previous_date = self.liste[row][2]
            if column == 0:
                cursor.execute(f"UPDATE sick_report SET keci_id = '{changed_data}' WHERE keci_id = '{previous_id}' AND sick_id = '{previous_sick}' AND start_date = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report")
                self.liste = cursor.fetchall()
            elif column == 1:
                cursor.execute(f"UPDATE sick_report SET sick_id = '{changed_sick}' WHERE keci_id = '{previous_id}' AND sick_id = '{previous_sick}' AND start_date = '{previous_date}'")
                cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report")
                self.liste = cursor.fetchall()
            elif column == 2:
                cursor.execute(f"UPDATE sick_report SET start_date = '{changed_data}' WHERE keci_id = '{previous_id}' AND sick_id = '{previous_sick}' AND start_date = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report")
                self.liste = cursor.fetchall()
            elif column == 3:
                cursor.execute(f"UPDATE sick_report SET end_date = '{changed_data}' WHERE keci_id = '{previous_id}' AND sick_id = '{previous_sick}' AND start_date = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report")
                self.liste = cursor.fetchall()
            connection.commit()
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")
            
class AsiDuzenle(QtWidgets.QWidget):
    def __init__(self):
        super(AsiDuzenle, self).__init__()
        self.ui = Ui_AsiDuzenle()
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
        self.ui.goatList.setHorizontalHeaderLabels(("Keçi ID","Aşı","Tarih"))
        cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report")
        liste = cursor.fetchall()
        self.liste = liste
        self.ui.goatList.setRowCount(len(liste)) 
        for i in range(len(liste)):   
            cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][0]}'")
            self.ui.goatList.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
            cursor.execute(f"SELECT vaccines from vaccines where ID = '{liste[i][1]}'")
            self.ui.goatList.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            self.ui.goatList.setItem(i,2,QtWidgets.QTableWidgetItem(liste[i][2]))
        self.ui.goatList.cellChanged.connect(self.Changing)
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        

    def AcceptClickControl(self):
        self.ui.result.setText("Kaydedildi")       

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()    
    def Checking(self):
        currentTextRow = self.ui.goatList.currentRow()
        currentText = self.ui.goatList.item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))
    
    def Changing(self,row,column):
        changed_data = self.ui.goatList.item(row,column).text()
        cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{changed_data}'")
        try:    
            changed_data = cursor.fetchone()[0]
        except:
            pass
        changed_vaccine = self.ui.goatList.item(row,column).text()
        cursor.execute(f"SELECT ID FROM vaccines WHERE vaccines = '{changed_vaccine}'")
        try:    
            changed_vaccine = cursor.fetchone()[0]
        except:
            pass
        try:
            keci = self.ui.goatList.item(row,0).text()
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{keci}'")
            keci = cursor.fetchone()[0]              
            previous_id = self.liste[row][0]
            previous_vaccine = self.liste[row][1]
            previous_date = self.liste[row][2]
            if column == 0:
                cursor.execute(f"UPDATE vaccine_report SET keci_id = '{changed_data}' WHERE keci_id = '{previous_id}' AND asi_id = '{previous_vaccine}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report")
                self.liste = cursor.fetchall()
            elif column == 1:
                cursor.execute(f"UPDATE vaccine_report SET asi_id = '{changed_vaccine}' WHERE keci_id = '{previous_id}' AND asi_id = '{previous_vaccine}' AND tarih = '{previous_date}'")
                cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report")
                self.liste = cursor.fetchall()
            elif column == 2:
                cursor.execute(f"UPDATE vaccine_report SET tarih = '{changed_data}' WHERE keci_id = '{previous_id}' AND asi_id = '{previous_vaccine}' AND tarih = '{previous_date}' ")
                cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report")
                self.liste = cursor.fetchall()
            connection.commit()
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")