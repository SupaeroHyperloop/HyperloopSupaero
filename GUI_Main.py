#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:03:37 2022

@author: SupaeroHyperloop
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys


#---Add paths of python files here----#

sys.path.insert(1,'statesWindow.py') 
sys.path.insert(1,'estopWindow.py')
sys.path.insert(1,'shutdownWindow.py')


from statesWindow import Ui_statesWindow
from estopWindow import Ui_estopWindow
from shutdownWindow import Ui_shutdownWindow

class Ui_MainWindow(object):
    

    def __init__(self):
        self.LogList = str()

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
        
        
    def setTotalTimer(self):
        self.time=0.000
        self.totalTime.timeout.connect(self.setTotalTimeLCD)
        self.totalTime.start(50)
        print(self.LogList)
            
    def setTotalTimeLCD(self):                    
        self.time +=0.05
        self.totalTimerLCD.display("{:.2f}".format(self.time))    
  
    def setStateTimer(self):
        self.timeState= float(0.000)
        self.stateTime.timeout.connect(self.setStateTimeLCD)
        self.stateTime.start(50)
                
    def setStateTimeLCD(self):    
        self.timeState += 0.05
        self.stateTimerLCD.display("{:.2f}".format(self.timeState))    


        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 949)
        MainWindow.setStyleSheet("background-color: darkblue;")
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        """
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(200, 17, 101, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setStyleSheet("background-color: white;")
        
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(200, 57, 101, 31))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.timeEdit_2.setStyleSheet("background-color: white;")
        """""
        
        self.TimeTotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeTotalLabel.setGeometry(QtCore.QRect(10, 20, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TimeTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeTotalLabel.setFont(font)
        self.TimeTotalLabel.setObjectName("TimeTotalLabel")
        self.TimeTotalLabel.setStyleSheet("background-color: white;")

        self.TimeStateLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeStateLabel.setGeometry(QtCore.QRect(10, 60, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TimeStateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeStateLabel.setFont(font)
        self.TimeStateLabel.setObjectName("TimeStateLabel")
        self.TimeStateLabel.setStyleSheet("background-color: white;")
        
        
        
        self.totalTimerLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.totalTimerLCD.setGeometry(QtCore.QRect(210, 17, 101, 31))
        self.totalTimerLCD.setStyleSheet("QLCDNumber{\n" "\n" "background-color:black;\n" "}")
        self.totalTimerLCD.setObjectName("totalTimerLCD")
        
        self.stateTimerLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.stateTimerLCD.setGeometry(QtCore.QRect(210, 57, 101, 31))
        self.stateTimerLCD.setStyleSheet("QLCDNumber{\n" "\n" "background-color:black;\n" "}")
        self.stateTimerLCD.setObjectName("stateTimerLCD")
        
        #Create a timer
        self.totalTime=QtCore.QTimer()
        self.stateTime=QtCore.QTimer()
        
        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QPixmap('GUI_Logo.png') #Remember to add your own path
        self.label_Logo.setPixmap(self.pixmap)
        self.label_Logo.setGeometry(QtCore.QRect(40, 450, 900, 500))

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(460, 85, 101, 28))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setStyleSheet("background-color: white;")
        
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 115, 101, 28))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.setStyleSheet("background-color: white;")
        
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(460, 145, 101, 28))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_5.setStyleSheet("background-color: white;")
        
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_13.setGeometry(QtCore.QRect(460, 175, 101, 28))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_13.setStyleSheet("background-color: white;")
        
        
        self.TemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.TemperatureLabel.setGeometry(QtCore.QRect(370, 45, 175, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TemperatureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TemperatureLabel.setFont(font)
        self.TemperatureLabel.setObjectName("TemperatureLabel")
        self.TemperatureLabel.setStyleSheet("background-color: white;")
        
        
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(775, 115, 101, 28))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_4.setStyleSheet("background-color: white;")
        
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(775, 85, 101, 28))
        self.textBrowser_6.setStyleSheet("background-color: white;")
        self.textBrowser_6.setObjectName("textBrowser_6")
        
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(775, 145, 101, 28))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_7.setStyleSheet("background-color: white")
        
        #Temperature labels
        
        self.PodTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.PodTempLabel.setGeometry(QtCore.QRect(340, 85, 81, 28))
        self.PodTempLabel.setObjectName("PodTempLabel")
        self.PodTempLabel.setStyleSheet("background-color: white;")
        
        self.BrakesTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrakesTempLabel.setGeometry(QtCore.QRect(340, 115, 81, 28))
        self.BrakesTempLabel.setObjectName("BrakesTempLabel")
        self.BrakesTempLabel.setStyleSheet("background-color: white;")
        
        self.ClampsTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClampsTempLabel.setGeometry(QtCore.QRect(340, 145, 81, 28))
        self.ClampsTempLabel.setObjectName("ClampsTempLabel")
        self.ClampsTempLabel.setStyleSheet("background-color: white;")
        
        self.BatteryTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryTempLabel.setGeometry(QtCore.QRect(340, 175, 81, 28))
        self.BatteryTempLabel.setObjectName("BatteryTempLabel")
        self.BatteryTempLabel.setStyleSheet("background-color: white;")
        
        
        #IMU labels
        
        self.AccelLabel = QtWidgets.QLabel(self.centralwidget)
        self.AccelLabel.setGeometry(QtCore.QRect(650, 145, 121, 28))
        self.AccelLabel.setObjectName("AccelLabel")
        self.AccelLabel.setStyleSheet("background-color: white;")
        
        self.DistanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.DistanceLabel.setGeometry(QtCore.QRect(650, 85, 121, 28))
        self.DistanceLabel.setObjectName("DistanceLabel")
        self.DistanceLabel.setStyleSheet("background-color: white;")
        
        self.VelocityLabel = QtWidgets.QLabel(self.centralwidget)
        self.VelocityLabel.setGeometry(QtCore.QRect(650, 115, 121, 28))
        self.VelocityLabel.setObjectName("VelocityLabel")
        self.VelocityLabel.setStyleSheet("background-color: white;")

        self.IMULabel= QtWidgets.QLabel(self.centralwidget)
        self.IMULabel.setGeometry(QtCore.QRect(700, 45, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.IMULabel.setFont(font)
        self.IMULabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IMULabel.setObjectName("IMULabel")
        self.IMULabel.setStyleSheet("background-color: white;")
       
        
       # Levitation labels
        
        self.RearLeftLabel = QtWidgets.QLabel(self.centralwidget)
        self.RearLeftLabel.setGeometry(QtCore.QRect(950, 145, 151, 28))
        self.RearLeftLabel.setObjectName("RearLeftLabel")
        self.RearLeftLabel.setStyleSheet("background-color: white;")
        
        self.FrontRightLabel = QtWidgets.QLabel(self.centralwidget)
        self.FrontRightLabel.setGeometry(QtCore.QRect(950, 115, 151, 28))
        self.FrontRightLabel.setObjectName("FrontRightLabel")
        self.FrontRightLabel.setStyleSheet("background-color: white;")
        
        self.FrontLeftLabel = QtWidgets.QLabel(self.centralwidget)
        self.FrontLeftLabel.setGeometry(QtCore.QRect(950, 85, 151, 28))
        self.FrontLeftLabel.setObjectName("FrontLeftLabel")
        self.FrontLeftLabel.setStyleSheet("background-color: white;")
        
        
        self.RearRightLabel = QtWidgets.QLabel(self.centralwidget)
        self.RearRightLabel.setGeometry(QtCore.QRect(950, 175, 151, 28))
        self.RearRightLabel.setObjectName("RearRightLabel")
        self.RearRightLabel.setStyleSheet("background-color: white;")
        
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(1110, 145, 101, 28))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_8.setStyleSheet("background-color: white;")
        
    
        self.LevitationLabel = QtWidgets.QLabel(self.centralwidget)
        self.LevitationLabel.setGeometry(QtCore.QRect(970, 45, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.LevitationLabel.setFont(font)
        self.LevitationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LevitationLabel.setObjectName("LevitationLabel")
        self.LevitationLabel.setStyleSheet("background-color: white;")
        
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(1110, 115, 101, 28))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_9.setStyleSheet("background-color: white;")
        
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(1110, 85, 101, 28))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_10.setStyleSheet("background-color: white;")
        
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(1110, 175, 101, 28))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_11.setStyleSheet("background-color: white;")
        

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(310, 220, 921, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.ModeTab = QtWidgets.QWidget()
        self.ModeTab.setObjectName("ModeTab")

        
        self.estopButton = QtWidgets.QPushButton(self.ModeTab,
                                                 clicked=lambda:self.openEstopWindow())
        self.estopButton.setGeometry(QtCore.QRect(40, 200, 221, 61))
        self.estopButton.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.estopButton.setFont(font)
        self.estopButton.setAutoFillBackground(True)
        self.estopButton.setAutoDefault(False)
        self.estopButton.setObjectName("estopButton")
        self.estopButton.setStyleSheet("background-color: gray;")
        
        self.PodModeLabel = QtWidgets.QLabel(self.ModeTab)
        self.PodModeLabel.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.PodModeLabel.setObjectName("PodModeLabel")
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.PodModeLabel.setFont(font)
        self.PodModeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PodModeLabel.setStyleSheet("background-color: white;")
        
        self.shutdownButton = QtWidgets.QPushButton(self.ModeTab,
                                    clicked=lambda: self.openShutdownWindow())
        self.shutdownButton.setGeometry(QtCore.QRect(40, 261, 221, 61))
        self.shutdownButton.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setAutoFillBackground(True)
        self.shutdownButton.setAutoDefault(False)
        self.shutdownButton.setObjectName("shutdownButton")
        self.shutdownButton.setStyleSheet("background-color: gray;")
        
        self.changeStateButton = QtWidgets.QPushButton(self.ModeTab,
                                    clicked=lambda: self.openStatesWindow())
        self.changeStateButton.setGeometry(QtCore.QRect(40, 140, 221, 61))
        self.changeStateButton.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.changeStateButton.setFont(font)
        self.changeStateButton.setAutoDefault(False)
        self.changeStateButton.setObjectName("changeStateButton")
        self.changeStateButton.setStyleSheet("background-color: gray;")
        
        self.LogLabel = QtWidgets.QLabel(self.ModeTab)
        self.LogLabel.setGeometry(QtCore.QRect(330, 130, 581, 41))
        self.LogLabel.setFont(font)
        self.LogLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LogLabel.setObjectName("LogLabel")
        self.LogLabel.setStyleSheet("background-color: gray;")
        
        self.Mode_logging = QtWidgets.QScrollArea(self.ModeTab)
        self.Mode_logging.setGeometry(QtCore.QRect(330, 170, 581, 441))
        
        self.Mode_logging.setWidgetResizable(True)
        self.Mode_logging.setObjectName("Mode_logging")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_12.setGeometry(QtCore.QRect(0, 0, 581, 441))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_12.setStyleSheet("background-color: white;")
        
        self.Mode_logging.setWidget(self.scrollAreaWidgetContents)
        
        self.textBrowser = QtWidgets.QTextBrowser(self.ModeTab)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 891, 31))
        self.textBrowser.setStyleSheet("background-color: white;")
        self.textBrowser.setObjectName("textBrowser")
        
        self.tabWidget.addTab(self.ModeTab, "")
        self.TeleopTab = QtWidgets.QWidget()
        self.TeleopTab.setObjectName("TeleopTab")
        self.tabWidget.addTab(self.TeleopTab, "")
        self.LowSpeedTab = QtWidgets.QWidget()
        self.LowSpeedTab.setObjectName("LowSpeedTab")
        self.tabWidget.addTab(self.LowSpeedTab, "")
        self.CamFTab = QtWidgets.QWidget()
        self.CamFTab.setObjectName("CamFTab")
        self.tabWidget.addTab(self.CamFTab, "")
        self.CamRTab = QtWidgets.QWidget()
        self.CamRTab.setObjectName("CamRTab")
        self.tabWidget.addTab(self.CamRTab, "")
        self.NavTab = QtWidgets.QWidget()
        self.NavTab.setObjectName("NavTab")
        self.tabWidget.addTab(self.NavTab, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TimeTotalLabel.setText(_translate("MainWindow", "Time (total)"))
        self.TimeStateLabel.setText(_translate("MainWindow", "Time (state)"))
        self.PodTempLabel.setText(_translate("MainWindow", "Pod:"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        self.BrakesTempLabel.setText(_translate("MainWindow", "Brakes:"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        self.TemperatureLabel.setText(_translate("MainWindow", "Temperature (°C)"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">15</span></p></body></html>"))
        
        self.ClampsTempLabel.setText(_translate("MainWindow", "Clamp:"))
        self.AccelLabel.setText(_translate("MainWindow", "Accel (m/s2):"))
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
        self.DistanceLabel.setText(_translate("MainWindow", "Distance (m):"))
        
        self.IMULabel.setText(_translate("MainWindow", "IMU"))
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity (m/s):"))
        
        
        self.RearLeftLabel.setText(_translate("MainWindow", "Rear Left:"))
        self.FrontRightLabel.setText(_translate("MainWindow", "Front Right:"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">3</span></p></body></html>"))
        self.FrontLeftLabel.setText(_translate("MainWindow", "Front Left:"))
        self.LevitationLabel.setText(_translate("MainWindow", "Levitation (cm)"))
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
        self.RearRightLabel.setText(_translate("MainWindow", "Rear Right:"))
      
        self.BatteryTempLabel.setText(_translate("MainWindow", "Battery:"))
        self.estopButton.setText(_translate("MainWindow", "ESTOP"))
        self.PodModeLabel.setText(_translate("MainWindow", "Pod Mode:"))
        self.shutdownButton.setText(_translate("MainWindow", "Shutdown"))
        self.changeStateButton.setText(_translate("MainWindow", "Change State"))
        self.LogLabel.setText(_translate("MainWindow", "Log"))
        
        self.textBrowser_12.setHtml(_translate("MainWindow",""))
        
        self.textBrowser.setHtml(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModeTab), _translate("MainWindow", "Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TeleopTab), _translate("MainWindow", "Teleop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LowSpeedTab), _translate("MainWindow", "Low Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CamFTab), _translate("MainWindow", "CamF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CamRTab), _translate("MainWindow", "CamR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NavTab), _translate("MainWindow", "Nav"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
