#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- This is the estopwindow that will enable the pod to perform an emergancy stop during any state of the mission.
- The brakes are closed and power relay is disabled to ensure the pod is stopped safely.

* This interface is still currently in the development stage, so modifications to its design and functionality will be added overtime.

@author: SupaeroHyperloop test
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_estopWindow(QtWidgets.QWidget):
    def setESTOPstate(self,main_w,log):
        self.ui=main_w
        TextButton= 'ESTOP'
        
        timer = self.ui.time
        self.ui.setStateTimer()
        
        m, s = divmod(timer, 60)

        log = log + '{:02d}:{:02d}'.format(int(m), int(s)) + ": Emergancy Stop Called...\n"
        
        self.ui.updateLogList(log)
        timer = self.ui.time
        self.ui.setStateTimer()
        
        self.ui.PodModeReading.setText(TextButton)
        self.ui.LogHistoryBrowser.setText(log)
        
    def setupUi(self, estopWindow,Ui_MainWindow,log):
        estopWindow.setObjectName("estopWindow")
        estopWindow.resize(546, 300)
        self.label = QtWidgets.QLabel(estopWindow)
        self.label.setGeometry(QtCore.QRect(150, 80, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.acceptbutton = QtWidgets.QPushButton(estopWindow, clicked=lambda: self.setESTOPstate(Ui_MainWindow,log))
        self.acceptbutton.clicked.connect(lambda:estopWindow.close())
        self.acceptbutton.setGeometry(QtCore.QRect(170, 200, 93, 28))
        self.acceptbutton.setObjectName("acceptbutton")

        self.declinebutton = QtWidgets.QPushButton(estopWindow,clicked=lambda:estopWindow.close())
        self.declinebutton.setGeometry(QtCore.QRect(290, 200, 93, 28))
        self.declinebutton.setObjectName("declinebutton")

        self.retranslateUi(estopWindow)
        QtCore.QMetaObject.connectSlotsByName(estopWindow)

    def retranslateUi(self, estopWindow):
        _translate = QtCore.QCoreApplication.translate
        estopWindow.setWindowTitle(_translate("estopWindow", "Dialog"))
        self.label.setText(_translate("estopWindow", "Do you want to proceed? Y/N"))
        self.acceptbutton.setText(_translate("estopWindow", "Yes"))
        self.declinebutton.setText(_translate("estopWindow", "No"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    estopWindow = QtWidgets.QMainWindow()
    ui = Ui_estopWindow()
    ui.setupUi(estopWindow)
    estopWindow.show()

    sys.exit(app.exec_())


