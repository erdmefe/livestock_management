from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from mainmenu import Ui_AnaMenu

#Ana Menü İçin Sınıf Oluşturuduk
class Ui(QtWidgets.QMainWindow): 
    switch_window = QtCore.pyqtSignal(str)
    #Qt designerden gelen sınıfa bağlantı
    def __init__(self): 
        super(Ui, self).__init__()
        self.ui = Ui_AnaMenu()
        self.ui.setupUi(self)
        #Tıklanan Butonlara Fonksiyon Atadık
        self.ui.eklebuton.clicked.connect(self.ClickControl)
        self.ui.cikisbuton.clicked.connect(self.ClickControl)
        self.ui.duzenlebuton.clicked.connect(self.ClickControl)
        self.ui.silbuton.clicked.connect(self.ClickControl)
        self.ui.tanimlabuton.clicked.connect(self.ClickControl)
        self.ui.raporlabuton.clicked.connect(self.ClickControl)
        #loop error aldığımız için diğer sayfalardaki pencere sınıflarını burda ekledik
        from second import AddMenu
        from third import DelMenu
        from fourth import EditMenu
        from fifth import ReportMenu
        from sixth import DescMenu
        #ana sayfadan geçilecek pencere objeleri oluşturduk
        self.add_menu = AddMenu()
        self.del_menu = DelMenu()
        self.edit_menu = EditMenu()
        self.report_menu = ReportMenu()
        self.desc_menu = DescMenu()
    #Hangi tuşa basıldığını kontrol edip işlem yapan fonksiyon    
    def ClickControl(self):
        sender = self.sender().text()
        if sender == "EKLE":
            self.add_menu.show()
            self.hide()
        elif sender == "SİL":
            self.del_menu.show()
            self.hide()
        elif sender == "DÜZENLE":
            self.edit_menu.show()
            self.hide()
        elif sender == "RAPORLA":
            self.report_menu.show()
            self.hide()
        elif sender == "TANIMLA":
            self.desc_menu.show()
            self.hide() 
        elif sender == "ÇIKIŞ":
            sys.exit()
#Uygulamanın başlatılması için gerekli işlemler
app = QtWidgets.QApplication(sys.argv)
win = Ui()
#Diğer modüllerden bu modüle her ulaştığında çalışmasın diye if bloğuna aldık
if __name__ == '__main__':
    win.show()
    sys.exit(app.exec_())