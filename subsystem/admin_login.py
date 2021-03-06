# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminLogin(object):
    def setupUi(self, AdminLogin):
        if AdminLogin.objectName():
                AdminLogin.setObjectName("AdminLogin")
        AdminLogin.resize(1280, 720)
        AdminLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AdminLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/pannel.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(657, 70, 601, 3))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(720, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 102, 0);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_auserid = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_auserid.setGeometry(QtCore.QRect(720, 280, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_auserid.setFont(font)
        self.lineEdit_auserid.setObjectName("lineEdit_auserid")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 102, 0);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_apass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_apass.setGeometry(QtCore.QRect(720, 380, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_apass.setFont(font)
        self.lineEdit_apass.setInputMask("")
        self.lineEdit_apass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_apass.setObjectName("lineEdit_apass")
        self.pushButton_aback = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_aback.setGeometry(QtCore.QRect(720, 530, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_aback.setFont(font)
        self.pushButton_aback.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"border-style: None;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"")
        self.pushButton_aback.setObjectName("pushButton_aback")
        self.pushButton_alogin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_alogin.setGeometry(QtCore.QRect(1070, 530, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_alogin.setFont(font)
        self.pushButton_alogin.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"border-style: None;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"")
        self.pushButton_alogin.setObjectName("pushButton_alogin")
        self.pushButton_fpass = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fpass.setGeometry(QtCore.QRect(720, 430, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_fpass.setFont(font)
        self.pushButton_fpass.setStyleSheet("QPushButton{\n"
"\n"
"text-align: left;\n"
"color: rgb(255, 159, 51);\n"
"    background-color: rgb(255, 255, 255);\n"
"border-style: None;\n"
"\n"
"}")
        self.pushButton_fpass.setObjectName("pushButton_fpass")
        AdminLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminLogin)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)

    def retranslateUi(self, AdminLogin):
        _translate = QtCore.QCoreApplication.translate
        AdminLogin.setWindowTitle(_translate("AdminLogin", "Pizza House"))
        AdminLogin.setWindowIcon(QtGui.QIcon("img/titleicon.jpeg"))
        self.label_2.setText(_translate("AdminLogin", "Admin"))
        self.label_3.setText(_translate("AdminLogin", "User Id"))
        self.label_4.setText(_translate("AdminLogin", "Password"))
        self.pushButton_aback.setText(_translate("AdminLogin", "Back"))
        self.pushButton_alogin.setText(_translate("AdminLogin", "Login"))
        self.pushButton_alogin.setShortcut(_translate("AdminLogin","Return"))
        self.pushButton_aback.setShortcut(_translate("AdminLogin","Escape"))
        self.pushButton_fpass.setText(_translate("AdminLogin", "Forgot Password"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
