# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_statesWindow(object):

    def setPreDriveState(self,main_w,MainWindow):
        TextButton= self.PreDriveButton_DS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
        
    def setInitState(self,main_w,MainWindow):
        TextButton= self.InitButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
        
        

    
    def setInitState(self,main_w,MainWindow):
        TextButton= self.InitButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setPreDriveState(self,main_w,MainWindow):
        TextButton= self.PreDriveButton_DS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)

    def setDriveState(self,main_w,MainWindow):
        TextButton= self.DriveButton_DS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)

       
        

    def setPreArmState(self,main_w,MainWindow):
        TextButton= self.PreArmButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setArmState(self,main_w,MainWindow):
        TextButton= self.ArmButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setLaunchState(self,main_w,MainWindow):
        TextButton= self.LaunchButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setFlightState(self,main_w,MainWindow):
        TextButton= self.FlightButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setSoftStop(self,main_w,MainWindow):
        TextButton= self.SoftStopButton_FS.text()
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    
    def setupUi(self, statesWindow, Ui_MainWindow,MainWindow):
        statesWindow.setObjectName("statesWindow")
        statesWindow.resize(450, 344)
        self.label = QtWidgets.QLabel(statesWindow)
        self.label.setGeometry(QtCore.QRect(270, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(statesWindow)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.InitButton_FS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setInitState(Ui_MainWindow,MainWindow))
        self.InitButton_FS.clicked.connect(lambda:statesWindow.close())
        self.InitButton_FS.setGeometry(QtCore.QRect(290, 70, 93, 28))
        self.InitButton_FS.setObjectName("InitButton_FS")
        
        self.PreArmButton_FS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setPreArmState(Ui_MainWindow,MainWindow))
        self.PreArmButton_FS.clicked.connect(lambda:statesWindow.close())
        self.PreArmButton_FS.setGeometry(QtCore.QRect(290, 110, 93, 28))
        self.PreArmButton_FS.setObjectName("PreArmButton_FS")
        
        self.ArmButton_FS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setArmState(Ui_MainWindow,MainWindow))
        self.ArmButton_FS.clicked.connect(lambda:statesWindow.close())
        self.ArmButton_FS.setGeometry(QtCore.QRect(290, 150, 93, 28))
        self.ArmButton_FS.setObjectName("ArmButton_FS")
        
        self.LaunchButton_FS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setLaunchState(Ui_MainWindow,MainWindow))
        self.LaunchButton_FS.clicked.connect(lambda:statesWindow.close())
        self.LaunchButton_FS.setGeometry(QtCore.QRect(290, 190, 93, 28))
        self.LaunchButton_FS.setObjectName("LaunchButton_FS")
        
        self.FlightButton_FS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setFlightState(Ui_MainWindow,MainWindow))
        self.FlightButton_FS.clicked.connect(lambda:statesWindow.close())
        self.FlightButton_FS.setGeometry(QtCore.QRect(290, 230, 93, 28))
        self.FlightButton_FS.setObjectName("FlightButton_FS")
        
        self.SoftStopButton_FS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setSoftStop(Ui_MainWindow,MainWindow))
        self.SoftStopButton_FS.clicked.connect(lambda:statesWindow.close())
        self.SoftStopButton_FS.setGeometry(QtCore.QRect(290, 270, 93, 28))
        self.SoftStopButton_FS.setObjectName("SoftStopButton_FS")
        
        self.PreDriveButton_DS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setPreDriveState(Ui_MainWindow,MainWindow))
        self.PreDriveButton_DS.clicked.connect(lambda:statesWindow.close())
        self.PreDriveButton_DS.setGeometry(QtCore.QRect(80, 110, 93, 28))
        self.PreDriveButton_DS.setObjectName("PreDriveButton_DS")
        
        self.DriveButton_DS = QtWidgets.QPushButton(statesWindow, clicked=lambda: self.setDriveState(Ui_MainWindow,MainWindow))
        self.DriveButton_DS.clicked.connect(lambda:statesWindow.close())
        self.DriveButton_DS.setGeometry(QtCore.QRect(80, 180, 93, 28))
        self.DriveButton_DS.setObjectName("DriveButton_DS")


        self.retranslateUi(statesWindow)
        QtCore.QMetaObject.connectSlotsByName(statesWindow)

    def retranslateUi(self, statesWindow):
        _translate = QtCore.QCoreApplication.translate
        statesWindow.setWindowTitle(_translate("statesWindow", "Dialog"))
        self.label.setText(_translate("statesWindow", "FLIGHT STATES"))
        self.label_2.setText(_translate("statesWindow", "DRIVE STATES"))

        self.PreArmButton_FS.setText(_translate("statesWindow", "Pre-Arm"))
        self.InitButton_FS.setText(_translate("statesWindow", "Initializing"))

        self.InitButton_FS.setText(_translate("statesWindow", "Initializing"))
        self.PreArmButton_FS.setText(_translate("statesWindow", "Pre-Arm"))

        self.ArmButton_FS.setText(_translate("statesWindow", "Arm"))
        self.LaunchButton_FS.setText(_translate("statesWindow", "Launch"))
        self.FlightButton_FS.setText(_translate("statesWindow", "Flight"))
        self.SoftStopButton_FS.setText(_translate("statesWindow", "Soft Stop"))
        self.PreDriveButton_DS.setText(_translate("statesWindow", "Pre-Drive"))
        self.DriveButton_DS.setText(_translate("statesWindow", "Drive"))
        #self.PreArmButton_FS.text()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statesWindow = QtWidgets.QMainWindow()
    ui = Ui_statesWindow()
    ui.setupUi(statesWindow)
    statesWindow.show()

    sys.exit(app.exec_())

    sys.exit(app.exec_())

