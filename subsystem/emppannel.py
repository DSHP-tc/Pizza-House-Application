# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emppannel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QButtonGroup, QTableWidgetItem



class Ui_EmpPannel(object):
    def setupUi(self, EmpPannel):
        if EmpPannel.objectName():
                EmpPannel.setObjectName("EmpPannel")
        EmpPannel.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/titleicon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EmpPannel.setWindowIcon(icon)
        EmpPannel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(EmpPannel)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(49, 39, 1840, 951))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(55, 55, 55);\n"
"border-radius: 50px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(790, 60, 1011, 831))
        self.frame_2.setStyleSheet("background-color: rgb(91, 88, 88);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(480, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(580, 70, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_cname = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_cname.setGeometry(QtCore.QRect(70, 120, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_cname.setFont(font)
        self.lineEdit_cname.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        self.lineEdit_cname.setObjectName("lineEdit_cname")
        self.lineEdit_ccontact = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_ccontact.setGeometry(QtCore.QRect(580, 120, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ccontact.setFont(font)
        self.lineEdit_ccontact.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        self.lineEdit_ccontact.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{10}")))
        self.lineEdit_ccontact.setObjectName("lineEdit_ccontact")
        self.group1=QButtonGroup(self.frame_2)
        self.group2=QButtonGroup(self.frame_2)
        self.radioButton_dinein = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_dinein.setGeometry(QtCore.QRect(80, 170, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_dinein.setFont(font)
        self.radioButton_dinein.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_dinein.setObjectName("radioButton_dinein")
        self.radioButton_take = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_take.setGeometry(QtCore.QRect(460, 170, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_take.setFont(font)
        self.radioButton_take.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_take.setObjectName("radioButton_take")
        self.radioButton_del = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_del.setGeometry(QtCore.QRect(850, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_del.setFont(font)
        self.radioButton_del.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_del.setObjectName("radioButton_del")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_cadd = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_cadd.setGeometry(QtCore.QRect(70, 260, 881, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_cadd.setFont(font)
        self.lineEdit_cadd.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        self.lineEdit_cadd.setObjectName("lineEdit_cadd")
        self.radioButton_cp = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_cp.setGeometry(QtCore.QRect(460, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_cp.setFont(font)
        self.radioButton_cp.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_cp.setObjectName("radioButton_cp")
        self.radioButton_op = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_op.setGeometry(QtCore.QRect(80, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_op.setFont(font)
        self.radioButton_op.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_op.setObjectName("radioButton_op")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(80, 360, 871, 375))
        self.tableWidget.setStyleSheet("background-color: rgb(174, 173, 173);")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Item")) 
        self.tableWidget.setItem(0,1, QTableWidgetItem("Extras"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Qty")) 
        self.tableWidget.setItem(0,3, QTableWidgetItem("Price"))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_order = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_order.setGeometry(QtCore.QRect(440, 770, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_order.setFont(font)
        self.pushButton_order.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_order.setObjectName("pushButton_order")

        self.pushButton_delitem = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_delitem.setGeometry(QtCore.QRect(700, 770, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_delitem.setFont(font)
        self.pushButton_delitem.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_delitem.setObjectName("pushButton_delitem")




        self.pushButton_pizza = QtWidgets.QPushButton(self.frame)
        self.pushButton_pizza.setGeometry(QtCore.QRect(80, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_pizza.setFont(font)
        self.pushButton_pizza.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_pizza.setObjectName("pushButton_pizza")
        self.pushButton_pizzam = QtWidgets.QPushButton(self.frame)
        self.pushButton_pizzam.setGeometry(QtCore.QRect(460, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_pizzam.setFont(font)
        self.pushButton_pizzam.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_pizzam.setObjectName("pushButton_pizzam")
        self.pushButton_dsides = QtWidgets.QPushButton(self.frame)
        self.pushButton_dsides.setGeometry(QtCore.QRect(80, 700, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_dsides.setFont(font)
        self.pushButton_dsides.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_dsides.setObjectName("pushButton_dsides")
        self.pushButton_dessert = QtWidgets.QPushButton(self.frame)
        self.pushButton_dessert.setGeometry(QtCore.QRect(460, 700, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_dessert.setFont(font)
        self.pushButton_dessert.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_dessert.setObjectName("pushButton_dessert")
        self.pushButton_bev = QtWidgets.QPushButton(self.frame)
        self.pushButton_bev.setGeometry(QtCore.QRect(280, 410, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_bev.setFont(font)
        self.pushButton_bev.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_bev.setObjectName("pushButton_bev")
        self.label_showempid = QtWidgets.QLabel(self.centralwidget)
        self.label_showempid.setGeometry(QtCore.QRect(90, 10, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_showempid.setFont(font)
        self.label_showempid.setObjectName("label_showempid")

        self.group1.addButton(self.radioButton_del)
        self.group1.addButton(self.radioButton_dinein)
        self.group1.addButton(self.radioButton_take)
        self.group2.addButton(self.radioButton_cp)
        self.group2.addButton(self.radioButton_op)
        EmpPannel.setCentralWidget(self.centralwidget)


        self.retranslateUi(EmpPannel)
        QtCore.QMetaObject.connectSlotsByName(EmpPannel)

    def retranslateUi(self, EmpPannel):
        _translate = QtCore.QCoreApplication.translate
        EmpPannel.setWindowTitle(_translate("EmpPannel", "Pizza House"))
        self.label.setText(_translate("EmpPannel", "Cart"))
        self.label_2.setText(_translate("EmpPannel", "Name"))
        self.label_3.setText(_translate("EmpPannel", "Contact No."))
        self.radioButton_dinein.setText(_translate("EmpPannel", "Dine-in"))
        self.radioButton_take.setText(_translate("EmpPannel", "Takeaway"))
        self.radioButton_del.setText(_translate("EmpPannel", "Delivery"))
        self.label_4.setText(_translate("EmpPannel", "Address"))
        self.radioButton_cp.setText(_translate("EmpPannel", "Cash Payment"))
        self.radioButton_op.setText(_translate("EmpPannel", "Online Payment"))
        self.pushButton_order.setText(_translate("EmpPannel", "Place Order"))
        self.pushButton_delitem.setText(_translate("EmpPannel", "Delete"))
        self.pushButton_pizza.setText(_translate("EmpPannel", "Pizza"))
        self.pushButton_pizzam.setText(_translate("EmpPannel", "Pizza Mania"))
        self.pushButton_dsides.setText(_translate("EmpPannel", "Delicious Sides"))
        self.pushButton_dessert.setText(_translate("EmpPannel", "Dessert"))
        self.pushButton_bev.setText(_translate("EmpPannel", "Beverages"))
        self.label_showempid.setText(_translate("EmpPannel", "EMP ID"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     EmpPannel = QtWidgets.QMainWindow()
#     ui = Ui_EmpPannel()
#     ui.setupUi(EmpPannel)
#     EmpPannel.show()
#     sys.exit(app.exec_())
