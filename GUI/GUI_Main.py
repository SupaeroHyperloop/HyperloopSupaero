#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- This is the main window that will be used to display the key parameters recieved from the on-board sensors of the Hyperloop pod.
- This window also enables you to launch the statesWindow where control commands can be accessed.
- An emergancy stop or a total shutdown of the Hyperloop pod can be enabled by accessing the estopWindow and shutdownWindow respectively.
- This interface is still currently in the development stage, so modifications to its design and functionality will be added overtime.

@author: SupaeroHyperloop
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys


#---Add paths of python files here----#
sys.path.insert(1,'/HyperloopSupaero/GUI/statesWindow.py') 
sys.path.insert(1,'/HyperloopSupaero/GUI/estopWindow.py')
sys.path.insert(1,'/HyperloopSupaero/GUI/shutdownWindow.py')


from statesWindow import Ui_statesWindow
from estopWindow import Ui_estopWindow
from shutdownWindow import Ui_shutdownWindow


    
class Ui_MainWindow(object):

    def __init__(self):

        self.time =0.00000
        self.log = str()

    def openStatesWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_statesWindow()
        self.ui.setupUi(self.window,Ui_MainWindow(),MainWindow,self.getLogList(),self.getTotalTimer())
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
        
        
        
#-----------Set clock and update Log of UI --------------------#        

    def setTotalTimer(self,timer):
        if timer is None:
            self.time=0.000
        else:
            self.time = timer
        self.totalTime=QtCore.QTimer()
        self.totalTime.setInterval(50)
        self.totalTime.timeout.connect(self.setTotalTimeLCD)
        self.totalTime.start()
   
    def setTotalTimeLCD(self):   
        self.time = self.time + 0.05
        self.getTotalTimer()
        
        m, s = divmod(self.time, 60)
        self.totalTimerLCD.display('{:02d}:{:02d}'.format(int(m), int(s)))
        
    def getTotalTimer(self):
        return self.time
        
    def setStateTimer(self):
        self.timeState= 0.000
        self.stateTime=QtCore.QTimer()
        self.stateTime.setInterval(50)
        self.stateTime.timeout.connect(self.setStateTimeLCD)
        self.stateTime.start()
        
    def setStateTimeLCD(self):    
        self.timeState += 0.05
        self.stateTimerLCD.display("{:.2f}".format(self.timeState))  
        
    def updateLogList(self, logList):
        self.log = logList
    
    def getLogList(self):
        return self.log
        
        
#-----------Simulation of the pod --------------------#   
  
    def computeAccel(self):
        self.computedAccel= 0.000
        self.accelCounter.setInterval(1000)
        self.accelCounter.timeout.connect(self.setAccel)
        self.accelCounter.start()
    
    def computeVelocity(self):
        self.computedVelocity= 0.000
        self.velocityCounter.setInterval(1000)
        self.velocityCounter.timeout.connect(self.setVelocity)
        self.velocityCounter.start()
    
    def computeDistance(self):
        self.computedDistance= 0.000
        self.distanceCounter.setInterval(1000)
        self.distanceCounter.timeout.connect(self.setDistance)
        self.distanceCounter.start()
        
    def setAccel(self):
        self.computedAccel+=0.05
        self.AccelReading .setText("{:.2f}".format(self.computedAccel))
    
    def setVelocity(self):
        self.computedVelocity+=0.1
        self.VelocityReading.setText("{:.2f}".format(self.computedVelocity))
    
    def setDistance(self):
        self.computedDistance+=0.5
        self.DistanceReading.setText("{:.2f}".format(self.computedDistance))
        
#------------------------------------------------------#   
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 949)
        MainWindow.setStyleSheet("background-color: darkblue;")
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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
        
        #Time Readings
        
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

        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QPixmap('GUI_Logo.png') #Remember to add your own path
        self.label_Logo.setPixmap(self.pixmap)
        self.label_Logo.setGeometry(QtCore.QRect(40, 450, 900, 500))

        #Temperature Readings

        self.PodTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.PodTempReading.setGeometry(QtCore.QRect(460, 85, 101, 28))
        self.PodTempReading.setObjectName("PodTempReading")
        self.PodTempReading.setStyleSheet("background-color: white;")
        
        self.BrakesTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.BrakesTempReading.setGeometry(QtCore.QRect(460, 115, 101, 28))
        self.BrakesTempReading.setObjectName("BrakesTempReading")
        self.BrakesTempReading.setStyleSheet("background-color: white;")
        
        self.ClampTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.ClampTempReading.setGeometry(QtCore.QRect(460, 145, 101, 28))
        self.ClampTempReading.setObjectName("ClampTempReading")
        self.ClampTempReading.setStyleSheet("background-color: white;")
        
        self.BatteryTempReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.BatteryTempReading.setGeometry(QtCore.QRect(460, 175, 101, 28))
        self.BatteryTempReading.setObjectName("BatteryTempReading")
        self.BatteryTempReading.setStyleSheet("background-color: white;")
          
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
        
        #IMU Readings
    
        self.VelocityReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.VelocityReading.setGeometry(QtCore.QRect(775, 115, 101, 28))
        self.VelocityReading.setObjectName("VelocityReading")
        self.VelocityReading.setStyleSheet("background-color: white;")
        
        self.DistanceReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.DistanceReading.setGeometry(QtCore.QRect(775, 85, 101, 28))
        self.DistanceReading.setStyleSheet("background-color: white;")
        self.DistanceReading.setObjectName("DistanceReading")
        
        self.AccelReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.AccelReading .setGeometry(QtCore.QRect(775, 145, 101, 28))
        self.AccelReading .setObjectName("AccelReading ")
        self.AccelReading .setStyleSheet("background-color: white")
        
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
        
        self.accelCounter=QtCore.QTimer()
        self.velocityCounter=QtCore.QTimer()
        self.distanceCounter=QtCore.QTimer()
       
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
                
        self.RearLeftReading  = QtWidgets.QTextBrowser(self.centralwidget)
        self.RearLeftReading.setGeometry(QtCore.QRect(1110, 145, 101, 28))
        self.RearLeftReading.setObjectName("RearLeftReading ")
        self.RearLeftReading.setStyleSheet("background-color: white;")
        
        self.FrontRightReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.FrontRightReading.setGeometry(QtCore.QRect(1110, 115, 101, 28))
        self.FrontRightReading.setObjectName("FrontRightReading")
        self.FrontRightReading.setStyleSheet("background-color: white;")
        
        self.FrontLeftReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.FrontLeftReading.setGeometry(QtCore.QRect(1110, 85, 101, 28))
        self.FrontLeftReading.setObjectName("FrontLeftReading")
        self.FrontLeftReading.setStyleSheet("background-color: white;")
        
        self.RearRightReading = QtWidgets.QTextBrowser(self.centralwidget)
        self.RearRightReading.setGeometry(QtCore.QRect(1110, 175, 101, 28))
        self.RearRightReading.setObjectName("RearRightReading")
        self.RearRightReading.setStyleSheet("background-color: white;")
        
        # Tab Options
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(310, 220, 921, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.ModeTab = QtWidgets.QWidget()
        self.ModeTab.setObjectName("ModeTab")
        
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
        
        # Enable scrolling option
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Button Options
        
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
        self.Mode_logging.setWidget(self.scrollAreaWidgetContents)
        
        
        self.LogHistoryBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.LogHistoryBrowser.moveCursor(QtGui.QTextCursor.End) #the self.scrollbar is the same as your self.console_window
        self.LogHistoryBrowser.setVerticalScrollBarPolicy(2)
        self.LogHistoryBrowser.setGeometry(QtCore.QRect(0, 0, 581, 441))
        self.LogHistoryBrowser.setObjectName("LogHistoryBrowser")
        self.LogHistoryBrowser.setStyleSheet("background-color: white;")
        
        self.PodModeReading = QtWidgets.QTextBrowser(self.ModeTab)
        self.PodModeReading.setGeometry(QtCore.QRect(20, 70, 891, 31))
        self.PodModeReading.setStyleSheet("background-color: white;")
        self.PodModeReading.setObjectName("textBrowser")

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
        self.PodTempReading.setHtml(_translate("MainWindow", "15"))
        self.BrakesTempLabel.setText(_translate("MainWindow", "Brakes:"))
        self.BrakesTempReading.setHtml(_translate("MainWindow", "15"))
        self.TemperatureLabel.setText(_translate("MainWindow", "Temperature (°C)"))
        self.ClampTempReading.setHtml(_translate("MainWindow", "15"))   
        self.BatteryTempReading.setHtml(_translate("MainWindow", "15"))  
        self.ClampsTempLabel.setText(_translate("MainWindow", "Clamp:"))
        self.BatteryTempLabel.setText(_translate("MainWindow", "Battery:"))
        
        self.IMULabel.setText(_translate("MainWindow", "IMU"))
        self.DistanceLabel.setText(_translate("MainWindow", "Distance (m):"))
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity (m/s):"))
        self.AccelLabel.setText(_translate("MainWindow", "Accel (m/s2):"))
        self.VelocityReading.setHtml(_translate("MainWindow", "0"))
        self.DistanceReading.setHtml(_translate("MainWindow", "0"))
        self.AccelReading .setHtml(_translate("MainWindow", "0"))

        self.RearLeftLabel.setText(_translate("MainWindow", "Rear Left:"))
        self.FrontRightLabel.setText(_translate("MainWindow", "Front Right:"))
        self.FrontLeftLabel.setText(_translate("MainWindow", "Front Left:"))
        self.RearLeftReading .setHtml(_translate("MainWindow", "3"))

        self.LevitationLabel.setText(_translate("MainWindow", "Levitation (cm)"))
        self.FrontRightReading.setHtml(_translate("MainWindow", "3"))
        self.FrontLeftReading.setHtml(_translate("MainWindow", "3"))
        self.RearRightReading.setHtml(_translate("MainWindow", "3"))
        self.RearRightLabel.setText(_translate("MainWindow", "Rear Right:"))

        self.estopButton.setText(_translate("MainWindow", "ESTOP"))
        self.PodModeLabel.setText(_translate("MainWindow", "Pod Mode:"))
        self.PodModeReading.setHtml(_translate("MainWindow", ""))
        self.shutdownButton.setText(_translate("MainWindow", "Shutdown"))
        self.changeStateButton.setText(_translate("MainWindow", "Change State"))
        self.LogLabel.setText(_translate("MainWindow", "Log"))
        self.LogHistoryBrowser.setHtml(_translate("MainWindow",None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModeTab), _translate("MainWindow", "Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TeleopTab), _translate("MainWindow", "Teleop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LowSpeedTab), _translate("MainWindow", "Low Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CamFTab), _translate("MainWindow", "CamF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CamRTab), _translate("MainWindow", "CamR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NavTab), _translate("MainWindow", "Nav"))

if __name__ == "__main__":
    import sys
    log = str()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
