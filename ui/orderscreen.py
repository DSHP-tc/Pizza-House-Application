# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_size = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_size.setGeometry(QtCore.QRect(100, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_size.setFont(font)
        self.comboBox_size.setStyleSheet("QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down{\n"
"border-style: None;\n"
"border-radius: 15px\n"
"}")
        self.comboBox_size.setObjectName("comboBox_size")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(40, 100, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 15px;\n"
"}")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_seacrh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seacrh.setGeometry(QtCore.QRect(550, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_seacrh.setFont(font)
        self.pushButton_seacrh.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_seacrh.setObjectName("pushButton_seacrh")
        self.lineEdit_qty = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_qty.setGeometry(QtCore.QRect(930, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_qty.setFont(font)
        self.lineEdit_qty.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.lineEdit_qty.setObjectName("lineEdit_qty")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(1120, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(880, 440, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1130, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.checkBox_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_cb.setGeometry(QtCore.QRect(880, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_cb.setFont(font)
        self.checkBox_cb.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_cb.setObjectName("checkBox_cb")
        self.checkBox_dcb = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_dcb.setGeometry(QtCore.QRect(880, 230, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_dcb.setFont(font)
        self.checkBox_dcb.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_dcb.setObjectName("checkBox_dcb")
        self.checkBox_fp = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_fp.setGeometry(QtCore.QRect(880, 260, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_fp.setFont(font)
        self.checkBox_fp.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_fp.setObjectName("checkBox_fp")
        self.checkBox_tc = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_tc.setGeometry(QtCore.QRect(880, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_tc.setFont(font)
        self.checkBox_tc.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_tc.setObjectName("checkBox_tc")
        self.checkBox_r = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_r.setGeometry(QtCore.QRect(880, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_r.setFont(font)
        self.checkBox_r.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_r.setObjectName("checkBox_r")
        self.checkBox_m = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_m.setGeometry(QtCore.QRect(880, 400, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_m.setFont(font)
        self.checkBox_m.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_m.setObjectName("checkBox_m")
        self.checkBox_cd = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_cd.setGeometry(QtCore.QRect(880, 480, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_cd.setFont(font)
        self.checkBox_cd.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_cd.setObjectName("checkBox_cd")
        self.checkBox_md = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_md.setGeometry(QtCore.QRect(880, 510, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_md.setFont(font)
        self.checkBox_md.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_md.setObjectName("checkBox_md")
        self.checkBox_jp = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_jp.setGeometry(QtCore.QRect(880, 540, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_jp.setFont(font)
        self.checkBox_jp.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_jp.setObjectName("checkBox_jp")
        self.checkBox_td = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_td.setGeometry(QtCore.QRect(880, 570, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_td.setFont(font)
        self.checkBox_td.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_td.setObjectName("checkBox_td")
        self.checkBox_o = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_o.setGeometry(QtCore.QRect(1130, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_o.setFont(font)
        self.checkBox_o.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_o.setObjectName("checkBox_o")
        self.checkBox_c = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_c.setGeometry(QtCore.QRect(1130, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_c.setFont(font)
        self.checkBox_c.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_c.setObjectName("checkBox_c")
        self.checkBox_t = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_t.setGeometry(QtCore.QRect(1130, 250, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_t.setFont(font)
        self.checkBox_t.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_t.setObjectName("checkBox_t")
        self.checkBox_m_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_m_2.setGeometry(QtCore.QRect(1130, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_m_2.setFont(font)
        self.checkBox_m_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_m_2.setObjectName("checkBox_m_2")
        self.checkBox_gc = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gc.setGeometry(QtCore.QRect(1130, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_gc.setFont(font)
        self.checkBox_gc.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_gc.setObjectName("checkBox_gc")
        self.checkBox_p = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_p.setGeometry(QtCore.QRect(1130, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_p.setFont(font)
        self.checkBox_p.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_p.setObjectName("checkBox_p")
        self.checkBox_rp = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rp.setGeometry(QtCore.QRect(1130, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_rp.setFont(font)
        self.checkBox_rp.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_rp.setObjectName("checkBox_rp")
        self.checkBox_bo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_bo.setGeometry(QtCore.QRect(1130, 400, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_bo.setFont(font)
        self.checkBox_bo.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_bo.setObjectName("checkBox_bo")
        self.checkBox_ry = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ry.setGeometry(QtCore.QRect(1130, 430, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_ry.setFont(font)
        self.checkBox_ry.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_ry.setObjectName("checkBox_ry")
        self.checkBox_j = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_j.setGeometry(QtCore.QRect(1130, 460, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_j.setFont(font)
        self.checkBox_j.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_j.setObjectName("checkBox_j")
        self.checkBox_bc = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_bc.setGeometry(QtCore.QRect(1130, 490, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_bc.setFont(font)
        self.checkBox_bc.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_bc.setObjectName("checkBox_bc")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 160, 771, 571))
        self.listView.setStyleSheet("color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order Screen"))
        self.comboBox_size.setItemText(0, _translate("MainWindow", "Regular"))
        self.comboBox_size.setItemText(1, _translate("MainWindow", "Medium"))
        self.comboBox_size.setItemText(2, _translate("MainWindow", "Large"))
        self.label.setText(_translate("MainWindow", "Size:"))
        self.pushButton_seacrh.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Qty:"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Crust"))
        self.label_4.setText(_translate("MainWindow", "Extra Cheese"))
        self.label_5.setText(_translate("MainWindow", "Dips"))
        self.label_6.setText(_translate("MainWindow", "Toppings"))
        self.checkBox_cb.setText(_translate("MainWindow", "Cheese Burst"))
        self.checkBox_dcb.setText(_translate("MainWindow", "Double Cheese Burst"))
        self.checkBox_fp.setText(_translate("MainWindow", "Fresh Pan"))
        self.checkBox_tc.setText(_translate("MainWindow", "Thin Crust"))
        self.checkBox_r.setText(_translate("MainWindow", "Regular"))
        self.checkBox_m.setText(_translate("MainWindow", "Medium"))
        self.checkBox_cd.setText(_translate("MainWindow", "Cheese Dip"))
        self.checkBox_md.setText(_translate("MainWindow", "Mayonnaise Dip"))
        self.checkBox_jp.setText(_translate("MainWindow", "Jalapeno Dip"))
        self.checkBox_td.setText(_translate("MainWindow", "Tandori Dip"))
        self.checkBox_o.setText(_translate("MainWindow", "Onion"))
        self.checkBox_c.setText(_translate("MainWindow", "Capcicum"))
        self.checkBox_t.setText(_translate("MainWindow", "Tamato"))
        self.checkBox_m_2.setText(_translate("MainWindow", "Mushroom"))
        self.checkBox_gc.setText(_translate("MainWindow", "Golden Corn"))
        self.checkBox_p.setText(_translate("MainWindow", "Paneer"))
        self.checkBox_rp.setText(_translate("MainWindow", "Red Peprika"))
        self.checkBox_bo.setText(_translate("MainWindow", "Black Olive"))
        self.checkBox_ry.setText(_translate("MainWindow", "R&Y Black Pepper"))
        self.checkBox_j.setText(_translate("MainWindow", "Jalapeno"))
        self.checkBox_bc.setText(_translate("MainWindow", "Baby Corn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
