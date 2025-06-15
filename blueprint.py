# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blueprintHtWBhF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 300)
        MainWindow.setMinimumSize(QSize(567, 250))
        MainWindow.setMaximumSize(QSize(567, 300))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(40,40,40);")
        self.Audio = QGroupBox(self.centralwidget)
        self.Audio.setObjectName(u"Audio")
        self.Audio.setGeometry(QRect(10, 90, 261, 121))
        self.Audio.setStyleSheet(u"")
        self.Audio.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.mp3_radio = QRadioButton(self.Audio)
        self.mp3_radio.setObjectName(u"mp3_radio")
        self.mp3_radio.setGeometry(QRect(10, 40, 51, 20))
        self.mp3_radio.setChecked(True)
        self.flac_radio = QRadioButton(self.Audio)
        self.flac_radio.setObjectName(u"flac_radio")
        self.flac_radio.setGeometry(QRect(130, 40, 51, 20))
        self.wav_radio = QRadioButton(self.Audio)
        self.wav_radio.setObjectName(u"wav_radio")
        self.wav_radio.setGeometry(QRect(70, 40, 51, 20))
        self.label_2 = QLabel(self.Audio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 91, 16))
        self.go_audio = QPushButton(self.Audio)
        self.go_audio.setObjectName(u"go_audio")
        self.go_audio.setGeometry(QRect(10, 75, 75, 24))
        self.playlist_check = QCheckBox(self.Audio)
        self.playlist_check.setObjectName(u"playlist_check")
        self.playlist_check.setGeometry(QRect(190, 90, 61, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 25, 91, 16))
        self.directory_browse = QPushButton(self.centralwidget)
        self.directory_browse.setObjectName(u"directory_browse")
        self.directory_browse.setGeometry(QRect(110, 22, 75, 24))
        self.directory_browse.setStyleSheet(u"background-color: rgb(60,60,60);\n"
"border-radius: 5px;")
        self.directory_label = QLineEdit(self.centralwidget)
        self.directory_label.setObjectName(u"directory_label")
        self.directory_label.setGeometry(QRect(200, 24, 351, 21))
        self.directory_label.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"\n"
"border-radius: 5px; border-bottom: 1px solid white;")
        self.directory_label.setFrame(False)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 31, 16))
        self.URL_label = QLineEdit(self.centralwidget)
        self.URL_label.setObjectName(u"URL_label")
        self.URL_label.setGeometry(QRect(50, 58, 501, 21))
        self.URL_label.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"\n"
"border-radius: 5px; border-bottom: 1px solid white;")
        self.URL_label.setFrame(False)
        self.Video = QGroupBox(self.centralwidget)
        self.Video.setObjectName(u"Video")
        self.Video.setGeometry(QRect(280, 90, 261, 121))
        self.Video.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.mp4_radio = QRadioButton(self.Video)
        self.mp4_radio.setObjectName(u"mp4_radio")
        self.mp4_radio.setGeometry(QRect(10, 40, 51, 20))
        self.mp4_radio.setChecked(True)
        self.mkv_radio = QRadioButton(self.Video)
        self.mkv_radio.setObjectName(u"mkv_radio")
        self.mkv_radio.setGeometry(QRect(130, 40, 51, 20))
        self.avi_radio = QRadioButton(self.Video)
        self.avi_radio.setObjectName(u"avi_radio")
        self.avi_radio.setGeometry(QRect(70, 40, 51, 20))
        self.label_4 = QLabel(self.Video)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 91, 16))
        self.go_video = QPushButton(self.Video)
        self.go_video.setObjectName(u"go_video")
        self.go_video.setGeometry(QRect(10, 75, 75, 24))
        self.playlist_check_video = QCheckBox(self.Video)
        self.playlist_check_video.setObjectName(u"playlist_check_video")
        self.playlist_check_video.setGeometry(QRect(190, 90, 61, 20))
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(10, 220, 461, 51))
        self.destination = QPushButton(self.centralwidget)
        self.destination.setObjectName(u"destination")
        self.destination.setGeometry(QRect(480, 233, 75, 31))
        self.destination.setStyleSheet(u"background-color: rgb(60, 60, 60);\n"
"border-radius: 5px; ")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YouTube downloader", None))
        self.Audio.setTitle(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.mp3_radio.setText(QCoreApplication.translate("MainWindow", u"mp3", None))
        self.flac_radio.setText(QCoreApplication.translate("MainWindow", u"flac", None))
        self.wav_radio.setText(QCoreApplication.translate("MainWindow", u"wav", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select format", None))
        self.go_audio.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.playlist_check.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select directory: ", None))
        self.directory_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.directory_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.URL_label.setText("")
        self.Video.setTitle(QCoreApplication.translate("MainWindow", u"Video", None))
        self.mp4_radio.setText(QCoreApplication.translate("MainWindow", u"mp4", None))
        self.mkv_radio.setText(QCoreApplication.translate("MainWindow", u"mkv", None))
        self.avi_radio.setText(QCoreApplication.translate("MainWindow", u"avi", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select format", None))
        self.go_video.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.playlist_check_video.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.result_label.setText("")
        self.destination.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
    # retranslateUi

