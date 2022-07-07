from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import urllib.request
import os
from os import path
import pafy
import humanize
import webbrowser
FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))
class MainApp(QMainWindow , FORM_CLASS):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Buttons()
    def Handel_Ui(self):
        self.setWindowTitle('Download Manager')  
        self.setMaximumSize(541,346)
        self.setMinimumSize(541, 346)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handel_Browse)
        self.pushButton_7.clicked.connect(self.Get_YouTube_Video)
        self.pushButton_3.clicked.connect(self.Download_YouTube_Video)
        self.pushButton_4.clicked.connect(self.save_browse)
        self.pushButton_6.clicked.connect(self.open_github)
        self.pushButton_5.clicked.connect(self.open_youtube)
        self.pushButton_8.clicked.connect(self.open_twitter)
    def Handel_Browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".",filter="All Files (*.*)")
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'",''))
        self.lineEdit_2.setText(name)
    def Handel_Progress(self,blocknum,blocksize,totalsize):
        read = blocknum * blocksize
        if totalsize > 0 :
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents()
    def Download (self):
        url_ = self.lineEdit.text()
        save_location_ = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url_,save_location_,self.Handel_Progress)
        except Exception :
                QMessageBox.warning(self, "Warning", "Download failed, please try again")
                return
        QMessageBox.information(self, "Congratulation", "Download completed successfully")
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
    def save_browse(self):
        save = QFileDialog.getExistingDirectory(self,"Save As")
        self.lineEdit_4.setText(save)
    def Get_YouTube_Video (self):
        video_link = self.lineEdit_3.text()
        video = pafy.new(video_link)
        save_location = self.lineEdit_4.text()
        st_ = video.allstreams
        for s in st_ :
            size = humanize.naturalsize(s.get_filesize())
            data = '{} {} {} {}'.format(s.mediatype,s.extension,s.quality,size)
            self.comboBox.addItem(data)
    def Download_YouTube_Video (self):
        video_link = self.lineEdit_3.text()
        save_location = self.lineEdit_4.text()
        video = pafy.new(video_link)
        st_ = video.allstreams
        quality = self.comboBox.currentIndex()
        down = st_[quality].download(filepath=save_location)
        QMessageBox.information(self, "Congratulation", "Download completed successfully")    
    def open_youtube(self):
        webbrowser.open('https://www.youtube.com/channel/UCCLowKYnIDTjfGuwHytglEw')   
    def open_github(self):
        webbrowser.open('https://github.com/anisharkat')  
    def open_twitter(self):
        webbrowser.open('https://twitter.com/_anisharkat')         
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()        