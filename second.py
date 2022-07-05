from PyQt5 import QtWidgets, QtCore, QtGui
import sys, os, shutil, sqlite3
from keciekle import Ui_KeciEkle
from addmenu import Ui_EkleMenu
from asimekle import Ui_AsimEkle
from sutekle import Ui_SutEkle
from agirlikekle import Ui_AgirlikEkle
from hastalikekle import Ui_HastalikEkle
from asiekle import Ui_AsiEkle
from dbconnection import cursor, connection
from datetime import date

class AddMenu(QtWidgets.QWidget):
    def __init__(self):
        super(AddMenu, self).__init__()
        self.ui = Ui_EkleMenu()
        self.ui.setupUi(self)
        self.ui.keciekle.clicked.connect(self.ClickControl)
        self.ui.asimekle.clicked.connect(self.ClickControl)
        self.ui.sutekle.clicked.connect(self.ClickControl)
        self.ui.kiloekle.clicked.connect(self.ClickControl)
        self.ui.hastalikekle.clicked.connect(self.ClickControl)
        self.ui.asiekle.clicked.connect(self.ClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.add_goat = KeciEkleme()
        self.add_asim = AsimEkleme()
        self.add_sut = SutVerimi()
        self.add_kilo = KiloBilgisi()
        self.add_sick = HastalikDurumu()
        self.add_asi = AsiDurumu()
    def ClickControl(self):
        sender = self.sender().text()
        if sender == "Keçi Ekle":
            self.add_goat.show()
            self.hide()
        elif sender == "Aşım Tarihi Ekle/Güncelle":
            self.add_asim.show()
            self.hide() 
        elif sender == "Süt Verimi Ekle":
            self.add_sut.show()
            self.hide() 
        elif sender == "Kilo Bilgisi Ekle":
            self.add_kilo.show()
            self.hide()
        elif sender == "Hastalık Durumu Ekle":
            self.add_sick.show()
            self.hide()
        elif sender == "Aşı Durumu Ekle":
            self.add_asi.show()
            self.hide()
    def ExitClickControl(self):
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.hide()
        win.show()

### Sub Classes ###        
class KeciEkleme(QtWidgets.QWidget):
    def __init__(self):
        super(KeciEkleme, self).__init__()
        self.ui = Ui_KeciEkle()
        self.ui.setupUi(self)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.gozat.clicked.connect(self.OpenChoosenPicture)
        self.ui.refreshbuton.clicked.connect(self.LoadData)
        self.ui.birthdate.setDate(date.today())
        self.LoadData()
        self.ui.result.clear()
    
    def LoadData(self):
        self.ui.kecituru.clear()
        cursor.execute("SELECT type FROM types")
        for i in cursor.fetchall():
            self.ui.kecituru.addItem(i[0])
            connection.commit()
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")

    def AcceptClickControl(self):
        try:
            sql = "INSERT INTO goats_table (keci_id,baba_id,anne_id,dogum_tarihi,cinsiyeti,cinsi) VALUES (?,?,?,?,?,?)"
            kimlik_no = str(self.ui.kimlikno.text())
            try:
                cursor.execute(f"SELECT id FROM goats_table where keci_id = '{self.ui.annekimlik.text()}'")
                anne_kimlik_no = int((cursor.fetchone()[0]))
                cursor.execute(f"SELECT id FROM goats_table where keci_id = '{self.ui.babakimlik.text()}'")
                baba_kimlik_no = int((cursor.fetchone()[0]))
            except:
                anne_kimlik_no = None
                baba_kimlik_no = None
            dogum_tarihi = self.ui.birthdate.date()
            dogum_tarihi = str(dogum_tarihi.toString(QtCore.Qt.ISODate))
            if self.ui.disi.isChecked():
                cinsiyet = "D"
            elif self.ui.erkek.isChecked():
                cinsiyet = "E"    
            chosen_type = self.ui.kecituru.currentText() 
            cursor.execute(f"SELECT ID FROM types WHERE type = '{chosen_type}'")
            keci_turu = int(cursor.fetchone()[0])
            values = (kimlik_no,baba_kimlik_no,anne_kimlik_no,dogum_tarihi,cinsiyet,keci_turu)
            cursor.execute(sql,values)
            connection.commit() 
            path = self.fileName
            uzanti = path.split(".")
            try:
                os.mkdir("Goat_Pictures")
            except:
                pass
            shutil.copy(path,f"Goat_Pictures/{kimlik_no}.{uzanti[1]}")
            self.ui.result.setText("İşlem Başarılı!\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklendi!")
        except Exception as err:
            print(err)
            self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!") 

    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()
    def OpenChoosenPicture(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open Image File","C:","Image Files (*.png *.jpg *.ico)", options=options)
        self.ui.goatshow.setPixmap(QtGui.QPixmap(fileName))
        self.fileName = fileName

class AsimEkleme(QtWidgets.QWidget):
    def __init__(self):
        super(AsimEkleme, self).__init__()
        self.ui = Ui_AsimEkle()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.asimdate.setDate(date.today())
    def AcceptClickControl(self):
        try:
            kimlik_no = str(self.ui.kimlikno.text())
            asim_tarihi = self.ui.asimdate.date()
            asim_tarihi = str(asim_tarihi.toString(QtCore.Qt.ISODate))
            sql = f"UPDATE goats_table SET asim_zamani = '{asim_tarihi}' WHERE keci_id = '{kimlik_no}' "
            cursor.execute(sql)
            connection.commit()
            if cursor.rowcount == 0:
                self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
            else:
                self.ui.result.setText("İşlem Başarılı!\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklendi!")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()    

class SutVerimi(QtWidgets.QWidget):
    def __init__(self):
        super(SutVerimi, self).__init__()
        self.ui = Ui_SutEkle()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.sutdate.setDate(date.today())
    def AcceptClickControl(self):
        try:
            kimlik_no = str(self.ui.kimlikno.text())
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{kimlik_no}'")
            kimlik_id = cursor.fetchone()[0]
            sut_miktari = float(self.ui.sutmiktar.text())
            sut_tarihi = self.ui.sutdate.date()
            sut_tarihi = str(sut_tarihi.toString(QtCore.Qt.ISODate))
            sql = f"INSERT INTO milk_efficency (keci_id,kilo,tarih) VALUES ('{kimlik_id}','{sut_miktari}','{sut_tarihi}')"
            cursor.execute(sql)
            connection.commit()
            if cursor.rowcount == 0:
                self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
            else:
                self.ui.result.setText("İşlem Başarılı!\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklendi!")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()        

class KiloBilgisi(QtWidgets.QWidget):
    def __init__(self):
        super(KiloBilgisi, self).__init__()
        self.ui = Ui_AgirlikEkle()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.agirlikdate.setDate(date.today())
    def AcceptClickControl(self):
        try:
            kimlik_no = str(self.ui.kimlikno.text())
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{kimlik_no}'")
            kimlik_id = cursor.fetchone()[0]
            agirlik = float(self.ui.agirlik.text())
            agirliktarihi = self.ui.agirlikdate.date()
            agirliktarihi = str(agirliktarihi.toString(QtCore.Qt.ISODate))
            sql = f"INSERT INTO weight_report (keci_id,kilo,tarih) VALUES ('{kimlik_id}','{agirlik}','{agirliktarihi}')"
            cursor.execute(sql)
            connection.commit()
            if cursor.rowcount == 0:
                self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
            else:
                self.ui.result.setText("İşlem Başarılı!\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklendi!")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()        

class HastalikDurumu(QtWidgets.QWidget):
    def __init__(self):
        super(HastalikDurumu, self).__init__()
        self.ui = Ui_HastalikEkle()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.refreshbuton.clicked.connect(self.LoadData)
        self.ui.hastalikdate.setDate(date.today())
        self.LoadData()
        self.ui.result.clear()
    
    def LoadData(self):
        self.ui.hastaliklar.clear()
        cursor.execute("SELECT sicks FROM sicks")
        for i in cursor.fetchall():
            self.ui.hastaliklar.addItem(i[0])
            connection.commit() 
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
          
    def AcceptClickControl(self):
        try:
            kimlik_no = str(self.ui.kimlikno.text())
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{kimlik_no}'")
            kimlik_id = cursor.fetchone()[0]
            chosen_sick = self.ui.hastaliklar.currentText() 
            cursor.execute(f"SELECT ID FROM sicks WHERE sicks = '{chosen_sick}'")
            chosen_sick = int(cursor.fetchone()[0])
            baslangictarihi = self.ui.hastalikdate.date()
            baslangictarihi = str(baslangictarihi.toString(QtCore.Qt.ISODate))
            cursor.execute(f"INSERT INTO sick_report (keci_id, sick_id, start_date) VALUES ('{kimlik_id}','{chosen_sick}','{baslangictarihi}')")
            connection.commit()
            if cursor.rowcount == 0:
                self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
            else:
                self.ui.result.setText("İşlem Başarılı!\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklendi!")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()            

class AsiDurumu(QtWidgets.QWidget):
    def __init__(self):
        super(AsiDurumu, self).__init__()
        self.ui = Ui_AsiEkle()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)        
        self.ui.refreshbuton.clicked.connect(self.LoadData)
        self.ui.asidate.setDate(date.today())
        self.LoadData()
        self.ui.result.clear()
    
    def LoadData(self):
        self.ui.asilar.clear()
        cursor.execute("SELECT vaccines FROM vaccines")
        for i in cursor.fetchall():
            self.ui.asilar.addItem(i[0])
        self.ui.result.setText("Veriler Veritabanından Yüklendi!")
        
    def AcceptClickControl(self):
        try:
            kimlik_no = str(self.ui.kimlikno.text())
            cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id = '{kimlik_no}'")
            kimlik_id = cursor.fetchone()[0]
            chosen_vaccine = self.ui.asilar.currentText() 
            cursor.execute(f"SELECT ID FROM vaccines WHERE vaccines = '{chosen_vaccine}'")
            chosen_vaccine = int(cursor.fetchone()[0])
            asitarihi = self.ui.asidate.date()
            asitarihi = str(asitarihi.toString(QtCore.Qt.ISODate))
            cursor.execute(f"INSERT INTO vaccine_report (keci_id, asi_id, tarih) VALUES ('{kimlik_id}','{chosen_vaccine}','{asitarihi}')")
            connection.commit()
            if cursor.rowcount == 0:
                self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
            else:
                self.ui.result.setText("İşlem Başarılı!\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklendi!")
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**\n"+kimlik_no+" ID Numaralı Keçi\nDatabase'e Eklenemedi!")
            
    def ExitClickControl(self):
        connection.close()
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.close()
        win.show()                  