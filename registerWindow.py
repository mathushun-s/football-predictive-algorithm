from PyQt5 import QtCore, QtGui, QtWidgets
import db
import mainWindow
import loginWindow

class Ui_registerWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = loginWindow.Ui_loginWindow()
        self.ui.setupUi(self.window)
        QtWidgets.QDialog().hide()
        self.window.show()

    def signup(self):
        result = db.register(self.Username.text(), self.Password.text(), self.conPassword.text())
        self.outputMessage.setText(result)
    
    def setupUi(self, registerWindow):
        registerWindow.setObjectName("registerWindow")
        registerWindow.resize(326, 240)
        registerWindow.setWindowIcon(QtGui.QIcon("football.png"))
        registerWindow.setMinimumSize(QtCore.QSize(326, 240))
        registerWindow.setMaximumSize(QtCore.QSize(326, 240))
        registerWindow.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.label_8 = QtWidgets.QLabel(registerWindow)
        self.label_8.setGeometry(QtCore.QRect(110, 60, 51, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.outputMessage = QtWidgets.QLabel(registerWindow)
        self.outputMessage.setGeometry(QtCore.QRect(110, 210, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputMessage.setFont(font)
        self.outputMessage.setAutoFillBackground(False)
        self.outputMessage.setStyleSheet("color: rgb(255, 0, 0);")
        self.outputMessage.setText("")
        self.outputMessage.setObjectName("outputMessage")
        self.label_5 = QtWidgets.QLabel(registerWindow)
        self.label_5.setGeometry(QtCore.QRect(100, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.registerBtn = QtWidgets.QPushButton(registerWindow)
        self.registerBtn.setGeometry(QtCore.QRect(110, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.registerBtn.setFont(font)
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5;")
        self.registerBtn.setObjectName("registerBtn")

        self.registerBtn.clicked.connect(self.signup)
        
        self.conPassword = QtWidgets.QLineEdit(registerWindow)
        self.conPassword.setGeometry(QtCore.QRect(110, 160, 113, 20))
        self.conPassword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3;")
        self.conPassword.setObjectName("conPassword")
        self.Username = QtWidgets.QLineEdit(registerWindow)
        self.Username.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.Username.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3;")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(registerWindow)
        self.Password.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.Password.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3;")
        self.Password.setObjectName("Password")
        self.label_6 = QtWidgets.QLabel(registerWindow)
        self.label_6.setGeometry(QtCore.QRect(110, 140, 91, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.loginWindowBtn = QtWidgets.QPushButton(registerWindow)
        self.loginWindowBtn.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.loginWindowBtn.setFont(font)
        self.loginWindowBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginWindowBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5;")
        self.loginWindowBtn.setObjectName("loginWindowBtn")

        self.loginWindowBtn.clicked.connect(self.openWindow)
        
        self.label_7 = QtWidgets.QLabel(registerWindow)
        self.label_7.setGeometry(QtCore.QRect(110, 100, 51, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(registerWindow)
        QtCore.QMetaObject.connectSlotsByName(registerWindow)

    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "Sign up"))
        self.label_8.setText(_translate("registerWindow", "Username:"))
        self.label_5.setText(_translate("registerWindow", "REGISTRATION"))
        self.registerBtn.setText(_translate("registerWindow", "REGISTER"))
        self.label_6.setText(_translate("registerWindow", "Confirm Password:"))
        self.loginWindowBtn.setText(_translate("registerWindow", "GO BACK"))
        self.label_7.setText(_translate("registerWindow", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerWindow = QtWidgets.QDialog()
    ui = Ui_registerWindow()
    ui.setupUi(registerWindow)
    registerWindow.show()
    sys.exit(app.exec_())
