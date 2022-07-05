from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from reportmenu import Ui_RaporlaMenu
import sqlite3
from dbconnection import cursor
import time

class ReportMenu(QtWidgets.QWidget):
    def __init__(self):
        super(ReportMenu, self).__init__()
        self.ui = Ui_RaporlaMenu()
        self.ui.setupUi(self)
        self.ui.mainmenubuton.clicked.connect(self.MainClickControl)
        self.ui.exitbuton.clicked.connect(self.ExitClickControl)
        self.ui.acceptbuton.clicked.connect(self.AcceptClickControl)
        self.ui.goats.itemSelectionChanged.connect(self.Checking)
        self.ui.vaccines.itemSelectionChanged.connect(self.Checking)
        self.ui.sicks.itemSelectionChanged.connect(self.Checking)
        self.ui.milk.itemSelectionChanged.connect(self.Checking)
        self.ui.weight.itemSelectionChanged.connect(self.Checking)
        self.ui.deleted.itemSelectionChanged.connect(self.Checking)
        self.ui.filterbuton.clicked.connect(self.Filter)
        self.ui.tabWidget.currentChanged.connect(self.FilterCombo)
        self.ui.columns.currentIndexChanged.connect(self.EnableDisable)
        itemler = []
        for i in range(7):            
            itemler.append(self.ui.goats.horizontalHeaderItem(i).text())
        self.ui.columns.addItems(itemler)
        ######################################################################################
        self.ui.refreshbuton.clicked.connect(self.LoadData)
        self.LoadData()
        self.ui.result.clear()

    def LoadData(self):
        self.DataScreen()
        self.ui.goats.clear()
        self.ui.vaccines.clear()
        self.ui.sicks.clear()
        self.ui.milk.clear()
        self.ui.weight.clear()
        self.ui.deleted.clear()
        self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
        self.ui.vaccines.setHorizontalHeaderLabels(("Keçi ID","Aşı","Tarih"))
        self.ui.sicks.setHorizontalHeaderLabels(("Keçi ID","Hastalık","Başlangıç Tarihi","Bitiş Tarihi"))
        self.ui.milk.setHorizontalHeaderLabels(("Keçi ID","Miktar (KG)","Tarih"))
        self.ui.weight.setHorizontalHeaderLabels(("Keçi ID","Kütle (KG)","Tarih"))
        self.ui.deleted.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı","Silinme Sebebi","Silinme Tarihi"))
        cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table")
        liste = cursor.fetchall()
        self.liste = liste
        self.ui.goats.setRowCount(len(liste))
        for i in range(len(liste)):   
            self.ui.goats.setItem(i,0,QtWidgets.QTableWidgetItem(str(liste[i][0])))
            try:
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][1]}'")
                self.ui.goats.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            except:
                pass 
            try:   
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][2]}'")
                self.ui.goats.setItem(i,2,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            except:
                pass
            try:
                cursor.execute(f"SELECT type from types where ID = '{liste[i][5]}'")            
                self.ui.goats.setItem(i,5,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
            except:
                pass
            try:
                self.ui.goats.setItem(i,3,QtWidgets.QTableWidgetItem(str(liste[i][3])))
                self.ui.goats.setItem(i,4,QtWidgets.QTableWidgetItem(str(liste[i][4])))            
                self.ui.goats.setItem(i,6,QtWidgets.QTableWidgetItem(str(liste[i][6])))
            except Exception as er:
                print(er)
                self.ui.result.setText("**HATA**")
        ######################################################################################
        try:    
            cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report")
            liste1 = cursor.fetchall()
            self.liste1 = liste1
            self.ui.vaccines.setRowCount(len(liste1)) 
            for i in range(len(liste1)):   
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste1[i][0]}'")
                self.ui.vaccines.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                cursor.execute(f"SELECT vaccines from vaccines where ID = '{liste1[i][1]}'")
                self.ui.vaccines.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                self.ui.vaccines.setItem(i,2,QtWidgets.QTableWidgetItem(liste1[i][2]))
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")
        ######################################################################################
        try:
            cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report")
            liste2 = cursor.fetchall()
            self.liste2 = liste2
            self.ui.sicks.setRowCount(len(liste2)) 
            for i in range(len(liste2)):   
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste2[i][0]}'")
                self.ui.sicks.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                cursor.execute(f"SELECT sicks from sicks where ID = '{liste2[i][1]}'")
                self.ui.sicks.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                self.ui.sicks.setItem(i,2,QtWidgets.QTableWidgetItem(liste2[i][2]))
                self.ui.sicks.setItem(i,3,QtWidgets.QTableWidgetItem(liste2[i][3]))
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")
        ######################################################################################
        try: 
            cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency")
            liste3 = cursor.fetchall()
            self.liste3 = liste3
            self.ui.milk.setRowCount(len(liste3)) 
            for i in range(len(liste3)):   
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste3[i][0]}'")
                self.ui.milk.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                self.ui.milk.setItem(i,1,QtWidgets.QTableWidgetItem(str(liste3[i][1])))
                self.ui.milk.setItem(i,2,QtWidgets.QTableWidgetItem(liste3[i][2]))
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")
        ######################################################################################
        try:
            cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report")
            liste4 = cursor.fetchall()
            self.liste4 = liste4
            self.ui.weight.setRowCount(len(liste4)) 
            for i in range(len(liste4)):   
                cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste4[i][0]}'")
                self.ui.weight.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                self.ui.weight.setItem(i,1,QtWidgets.QTableWidgetItem(str(liste4[i][1])))
                self.ui.weight.setItem(i,2,QtWidgets.QTableWidgetItem(liste4[i][2]))
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")
        ######################################################################################
        try:
            cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats")
            liste5 = cursor.fetchall()
            self.liste5 = liste5
            self.ui.deleted.setRowCount(len(liste5))
            for i in range(len(liste5)):   
                self.ui.deleted.setItem(i,0,QtWidgets.QTableWidgetItem(str(liste5[i][0])))
                try:
                    cursor.execute(f"SELECT keci_id from deleted_goats where ID = '{liste5[i][1]}'")
                    self.ui.deleted.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                except:
                    pass 
                try:   
                    cursor.execute(f"SELECT keci_id from deleted_goats where ID = '{liste5[i][2]}'")
                    self.ui.deleted.setItem(i,2,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                except:
                    pass
                try:
                    cursor.execute(f"SELECT type from types where ID = '{liste5[i][5]}'")            
                    self.ui.deleted.setItem(i,5,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                except:
                    pass
                self.ui.deleted.setItem(i,3,QtWidgets.QTableWidgetItem(str(liste5[i][3])))
                self.ui.deleted.setItem(i,4,QtWidgets.QTableWidgetItem(str(liste5[i][4])))            
                self.ui.deleted.setItem(i,6,QtWidgets.QTableWidgetItem(str(liste5[i][6])))
                self.ui.deleted.setItem(i,7,QtWidgets.QTableWidgetItem(str(liste5[i][7])))
                self.ui.deleted.setItem(i,8,QtWidgets.QTableWidgetItem(str(liste5[i][8])))
        except Exception as er:
            print(er)
            self.ui.result.setText("**HATA**")
        ######################################################################################
        self.ui.result.setText("Veriler Yüklendi!")
    def Filter(self):
        text = self.ui.filtertext.text()
        combo = self.ui.columns.currentText()
        firstDate = self.ui.firstDate.date()
        firstDate = str(firstDate.toString(QtCore.Qt.ISODate))
        lastDate = self.ui.secondDate.date()
        lastDate = str(lastDate.toString(QtCore.Qt.ISODate))
        currentTab = self.ui.tabWidget.currentIndex()
        ########## Filtering and Loading Data ##########
        if currentTab == 0:            
            if combo == "Keçi ID":
                filterName = "keci_id"
                sorgu = f"LIKE '%{text}%'"
                self.ui.goats.clear()        
                self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}")
                liste = cursor.fetchall()
                self.liste = liste
            elif combo == "Baba ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste = []
                self.liste = liste   
                filterName = "baba_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}")
                    try:
                        liste.append(cursor.fetchone())
                    except:
                        pass
                self.ui.goats.clear()        
                self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
                for i in range(len(liste)):
                    try:
                        x = liste.index(None)
                        liste.pop(x)
                    except:
                        pass               
            elif combo == "Anne ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste = []
                self.liste = liste   
                filterName = "anne_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}")
                    try:
                        liste.append(cursor.fetchone())
                    except:
                        pass
                self.ui.goats.clear()        
                self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
                for i in range(len(liste)):
                    try:
                        x = liste.index(None)
                        liste.pop(x)
                    except:
                        pass               
            elif combo == "Doğum Tarihi":
                liste = []
                self.liste = liste
                filterName = "dogum_tarihi"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"    
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}")   
                liste = cursor.fetchall()
            elif combo == "Cinsiyeti":
                liste = []
                self.liste = liste
                filterName = "cinsiyeti" 
                sorgu = f"LIKE '%{text}%'"         
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}") 
                liste = cursor.fetchall()      
            elif combo == "Cinsi":
                cursor.execute(f"SELECT ID FROM types WHERE type LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste = []
                self.liste = liste   
                filterName = "cinsi"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}")
                    try:
                        baselist = cursor.fetchall()
                        for q in baselist:
                            liste.append(q)
                    except:
                        pass
                self.ui.goats.clear()        
                self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
                for i in range(len(liste)):
                    try:
                        x = liste.index(None)
                        liste.pop(x)
                    except:
                        pass 
            elif combo == "Aşım Zamanı":
                liste = []
                self.liste = liste
                filterName = "asim_zamani"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"   
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani FROM goats_table WHERE {filterName} {sorgu}") 
                liste = cursor.fetchall()    
            self.ui.goats.setRowCount(len(liste))
            for i in range(len(liste)):   
                try:
                    self.ui.goats.setItem(i,0,QtWidgets.QTableWidgetItem(str(liste[i][0])))
                except:
                    pass
                try:
                    cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][1]}'")
                    self.ui.goats.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                except:
                    pass 
                try:   
                    cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste[i][2]}'")
                    self.ui.goats.setItem(i,2,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                except:
                    pass
                try:
                    cursor.execute(f"SELECT type from types where ID = '{liste[i][5]}'")            
                    self.ui.goats.setItem(i,5,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                except:
                    pass
                try:
                    self.ui.goats.setItem(i,3,QtWidgets.QTableWidgetItem(str(liste[i][3])))
                    self.ui.goats.setItem(i,4,QtWidgets.QTableWidgetItem(str(liste[i][4])))            
                    self.ui.goats.setItem(i,6,QtWidgets.QTableWidgetItem(str(liste[i][6])))
                except Exception as er:
                    print(er)
                    self.ui.result.setText("**HATA**")
                    self.LoadData()       
        elif currentTab == 1:
            try:
                if combo == "Keçi ID":
                    cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                    text_id = cursor.fetchall()
                    text_id_list = []
                    for i in range(len(text_id)):
                        text_id_list.append(text_id[i][0])
                    liste1 = []
                    self.liste1 = liste1  
                    filterName = "keci_id"
                    for i in range(len(text_id_list)):
                        sorgu = f"= {text_id_list[i]}"   
                        cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report WHERE {filterName} {sorgu}")
                        try:
                            baselist = cursor.fetchall()
                            for q in baselist:
                                liste1.append(q)
                        except:
                            pass
                    for i in range(len(liste1)):
                        try:
                            x = liste1.index(None)
                            liste1.pop(x)
                        except:
                            pass
                elif combo == "Aşı":
                    cursor.execute(f"SELECT ID FROM vaccines WHERE vaccines LIKE '%{text}%'")
                    text_id = cursor.fetchall()
                    text_id_list = []
                    for i in range(len(text_id)):
                        text_id_list.append(text_id[i][0])
                    liste1 = []
                    self.liste1 = liste1  
                    filterName = "asi_id"
                    for i in range(len(text_id_list)):
                        sorgu = f"= {text_id_list[i]}"   
                        cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report WHERE {filterName} {sorgu}")
                        try:
                            baselist = cursor.fetchall()
                            for q in baselist:
                                liste1.append(q)
                        except:
                            pass
                    for i in range(len(liste1)):
                        try:
                            x = liste1.index(None)
                            liste1.pop(x)
                        except:
                            pass               
                elif combo == "Tarih":
                    liste1 = []
                    self.liste1 = liste1
                    filterName = "tarih"
                    sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"  
                    cursor.execute(f"SELECT keci_id, asi_id, tarih FROM vaccine_report WHERE {filterName} {sorgu}")
                    liste1 = cursor.fetchall() 
                
                self.ui.vaccines.clear()      
                self.ui.vaccines.setHorizontalHeaderLabels(("Keçi ID","Aşı","Tarih")) 
                self.ui.vaccines.setRowCount(len(liste1)) 
                for i in range(len(liste1)):   
                    cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste1[i][0]}'")
                    self.ui.vaccines.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                    cursor.execute(f"SELECT vaccines from vaccines where ID = '{liste1[i][1]}'")
                    self.ui.vaccines.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                    self.ui.vaccines.setItem(i,2,QtWidgets.QTableWidgetItem(liste1[i][2]))
            except Exception as err:
                print(err)
                self.ui.result.setText("**HATA**")
                self.LoadData()                  
        elif currentTab == 2:
            if combo == "Keçi ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste2 = []
                self.liste2 = liste2 
                filterName = "keci_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report WHERE {filterName} {sorgu}")
                    try:
                        baselist = cursor.fetchall()
                        for q in baselist:
                            liste2.append(q)
                    except:
                        pass
                for i in range(len(liste2)):
                    try:
                        x = liste2.index(None)
                        liste2.pop(x)
                    except:
                        pass
            elif combo == "Hastalık":
                cursor.execute(f"SELECT ID FROM sicks WHERE sicks LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste2 = []
                self.liste2 = liste2  
                filterName = "sick_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report WHERE {filterName} {sorgu}")
                    try:
                        baselist = cursor.fetchall()
                        for q in baselist:
                            liste2.append(q)
                    except:
                        pass
                for i in range(len(liste2)):
                    try:
                        x = liste2.index(None)
                        liste2.pop(x)
                    except:
                        pass               
            elif combo == "Başlangıç Tarihi":
                liste2 = []
                self.liste2 = liste2
                filterName = "start_date"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"  
                cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report WHERE {filterName} {sorgu}")
                liste2 = cursor.fetchall() 
            elif combo == "Bitiş Tarihi":
                liste2 = []
                self.liste2 = liste2
                filterName = "end_date"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"  
                cursor.execute(f"SELECT keci_id, sick_id, start_date, end_date FROM sick_report WHERE {filterName} {sorgu}")
                liste2 = cursor.fetchall()

            try:
                self.ui.sicks.clear() 
                self.ui.sicks.setRowCount(len(liste2)) 
                self.ui.sicks.setHorizontalHeaderLabels(("Keçi ID","Hastalık","Başlangıç Tarihi","Bitiş Tarihi")) 
                for i in range(len(liste2)):   
                    cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste2[i][0]}'")
                    self.ui.sicks.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                    cursor.execute(f"SELECT sicks from sicks where ID = '{liste2[i][1]}'")
                    self.ui.sicks.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                    self.ui.sicks.setItem(i,2,QtWidgets.QTableWidgetItem(liste2[i][2]))
                    self.ui.sicks.setItem(i,3,QtWidgets.QTableWidgetItem(liste2[i][3]))                
            except Exception as er:
                print(er)
                self.ui.result.setText("**HATA**")
        elif currentTab == 3:
            if combo == "Keçi ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste3 = []
                self.liste3 = liste3
                filterName = "keci_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency WHERE {filterName} {sorgu}")
                    try:
                        baselist = cursor.fetchall()
                        for q in baselist:
                            liste3.append(q)
                    except:
                        pass
                for i in range(len(liste3)):
                    try:
                        x = liste3.index(None)
                        liste3.pop(x)
                    except:
                        pass
            elif combo == "Miktar (KG)":
                liste3 = []
                self.liste3 = liste3
                filterName = "kilo"
                sorgu = f" > {text}"
                try:
                    cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency WHERE {filterName} {sorgu}")
                    liste3 = cursor.fetchall()
                except:
                    pass
            elif combo == "Tarih":
                liste3 = []
                self.liste3 = liste3
                filterName = "tarih"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"  
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM milk_efficency WHERE {filterName} {sorgu}")
                liste3 = cursor.fetchall()
            try:
                self.ui.milk.clear() 
                self.ui.milk.setRowCount(len(liste3)) 
                for i in range(len(liste3)):   
                    cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste3[i][0]}'")
                    self.ui.milk.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                    self.ui.milk.setItem(i,1,QtWidgets.QTableWidgetItem(str(liste3[i][1])))
                    self.ui.milk.setItem(i,2,QtWidgets.QTableWidgetItem(liste3[i][2]))
            except Exception as er:
                print(er)
                self.ui.result.setText("**HATA**")
            self.ui.milk.setHorizontalHeaderLabels(("Keçi ID","Miktar (KG)","Tarih"))
        elif currentTab == 4:
            if combo == "Keçi ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste4 = []
                self.liste4 = liste4
                filterName = "keci_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report WHERE {filterName} {sorgu}")
                    try:
                        baselist = cursor.fetchall()
                        for q in baselist:
                            liste4.append(q)
                    except:
                        pass
                for i in range(len(liste4)):
                    try:
                        x = liste4.index(None)
                        liste4.pop(x)
                    except:
                        pass
            elif combo == "Kütle (KG)":
                liste4 = []
                self.liste4 = liste4
                filterName = "kilo"
                sorgu = f" > {text}"
                try:
                    cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report WHERE {filterName} {sorgu}")
                    liste4 = cursor.fetchall()
                except:
                    pass
            elif combo == "Tarih":
                liste4 = []
                self.liste4 = liste4
                filterName = "tarih"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"  
                cursor.execute(f"SELECT keci_id, kilo, tarih FROM weight_report WHERE {filterName} {sorgu}")
                liste4 = cursor.fetchall()
            try:
                self.ui.weight.clear()
                self.ui.weight.setHorizontalHeaderLabels(("Keçi ID","Kütle (KG)","Tarih"))
                self.ui.weight.setRowCount(len(liste4)) 
                for i in range(len(liste4)):   
                    cursor.execute(f"SELECT keci_id from goats_table where ID = '{liste4[i][0]}'")
                    self.ui.weight.setItem(i,0,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))  
                    self.ui.weight.setItem(i,1,QtWidgets.QTableWidgetItem(str(liste4[i][1])))
                    self.ui.weight.setItem(i,2,QtWidgets.QTableWidgetItem(liste4[i][2]))
            except Exception as er:
                print(er)
                self.ui.result.setText("**HATA**")    
        elif currentTab == 5:
            if combo == "Keçi ID":
                filterName = "keci_id"
                sorgu = f"LIKE '%{text}%'"
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}") 
                liste5 = cursor.fetchall()
                self.liste5 = liste5
            elif combo == "Baba ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste5 = []
                self.liste5 = liste5   
                filterName = "baba_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}") 
                    try:
                        liste5.append(cursor.fetchone())
                    except:
                        pass
                self.ui.goats.clear()        
                self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı"))
                for i in range(len(liste5)):
                    try:
                        x = liste5.index(None)
                        liste5.pop(x)
                    except:
                        pass               
            elif combo == "Anne ID":
                cursor.execute(f"SELECT ID FROM goats_table WHERE keci_id LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste5 = []
                self.liste5 = liste5   
                filterName = "anne_id"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}") 
                    try:
                        liste5.append(cursor.fetchone())
                    except:
                        pass
                for i in range(len(liste5)):
                    try:
                        x = liste5.index(None)
                        liste5.pop(x)
                    except:
                        pass               
            elif combo == "Doğum Tarihi":
                liste5 = []
                self.liste5 = liste5
                filterName = "dogum_tarihi"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"    
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}")    
                liste5 = cursor.fetchall()
            elif combo == "Cinsiyeti":
                liste5 = []
                self.liste5 = liste5
                filterName = "cinsiyeti" 
                sorgu = f"LIKE '%{text}%'"         
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}") 
                liste5 = cursor.fetchall()      
            elif combo == "Cinsi":
                cursor.execute(f"SELECT ID FROM types WHERE type LIKE '%{text}%'")
                text_id = cursor.fetchall()
                text_id_list = []
                for i in range(len(text_id)):
                    text_id_list.append(text_id[i][0])
                liste5 = []
                self.liste5 = liste5   
                filterName = "cinsi"
                for i in range(len(text_id_list)):
                    sorgu = f"= {text_id_list[i]}"   
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}") 
                    try:
                        baselist = cursor.fetchall()
                        for q in baselist:
                            liste5.append(q)
                    except:
                        pass
                for i in range(len(liste5)):
                    try:
                        x = liste5.index(None)
                        liste5.pop(x)
                    except:
                        pass 
            elif combo == "Aşım Zamanı":
                liste5 = []
                self.liste5 = liste5
                filterName = "asim_zamani"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"   
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}") 
                liste5 = cursor.fetchall()
            elif combo == "Silinme Sebebi":
                liste5 = []
                self.liste5 = liste5
                filterName = "delete_reason"
                sorgu = f" LIKE '%{text}%'"
                try:
                    cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}")
                    liste5 = cursor.fetchall()
                except:
                    pass
            elif combo == "Silinme Tarihi":
                liste5 = []
                self.liste5 = liste5
                filterName = "delete_date"
                sorgu = f" BETWEEN '{firstDate}' AND '{lastDate}'"    
                cursor.execute(f"SELECT keci_id, baba_id, anne_id, dogum_tarihi, cinsiyeti, cinsi, asim_zamani, delete_reason, delete_date FROM deleted_goats WHERE {filterName} {sorgu}")    
                liste5 = cursor.fetchall()
            try:
                self.ui.goats.clear()        
                self.ui.goats.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı", "Silinme Sebebi","Silinme Tarihi"))
                self.liste5 = liste5
                self.ui.deleted.setRowCount(len(liste5))
                for i in range(len(liste5)):   
                    self.ui.deleted.setItem(i,0,QtWidgets.QTableWidgetItem(str(liste5[i][0])))
                    try:
                        cursor.execute(f"SELECT keci_id from deleted_goats where ID = '{liste5[i][1]}'")
                        self.ui.deleted.setItem(i,1,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                    except:
                        pass 
                    try:   
                        cursor.execute(f"SELECT keci_id from deleted_goats where ID = '{liste5[i][2]}'")
                        self.ui.deleted.setItem(i,2,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                    except:
                        pass
                    try:
                        cursor.execute(f"SELECT type from types where ID = '{liste5[i][5]}'")            
                        self.ui.deleted.setItem(i,5,QtWidgets.QTableWidgetItem(cursor.fetchone()[0]))
                    except:
                        pass
                    self.ui.deleted.setItem(i,3,QtWidgets.QTableWidgetItem(str(liste5[i][3])))
                    self.ui.deleted.setItem(i,4,QtWidgets.QTableWidgetItem(str(liste5[i][4])))            
                    self.ui.deleted.setItem(i,6,QtWidgets.QTableWidgetItem(str(liste5[i][6])))
                    self.ui.deleted.setItem(i,7,QtWidgets.QTableWidgetItem(str(liste5[i][7])))
                    self.ui.deleted.setItem(i,8,QtWidgets.QTableWidgetItem(str(liste5[i][8])))
            except Exception as er:
                print(er)
                self.ui.result.setText("**HATA**")
                self.ui.deleted.setHorizontalHeaderLabels(("Keçi ID","Baba ID","Anne ID","Doğum Tarihi","Cinsiyeti","Cinsi","Aşım Zamanı","Silinme Sebebi","Silinme Tarihi"))
        ########## Filtering and Loading Data ##########

    def Checking(self):
        currentTextRow = self.sender().currentRow()
        currentText = self.sender().item(currentTextRow,0).text()
        self.ui.goatshow.setPixmap(QtGui.QPixmap(f"Goat_Pictures/{currentText}"))

    def AcceptClickControl(self):
        pass

    def ExitClickControl(self):
        sys.exit()
    def MainClickControl(self):
        from main import win
        self.hide()
        win.show()

    def FilterCombo(self):
        self.ui.columns.clear()
        currentTab = self.ui.tabWidget.currentIndex()
        if currentTab == 0:
            itemler = []
            for i in range(7):            
                itemler.append(self.ui.goats.horizontalHeaderItem(i).text())
            self.ui.columns.addItems(itemler)
        elif currentTab == 1:
            itemler = []
            for i in range(3):            
                itemler.append(self.ui.vaccines.horizontalHeaderItem(i).text())
            self.ui.columns.addItems(itemler)
        elif currentTab == 2:
            itemler = []
            for i in range(4):            
                itemler.append(self.ui.sicks.horizontalHeaderItem(i).text())
            self.ui.columns.addItems(itemler)
        elif currentTab == 3:
            itemler = []
            for i in range(3):            
                itemler.append(self.ui.milk.horizontalHeaderItem(i).text())
            self.ui.columns.addItems(itemler)
        elif currentTab == 4:
            itemler = []
            for i in range(3):            
                itemler.append(self.ui.weight.horizontalHeaderItem(i).text())
            self.ui.columns.addItems(itemler)
        elif currentTab == 5:
            itemler = []
            for i in range(9):            
                itemler.append(self.ui.deleted.horizontalHeaderItem(i).text())
            self.ui.columns.addItems(itemler)

    def EnableDisable(self,index):
        sender = self.sender().currentText()
        if sender == "Doğum Tarihi" or sender == "Aşım Zamanı" or sender == "Tarih" or sender =="Başlangıç Tarihi" or sender == "Bitiş Tarihi" or sender == "Silinme Tarihi":
            self.ui.filtertext.setDisabled(True)
            self.ui.firstDate.setDisabled(False)
            self.ui.secondDate.setDisabled(False)
        else:
            self.ui.filtertext.setDisabled(False)
            self.ui.firstDate.setDisabled(True)
            self.ui.secondDate.setDisabled(True)

    def DataScreen(self):
        try:
            cursor.execute("SELECT COUNT(*) FROM goats_table")
            variable1 = str(cursor.fetchone()[0])
            self.ui.keci_sayisi.setText(variable1)
            cursor.execute("SELECT COUNT(*) FROM goats_table WHERE cinsiyeti = 'E'")
            variable2 = str(cursor.fetchone()[0])
            cursor.execute("SELECT COUNT(*) FROM goats_table WHERE cinsiyeti = 'D'")
            variable3 = str(cursor.fetchone()[0])
            self.ui.erkekdisi_orani.setText(variable2+"/"+variable3)
            cursor.execute("SELECT COUNT(ID), cinsi FROM goats_table GROUP BY cinsi")
            variable4 = cursor.fetchall()
            temp = []
            for i in variable4:
                temp.append(i[0])
            temp.sort()
            for q in variable4:
                if q[0] == temp[-1]:
                    variable5 = q[1]
            cursor.execute(f"SELECT type FROM types WHERE ID = '{variable5}'")
            self.ui.cogunluk_cinsi.setText(cursor.fetchone()[0])
        except:
            pass
