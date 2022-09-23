# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
<<<<<<< HEAD

import sys

sys.path.insert(1,'/Users/ronankeane/Desktop/HYPERLOOP-SUPAERO/Hyperloop-SUPAERO/statesWindow.py')
sys.path.insert(1,'/Users/ronankeane/Desktop/HYPERLOOP-SUPAERO/Hyperloop-SUPAERO/estopWindow.py')
sys.path.insert(1,'/Users/ronankeane/Desktop/HYPERLOOP-SUPAERO/Hyperloop-SUPAERO/shutdownWindow.py')

=======
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b
from statesWindow import Ui_statesWindow
from estopWindow import Ui_estopWindow
from shutdownWindow import Ui_shutdownWindow

class Ui_MainWindow(object):
    def openStatesWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_statesWindow()
        self.ui.setupUi(self.window,Ui_MainWindow(),MainWindow)
        self.window.show()
    def openEstopWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_estopWindow()
        self.ui.setupUi(self.window,Ui_MainWindow(),MainWindow)
        self.window.show()
    def openShutdownWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_shutdownWindow()
        self.ui.setupUi(self.window,Ui_MainWindow(),MainWindow)
        self.window.show()
<<<<<<< HEAD
        
    def setupUi(self, MainWindow):

=======
    def setupUi(self, MainWindow):
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 712)
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
<<<<<<< HEAD
        
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(200, 13, 101, 31))

        self.timeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(1999, 12, 31), QtCore.QTime(23, 59, 59)))
        self.timeEdit.setMaximumDate(QtCore.QDate(1999, 12, 31))
        self.timeEdit.setMinimumDate(QtCore.QDate(1999, 12, 31))
        self.timeEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.timeEdit.setMinimumTime(QtCore.QTime(00, 00, 00))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setTimeSpec(QtCore.Qt.OffsetFromUTC)
        self.timeEdit.setTime(QtCore.QTime(0,0,0))
        self.timeEdit.setObjectName("timeEdit")
        
        # creating a timer object
        timer = QtCore.QTimer()
  
        # adding action to timer
        timer.timeout.connect(self.showTime)
  
        # update the timer every second
        timer.start(1000)
        
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 25))
        self.label.setObjectName("label")

                

      
=======
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(200, 13, 101, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 25))
        self.label.setObjectName("label")
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 55, 181, 31))
        self.label_2.setObjectName("label_2")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(200, 60, 101, 31))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 115, 141, 41))
        self.label_3.setObjectName("label_3")
<<<<<<< HEAD

        
=======
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 122, 141, 31))
        
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 45, 81, 31))
        self.label_4.setObjectName("label_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(560, 50, 101, 28))
        
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 80, 111, 31))
        self.label_5.setObjectName("label_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(560, 90, 101, 28))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 10, 291, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(560, 120, 101, 28))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 110, 101, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 308, 191, 31))
        self.label_8.setObjectName("label_8")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(580, 280, 101, 28))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(580, 240, 101, 28))
        
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(580, 310, 101, 28))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 240, 191, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 205, 121, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 270, 211, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 509, 141, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 479, 181, 31))
        self.label_13.setObjectName("label_13")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(550, 515, 101, 28))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(390, 449, 151, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(410, 410, 261, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(550, 485, 101, 28))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(550, 455, 101, 28))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(550, 545, 101, 28))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(370, 540, 161, 31))
        self.label_16.setObjectName("label_16")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_13.setGeometry(QtCore.QRect(560, 150, 101, 28))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(430, 140, 111, 31))
        self.label_18.setObjectName("label_18")
        self.Mode_logging = QtWidgets.QScrollArea(self.centralwidget)
        self.Mode_logging.setGeometry(QtCore.QRect(60, 200, 271, 121))
        
        self.Mode_logging.setWidgetResizable(True)
        self.Mode_logging.setObjectName("Mode_logging")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_12.setGeometry(QtCore.QRect(0, 0, 271, 121))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.Mode_logging.setWidget(self.scrollAreaWidgetContents)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(80, 170, 221, 31))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.shutdownButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.openShutdownWindow())
        self.shutdownButton.setGeometry(QtCore.QRect(70, 530, 181, 61))
        self.shutdownButton.setBaseSize(QtCore.QSize(100, 100))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setAutoFillBackground(True)
        self.shutdownButton.setAutoDefault(False)
        self.shutdownButton.setObjectName("shutdownButton")
        self.changeStateButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openStatesWindow())
        self.changeStateButton.setGeometry(QtCore.QRect(60, 330, 221, 61))
        
        self.changeStateButton.setAutoDefault(False)
        self.changeStateButton.setObjectName("changeStateButton")
        self.estopButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.openEstopWindow())
        self.estopButton.setGeometry(QtCore.QRect(90, 460, 131, 61))
        self.estopButton.setBaseSize(QtCore.QSize(100, 100))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.estopButton.setFont(font)
        self.estopButton.setAutoFillBackground(True)
        self.estopButton.setAutoDefault(False)
        self.estopButton.setObjectName("estopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Time (total)"))
        self.label_2.setText(_translate("MainWindow", "Time (state)"))
        self.label_3.setText(_translate("MainWindow", "Pod Mode:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:18pt; font-weight:600;\">Armed</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Pod:"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Brakes:"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Temperature (°C)"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Clamp:"))
        self.label_8.setText(_translate("MainWindow", "Accel (m/s2):"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">0</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">0</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Distance (m):"))
        self.label_10.setText(_translate("MainWindow", "IMU"))
        self.label_11.setText(_translate("MainWindow", "Velocity (m/s):"))
        self.label_12.setText(_translate("MainWindow", "Rear Left:"))
        self.label_13.setText(_translate("MainWindow", "Front Right:"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">3</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Front Left:"))
        self.label_15.setText(_translate("MainWindow", "Levitation (cm)"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">3</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">3</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">3</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Rear Right:"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Battery:"))
<<<<<<< HEAD
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"))
=======
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Initialising...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Initialisation Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Booting...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Booting Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Filling Pod...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Filling Pod Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Loading...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Loading Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Arming...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Armed - Ready to Push</span></p></body></html>"))
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b
        self.label_17.setText(_translate("MainWindow", "Log"))
        self.shutdownButton.setText(_translate("MainWindow", "Shutdown"))
        self.changeStateButton.setText(_translate("MainWindow", "Change State"))
        self.estopButton.setText(_translate("MainWindow", "ESTOP"))
<<<<<<< HEAD
        
    def showTime(self):
  
        # getting current time
        current_time = QtCore.QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.label.setText(label_time)

        
=======
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
<<<<<<< HEAD
    
    
 #       self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Initialising...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Initialisation Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Booting...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Booting Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Filling Pod...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Filling Pod Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Loading...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Loading Done</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Arming...</span></p>\n"
#"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt;\">Armed - Ready to Push</span></p></body></html>"))
=======
>>>>>>> 37c85cbcd286831a25ec8879ebdd5e798dcc9a0b
