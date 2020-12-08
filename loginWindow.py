from PyQt5 import QtCore, QtGui, QtWidgets
import db
import mainWindow
import registerWindow

class Ui_loginWindow(object):
    def openRegisterWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = registerWindow.Ui_registerWindow()
        self.ui.setupUi(self.window)
        QtWidgets.QMainWindow().close()
        self.window.show()

    def openMainWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = mainWindow.Ui_mainWindow()
        self.ui.setupUi(self.window)
        QtWidgets.QMainWindow().close()
        self.window.show()

    def signin(self):
        result = db.login(self.Username.text(), self.Password.text())
        if result == "Logged in":
            self.openMainWindow()
        else:
            self.outputMessage.setText(result)
      
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(326, 240)
        loginWindow.setMinimumSize(QtCore.QSize(326, 240))
        loginWindow.setWindowIcon(QtGui.QIcon("football.png"))
        loginWindow.setMaximumSize(QtCore.QSize(326, 240))
        loginWindow.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 51, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.Username.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3;")
        self.Username.setObjectName("Username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 51, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.Password.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3;")
        self.Password.setObjectName("Password")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.registerWindowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerWindowBtn.setGeometry(QtCore.QRect(250, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.registerWindowBtn.setFont(font)
        self.registerWindowBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerWindowBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5;")
        self.registerWindowBtn.setObjectName("registerWindowBtn")

        self.registerWindowBtn.clicked.connect(self.openRegisterWindow)
        
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(110, 150, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5;")
        self.loginBtn.setObjectName("loginBtn")

        self.loginBtn.clicked.connect(self.signin)
        
        self.outputMessage = QtWidgets.QLabel(self.centralwidget)
        self.outputMessage.setGeometry(QtCore.QRect(110, 170, 211, 20))
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
        self.label_2.raise_()
        self.Username.raise_()
        self.label.raise_()
        self.Password.raise_()
        self.label_4.raise_()
        self.loginBtn.raise_()
        self.outputMessage.raise_()
        self.registerWindowBtn.raise_()
        loginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Sign in"))
        self.label_2.setText(_translate("loginWindow", "Password:"))
        self.label.setText(_translate("loginWindow", "Username:"))
        self.label_4.setText(_translate("loginWindow", "LOGIN"))
        self.registerWindowBtn.setText(_translate("loginWindow", "SIGN UP"))
        self.loginBtn.setText(_translate("loginWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
