import sys
import easygui
import subprocess
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from blueprint import Ui_MainWindow 

class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #init
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #button_connections
        self.ui.directory_browse.clicked.connect(self.browse) 
        self.ui.go_audio.clicked.connect(self.audio)
        self.ui.destination.clicked.connect(self.destination)
        self.ui.go_video.clicked.connect(self.video)
        
    def browse(self):
        global x
        x = easygui.diropenbox('Select directory of ytdlp.exe')
        self.ui.directory_label.setText(x)
        return x
    
    def audio(self):
        if self.ui.playlist_check.isChecked():
            
            if self.ui.mp3_radio.isChecked():
                command = f'ytdlp.exe -x --audio-format mp3 -o "{x}/Audio/%(playlist)s/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.wav_radio.isChecked():
                command = f'ytdlp.exe -x --audio-format wav -o "{x}/Audio/%(playlist)s/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.flac_radio.isChecked():
                command = f'ytdlp.exe -x --audio-format flac -o "{x}/Audio/%(playlist)s/%(title)s.%(ext)s" {self.ui.URL_label.text()}'           
        else:
                
            if self.ui.mp3_radio.isChecked():
                command = f'ytdlp.exe -x --audio-format mp3 -o "{x}/Audio/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.wav_radio.isChecked():
                command = f'ytdlp.exe -x --audio-format wav -o "{x}/Audio/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.flac_radio.isChecked():
                command = f'ytdlp.exe -x --audio-format flac -o "{x}/Audio/%(title)s.%(ext)s" {self.ui.URL_label.text()}'

        try:
            os.chdir(x)
            process = subprocess.Popen(f'{command}', 
                shell=True, 
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace')
            
            for line in process.stdout:
                self.ui.result_label.setText(f'{line}')
                QApplication.processEvents() #gui_refresh
            
            self.ui.result_label.setText(f'Done!\nFile(s) saved at {x}')
            
        except Exception as e:
            print(f"Error: {e}")
    
    def video(self):
    
        if self.ui.playlist_check_video.isChecked():
            
            if self.ui.mp4_radio.isChecked():
                command = f'ytdlp.exe -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" --merge-output-format mp4  -o "{x}/Video/%(playlist)s/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.mkv_radio.isChecked():
                command = f'ytdlp.exe -f "bestvideo+bestaudio/best" --merge-output-format mkv -o "{x}/Video/%(playlist)s/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.avi_radio.isChecked():
                command = f'ytdlp.exe -f "bestvideo+bestaudio/best" --remux-video avi -o "{x}/Video/%(playlist)s/%(title)s.%(ext)s" {self.ui.URL_label.text()}'           
        else:
                
            if self.ui.mp4_radio.isChecked():
                command = f'ytdlp.exe -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" --merge-output-format mp4  -o "{x}/Video/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.mkv_radio.isChecked():
                command = f'ytdlp.exe -f "bestvideo+bestaudio/best" --merge-output-format mkv -o "{x}/Video/%(title)s.%(ext)s" {self.ui.URL_label.text()}'
            elif self.ui.avi_radio.isChecked():
                command = f'ytdlp.exe -f "bestvideo+bestaudio/best" --remux-video avi -o "{x}/Video/%(title)s.%(ext)s" {self.ui.URL_label.text()}'  

        try:
            os.chdir(x)
            
            process = subprocess.Popen(f'{command}', 
                shell=True, 
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace')
            
            for line in process.stdout:
                self.ui.result_label.setText(f'{line}')
                QApplication.processEvents() # gui_refresh
            
            self.ui.result_label.setText(f'Done!\nFile(s) saved at {x}')
            
        except Exception as e:
            print(f"Error: {e}")
    
    def destination(self):
        try:
            os.startfile(x)
        except:
            QMessageBox.information(self, "Please select working directory first","Did you forget to browse for location of ytdlp and ffmpeg executables?")
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())
