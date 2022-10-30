# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
- This window allows the user to confirm their decision to perform a system shutdown.
- When the pod transitions to the shutdown state, the failsafe brakes are triggered and the main pod battery will shut off.

* This interface is still currently in the development stage, so modifications to its design and functionality will be added overtime.

@author: SupaeroHyperloop
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_shutdownWindow(object):
    def setShutdownState(self,main_w,MainWindow):
        TextButton= 'Shutdown'
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setupUi(self, shutdownWindow,Ui_MainWindow,MainWindow):
        shutdownWindow.setObjectName("shutdownWindow")
        shutdownWindow.resize(569, 300)
        self.acceptbutton = QtWidgets.QPushButton(shutdownWindow, clicked=lambda: self.setShutdownState(Ui_MainWindow,MainWindow))
        self.acceptbutton.clicked.connect(lambda:shutdownWindow.close())
        self.acceptbutton.setGeometry(QtCore.QRect(170, 230, 93, 28))
        self.acceptbutton.setObjectName("acceptbutton")
        self.declinebutton = QtWidgets.QPushButton(shutdownWindow,clicked=lambda:shutdownWindow.close())

        #self.declinebutton.clicked.connect(lambda:shutdownWindow.close())
        self.declinebutton.setGeometry(QtCore.QRect(290, 230, 93, 28))
        self.declinebutton.setObjectName("declinebutton")

        

        self.declinebutton.setGeometry(QtCore.QRect(290, 230, 93, 28))
        self.declinebutton.setObjectName("declinebutton")

        self.label = QtWidgets.QLabel(shutdownWindow)
        self.label.setGeometry(QtCore.QRect(20, 90, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(shutdownWindow)
        QtCore.QMetaObject.connectSlotsByName(shutdownWindow)

    def retranslateUi(self, shutdownWindow):
        _translate = QtCore.QCoreApplication.translate
        shutdownWindow.setWindowTitle(_translate("shutdownWindow", "Dialog"))
        self.acceptbutton.setText(_translate("shutdownWindow", "Yes"))
        self.declinebutton.setText(_translate("shutdownWindow", "No"))

        

        self.label.setText(_translate("shutdownWindow", "Do you really want to shutdown the system? Y/N"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shutdownWindow = QtWidgets.QMainWindow()
    ui = Ui_shutdownWindow()
    ui.setupUi(shutdownWindow)
    shutdownWindow.show()

    sys.exit(app.exec_())

    sys.exit(app.exec_())

