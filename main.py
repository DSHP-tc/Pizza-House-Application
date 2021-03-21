#importing modules


from subsystem.emp_login import Ui_EmpLoginWindow
from subsystem.admin_login import Ui_AdminLogin
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtWidgets import  QTableWidgetItem
import sys
from subsystem.splash import Ui_SplashScreen
from subsystem.login import Ui_LoginWindow
from subsystem.emp_login import Ui_EmpLoginWindow
from subsystem.adminpannel import Ui_AdminPannel
from subsystem.createemp import Ui_AddEmp
from subsystem.addmenu import Ui_AddMenu
from subsystem.emppannel import Ui_EmpPannel
from subsystem.orderscreen import Ui_OrderScreen
from subsystem.bill_preview import Ui_Bill_Preview
import sqlite3
from datetime import datetime
from xlsxwriter.workbook import Workbook

#globals
print("Starting")
counter=0
admin_id="pizzahouse"
admin_pass="123"
row=0
grand_total=0
bill_list=[]
cur_ordernum=0


class BillPreview(QMainWindow):
    def __init__(self,cus_name,cus_con,cur_order,dbmenu,ordtype,paytype,address,empid):
        global bill_list
        global grand_total
        global cur_ordernum
        QMainWindow.__init__(self)
        self.ui=Ui_Bill_Preview()
        self.ui.setupUi(self)
        print(bill_list)
        self.labelcounter=0
        self.cname=cus_name
        self.ccontact=cus_con
        self.cur_order=cur_order
        self.ord_string=""
        self.db_menu=dbmenu
        self.ordtype=ordtype
        self.paytype=paytype
        self.address=address
        self.empid=empid
        
        
        # self.today=date.today()
        # self.date=self.today.strftime("%d/%m/%Y")
        # self.curtime=time.
        self.date_time= datetime.now()
        self.date=self.date_time.strftime("%d/%m/%Y")
        self.time=self.date_time.strftime("%H:%M:%S")
        self.ypos=210
  

        for i in range(0,len(bill_list)):
            if bill_list[i]["Extra"]=="":
                self.ui.label_dict[str(i)+'s']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}s"].setGeometry(QtCore.QRect(10, self.ypos, 16, 16))
                self.ui.label_dict[f"{i}s"].setObjectName(str(i)+'s')
                self.ui.label_dict[f"{i}s"].setText(f"{i+1}")

                self.ui.label_dict[str(i)+'n']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}n"].setGeometry(QtCore.QRect(30, self.ypos, 81, 16))
                self.ui.label_dict[f"{i}n"].setObjectName(str(i)+'n')
                self.ui.label_dict[f"{i}n"].setText(bill_list[i]["Name"])

                self.ui.label_dict[str(i)+'q']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}q"].setGeometry(QtCore.QRect(120, self.ypos, 21, 16))
                self.ui.label_dict[f"{i}q"].setObjectName(str(i)+'q')
                self.ui.label_dict[f"{i}q"].setText(bill_list[i]["Qty"])

                self.ui.label_dict[str(i)+'a']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}a"].setGeometry(QtCore.QRect(150, self.ypos, 41, 16))
                self.ui.label_dict[f"{i}a"].setObjectName(str(i)+'a')
                self.ui.label_dict[f"{i}a"].setText(bill_list[i]["Amount"])


                self.ypos+=20
            else:
                self.ui.label_dict[str(i)+'s']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}s"].setGeometry(QtCore.QRect(10, self.ypos, 16, 16))
                self.ui.label_dict[f"{i}s"].setObjectName(str(i)+'s')
                self.ui.label_dict[f"{i}s"].setText(f"{i+1}")

                self.ui.label_dict[str(i)+'n']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}n"].setGeometry(QtCore.QRect(30, self.ypos, 81, 16))
                self.ui.label_dict[f"{i}n"].setObjectName(str(i)+'n')
                self.ui.label_dict[f"{i}n"].setText(bill_list[i]["Name"])

                self.ui.label_dict[str(i)+'q']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}q"].setGeometry(QtCore.QRect(120, self.ypos, 21, 16))
                self.ui.label_dict[f"{i}q"].setObjectName(str(i)+'q')
                self.ui.label_dict[f"{i}q"].setText(bill_list[i]["Qty"])

                self.ui.label_dict[str(i)+'a']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}a"].setGeometry(QtCore.QRect(150, self.ypos, 41, 16))
                self.ui.label_dict[f"{i}a"].setObjectName(str(i)+'a')
                self.ui.label_dict[f"{i}a"].setText(bill_list[i]["Amount"])

                self.ypos+=20
                self.ui.label_dict[str(i)+'e']=QtWidgets.QLabel(self.ui.centralwidget)
                self.ui.label_dict[f"{i}e"].setGeometry(QtCore.QRect(30, self.ypos, 81, 16))
                self.ui.label_dict[f"{i}e"].setObjectName(str(i)+"e")
                self.ui.label_dict[f"{i}e"].setText(bill_list[i]["Extra"])
                self.ypos+=20
        self.ui.label_total.setGeometry(QtCore.QRect(10, self.ypos, 71, 16))
        self.ui.label_total.setText(f"Total : {grand_total}")
        
        self.ui.label.setGeometry(QtCore.QRect(20, self.ypos+20, 161, 21))
        self.ui.label_cname.setText(self.cname)
        self.ui.label_date.setText(f"Date: {self.date}")
        self.ui.label_mob.setText(f"Mob: {self.ccontact}")
        self.ui.label_time.setText(f"Time: {self.time}")
        self.ui.label_ordernum.setText(f"Ord No.: {cur_ordernum}")

        for i in range(0,len(bill_list)):
            self.ord_string+=f"{bill_list[i]},"

        print("ord str:",self.ord_string)

        self.cur_order.execute("INSERT INTO order_table VALUES(?,?,?,?,?,?,?,?,?,?,?)",(cur_ordernum,self.cname,self.ccontact,self.ord_string,self.time,self.date,grand_total,self.ordtype,self.paytype,self.address,self.empid))
        self.db_menu.commit()
        grand_total=0
        self.resize(200,self.ypos+50)
        self.show()
        self.printer = QtPrintSupport.QPrinter()
        # Create painter
        self.painter = QtGui.QPainter()
        # Start painter
        self.painter.begin(self.printer)
        # Grab a widget you want to print
        self.screen = self.grab()
        # Draw grabbed pixmap
        self.painter.drawPixmap(-8, 0, self.screen)
        # End painting
        self.painter.end()


        
        





class OrderScr(QMainWindow):
    def __init__(self,table_widget,eobj,cur_menudb,cur_extrasdb,item_data,wintitle):

        QMainWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui=Ui_OrderScreen()
        self.ui.setupUi(self)
        self.extrastr=""
        self.table_widget=table_widget
        self.empobj=eobj
        self.cur_extrasdb=cur_extrasdb
        self.cur_menudb=cur_menudb
        self.item_data=item_data
        self.extras=["cb","dcb","fp","tc","r","m","cd","md","jp","td","o","c","t","mr","gc","p","rp","bo","ry","j","bc"]
        self.item_list=[]
        self.total=0
        for i in self.item_data:
            self.item_list.append(i[0])

        self.ui.listWidget.addItems(self.item_list)
        self.setWindowTitle(wintitle)
        self.ui.pushButton_seacrh.pressed.connect(lambda: self.itemsearch())
        self.ui.pushButton_add.pressed.connect(lambda: self.additem())
        self.ui.listWidget.clicked.connect(lambda: self.getitem())
        self.ui.lineEdit_search.textChanged.connect(lambda: self.itemsearch())

    def getitem(self):
        self.item=self.ui.listWidget.currentItem()

    def itemsearch(self):
        self.ui.listWidget.clear()
        self.item_temp=[]
        for i in self.item_data:
            if self.ui.lineEdit_search.text().lower() in i[0].lower() and self.ui.comboBox_size.currentText()[0]==i[2]:
                print("Item Found")
                self.item_temp.append(i[0])
        self.ui.listWidget.addItems(self.item_temp)

    def additem(self):
        if self.ui.listWidget.currentItem()!=None:
            global bill_list
            global grand_total
            global row
            row+=1
            self.table_widget.setRowCount(row+1)
            print("Running",self.item.text())
            
            for i in self.item_data:
                if self.item.text()==i[0]:
                    self.total=i[1]
            
            for i in self.extras:
                if getattr(self.ui,"checkBox_%s"%i).isChecked():
                    self.cur_extrasdb.execute("SELECT Price FROM extras_db WHERE Addon=? AND Size=?",(i,self.ui.comboBox_size.currentText()[0],))
                    # print(self.cur_extrasdb.fetchone()[0])
                    
                    self.extrastr=self.extrastr+"_"+i
                    self.total+=self.cur_extrasdb.fetchone()[0]
            
            self.total*=float(self.ui.lineEdit_qty.text())

            if self.ui.lineEdit_peroff.text()!="0":
                self.total=(self.total*(100-float(self.ui.lineEdit_peroff.text())))/100
            elif self.ui.lineEdit_priceoff.text()!="0":
                self.total=self.total-float(self.ui.lineEdit_priceoff.text())



            print(self.total)

            self.empobj.ui.tableWidget.setItem(row,0, QTableWidgetItem(self.item.text())) 
            self.empobj.ui.tableWidget.setItem(row,1, QTableWidgetItem(self.extrastr))
            self.empobj.ui.tableWidget.setItem(row,2, QTableWidgetItem(self.ui.lineEdit_qty.text())) 
            self.empobj.ui.tableWidget.setItem(row,3, QTableWidgetItem(str(self.total)))

            bill_list.append({"Name":self.item.text(),"Extra":self.extrastr,"Qty":self.ui.lineEdit_qty.text(),"Amount":str(self.total)})

            self.ui.comboBox_size.setCurrentIndex(0)
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.item_list)
            self.ui.lineEdit_qty.setText("1")
            self.extrastr=""
            self.ui.lineEdit_search.clear()
            self.ui.lineEdit_priceoff.setText("0")
            self.ui.lineEdit_peroff.setText("0")
            
            for i in self.extras:
                getattr(self.ui,"checkBox_%s"%i).setChecked(False)
        else: 
            pass

    
        


class EmpScreen(QMainWindow):
    def __init__(self,empid):
        QMainWindow.__init__(self)
        self.ui=Ui_EmpPannel()
        self.ui.setupUi(self)
        
        self.db_menu=sqlite3.connect("db/menu_database.db")
        self.cur_menudb=self.db_menu.cursor()
        self.cur_extradb=self.db_menu.cursor()
        self.cur_order=self.db_menu.cursor()
        self.empid=empid
        self.ui.label_showempid.setText(empid)
        self.date_time= datetime.now()
        self.date=self.date_time.strftime("%d-%m-%Y")
        self.workbook=Workbook(f"order_files/{self.date}.xlsx")
        self.worksheet=self.workbook.add_worksheet("New")
        
        self.worksheet.write(0,0,"Ord No")
        self.worksheet.write(0,1,"Customer Name")
        self.worksheet.write(0,2,"Mob")
        self.worksheet.write(0,3,"Items")
        self.worksheet.write(0,4,"Time")
        self.worksheet.write(0,5,"Date")
        self.worksheet.write(0,6,"Grand Total")
        self.worksheet.write(0,7,"Order Type")
        self.worksheet.write(0,8,"Payment Type")
        self.worksheet.write(0,9,"Address")
        self.worksheet.write(0,10,"Employee Id")
      
        self.ui.pushButton_delitem.pressed.connect(lambda: self.itemdel())
       
        self.ui.pushButton_order.setDisabled(True)
        self.ui.lineEdit_cadd.setText("None")
        self.ui.pushButton_order.setStyleSheet("QPushButton{\n"
"background-color: rgb(142,119,94);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.ui.pushButton_pizza.pressed.connect(lambda: self.pizza())
        self.ui.pushButton_pizzam.pressed.connect(lambda: self.pizzam())
        self.ui.pushButton_bev.pressed.connect(lambda: self.bev())
        self.ui.pushButton_dessert.pressed.connect(lambda: self.des())
        self.ui.pushButton_dsides.pressed.connect(lambda: self.dside())
        self.ui.pushButton_order.pressed.connect(lambda: self.order())
        self.ui.lineEdit_cadd.setDisabled(True)
        self.ui.lineEdit_cadd.setStyleSheet("QLineEdit{\n"
"background-color: rgb(174, 173, 173);\n"
"border-radius: 15px;\n"
"}")
        
        self.ui.radioButton_del.toggled.connect(lambda: self.delcheck())
 
        self.ui.lineEdit_ccontact.editingFinished.connect(lambda: self.cconchanged())

    def closeEvent(self,event):
        self.mysel=self.cur_order.execute("SELECT * FROM order_table")
       
        for i, tablerow in enumerate(self.mysel):
            for j,value in enumerate(tablerow):
                self.worksheet.write(i+1,j,value)
        self.workbook.close()
        self.cur_order.execute("DELETE FROM order_table;")
        self.db_menu.commit()
        event.accept()

    def itemdel(self):
        global bill_list
        global row
        self.rows = sorted(list(index.row() for index in self.ui.tableWidget.selectedIndexes()))
        print(self.rows)
        for currow in self.rows:
            self.ui.tableWidget.removeRow(currow)
            row-=1
            for i in range(0,len(self.rows)):
                self.rows[i]=self.rows[i]-1
            bill_list.pop(currow-1)


    def cconchanged(self):
        if self.ui.lineEdit_cname.text()!="" and self.ui.lineEdit_ccontact.text()!="":
            self.ui.pushButton_order.setEnabled(True)
            self.ui.pushButton_order.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 159, 51);\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")

    def order(self):
        
        if self.ui.lineEdit_ccontact.text()!="" and self.ui.lineEdit_cname.text()!="":
            global bill_list
            global grand_total
            global row
            global cur_ordernum
            cur_ordernum+=1
            row=0
            for i in range(0,len(bill_list)):
                grand_total+=float(bill_list[i]["Amount"])

            print("Grand Total:",grand_total)

            if self.ui.radioButton_dinein.isChecked():
                self.ordtype="Dine-In"
            elif self.ui.radioButton_take.isChecked():
                self.ordtype="Take-away"

            if self.ui.radioButton_cp.isChecked():
                self.paytype="Cash Payment"
            elif self.ui.radioButton_op.isChecked():
                self.paytype="Online Payment"


            self.bill=BillPreview(self.ui.lineEdit_cname.text(),self.ui.lineEdit_ccontact.text(),self.cur_order,self.db_menu,self.ordtype,self.paytype,self.ui.lineEdit_cadd.text(),self.empid)
            
            bill_list.clear()
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setItem(0,0, QTableWidgetItem("Item")) 
            self.ui.tableWidget.setItem(0,1, QTableWidgetItem("Extras"))
            self.ui.tableWidget.setItem(0,2, QTableWidgetItem("Qty")) 
            self.ui.tableWidget.setItem(0,3, QTableWidgetItem("Price"))
            self.ui.lineEdit_cname.clear()
            self.ui.lineEdit_ccontact.clear()
            self.ui.lineEdit_cadd.clear()
            self.ui.group1.setExclusive(False)
            self.ui.group2.setExclusive(False)
            self.ui.radioButton_del.setChecked(False)
            self.ui.radioButton_dinein.setChecked(False)
            self.ui.radioButton_take.setChecked(False)
            self.ui.radioButton_op.setChecked(False)
            self.ui.radioButton_cp.setChecked(False)
            self.ui.group1.setExclusive(True)
            self.ui.group2.setExclusive(True)
            self.ui.pushButton_order.setDisabled(True)
            self.ui.lineEdit_cname.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
            self.ui.lineEdit_ccontact.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
            self.ui.pushButton_order.setStyleSheet("QPushButton{\n"
    "background-color: rgb(142,119,94);\n"
    "    color: rgb(0, 0, 0);\n"
    "border-radius: 20px;\n"
    "}")
        else:
            self.ui.lineEdit_cname.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid red;\n"
"}")
            self.ui.lineEdit_ccontact.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid red;\n"
"}")


        



    def delcheck(self):
        if self.ui.radioButton_del.isChecked():
            self.ordtype="Delivery"
            self.ui.lineEdit_cadd.setEnabled(True)
            self.ui.lineEdit_cadd.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        else:
            self.ui.lineEdit_cadd.setStyleSheet("QLineEdit{\n"
"background-color: rgb(174, 173, 173);\n"
"border-radius: 15px;\n"
"}")
            self.ui.lineEdit_cadd.setDisabled(True)    

    def pizza(self):
        self.cur_menudb.execute("SELECT item_name, price, size FROM menu_db WHERE category='Pizza'")
        self.item_data=self.cur_menudb.fetchall()
        print(self.item_data)
        self.ordscr=OrderScr(self.ui.tableWidget,self,self.cur_menudb,self.cur_extradb,self.item_data,"Pizza")
        self.ordscr.show()
        

        
    def pizzam(self):
        self.cur_menudb.execute("SELECT item_name, price, size FROM menu_db WHERE category='Pizza Mania'")
        self.item_data=self.cur_menudb.fetchall()
        print(self.item_data)
        self.ordscr=OrderScr(self.ui.tableWidget,self,self.cur_menudb,self.cur_extradb,self.item_data,"Pizza Mania")
        self.ordscr.show()
        

    def bev(self):
        self.cur_menudb.execute("SELECT item_name, price, size FROM menu_db WHERE category='Beverages'")
        self.item_data=self.cur_menudb.fetchall()
        print(self.item_data)
        self.ordscr=OrderScr(self.ui.tableWidget,self,self.cur_menudb,self.cur_extradb,self.item_data,"Beverages")
        self.ordscr.show()
        
    def des(self):
        self.cur_menudb.execute("SELECT item_name, price, size FROM menu_db WHERE category='Desserts'")
        self.item_data=self.cur_menudb.fetchall()
        print(self.item_data)
        self.ordscr=OrderScr(self.ui.tableWidget,self,self.cur_menudb,self.cur_extradb,self.item_data,"Desserts")
        self.ordscr.show()
        
    def dside(self):
        self.cur_menudb.execute("SELECT item_name, price, size FROM menu_db WHERE category='Delicious Sides'")
        self.item_data=self.cur_menudb.fetchall()
        print(self.item_data)
        self.ordscr=OrderScr(self.ui.tableWidget,self,self.cur_menudb,self.cur_extradb,self.item_data,"Delicious Sides")
        self.ordscr.show()
        
class AddMenuItem(QMainWindow):
    def __init__(self,cur,dbmenu):
        QMainWindow.__init__(self)
        self.ui=Ui_AddMenu()
        self.ui.setupUi(self)
        self.cur_menu=cur
        self.db_menu=dbmenu

        self.ui.pushButton_additem.pressed.connect(lambda: self.menuadder())


    def menuadder(self):
        self.ui.lineEdit_price.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border-style: None;\n""border-radius: 15px;\n""}\n""")
        self.ui.lineEdit_additem.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border-style: None;\n""border-radius: 15px;\n""}")
        if self.ui.lineEdit_additem.text()=="" or self.ui.lineEdit_price.text()=="":
            self.ui.lineEdit_price.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border: 3px solid red;\n""border-radius: 15px;\n""}\n""")
            self.ui.lineEdit_additem.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border: 3px solid red;\n""border-radius: 15px;\n""}")
        else:
            try:
                self.cur_menu.execute("INSERT INTO menu_db VALUES(?,?,?,?,?);",(self.ui.lineEdit_additem.text(),self.ui.comboBox_category.currentText(),self.ui.comboBox_category_2.currentText(),self.ui.lineEdit_price.text(),self.ui.lineEdit_additem.text()[-1]))
                self.db_menu.commit()
                self.ui.lineEdit_additem.clear()
                self.ui.lineEdit_price.clear()
                self.ui.comboBox_category.setCurrentIndex(0)
                self.ui.comboBox_category_2.setCurrentIndex(0)
            except sqlite3.IntegrityError :
                self.ui.lineEdit_additem.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border: 3px solid red;\n""border-radius: 15px;\n""}")
                self.ui.lineEdit_additem.clear()
                self.ui.lineEdit_price.clear()
                self.ui.comboBox_category.setCurrentIndex(0)
                self.ui.comboBox_category_2.setCurrentIndex(0)




#class for creating and adding new employees
class AddEmp(QMainWindow):
    def __init__(self,cur,dbemp):
        QMainWindow.__init__(self)
        self.ui=Ui_AddEmp()
        self.ui.setupUi(self)
        self.cur_empdb=cur
        self.db_emp=dbemp
        self.imgbdata=0
        self.linecontainer=["fempname","fcontact","faadhar","fpost","fempid","femppass"]
        #Connecting Buttons

        self.ui.pushButton_upimg.pressed.connect(lambda: self.openimg())
        self.ui.pushButton_createpro.pressed.connect(lambda: self.createemppro())
    #Opening image through the file browser
    def openimg(self):
        self.filepath=QFileDialog.getOpenFileName(self,"Single File","This PC","Image File(*.jpeg *.jpg *.png)")
        print(self.filepath)

        
        self.pixmap=QtGui.QPixmap(self.filepath[0])
        self.ui.label_empimg.setPixmap(self.pixmap)
        self.ui.label_empimg.setScaledContents(True)

        with open(self.filepath[0],"rb") as file:
            self.imgbdata=file.read()
    #function for creating the employee profile
    def createemppro(self):
        for n in self.linecontainer:
            getattr(self.ui,"lineEdit_%s"%n).setStyleSheet("QLineEdit{\n""border-radius: 20px;\n""\n""}")
        
        print("create prof working")
        if self.ui.lineEdit_fempname.text()!="" and self.ui.lineEdit_fcontact.text()!="" and self.ui.lineEdit_faadhar.text()!="" and self.ui.lineEdit_fpost.text()!="" and self.ui.lineEdit_fempid.text()!="" and self.ui.lineEdit_femppass.text()!="":
            try:
                self.cur_empdb.execute("INSERT INTO emp_db VALUES(?,?,?,?,?,?,?);",(self.ui.lineEdit_fempname.text(),self.ui.lineEdit_fcontact.text(),self.ui.lineEdit_faadhar.text(),self.ui.lineEdit_fpost.text(),self.ui.lineEdit_fempid.text(),self.ui.lineEdit_femppass.text(),self.imgbdata))
                self.db_emp.commit()
                for n in self.linecontainer:
                    getattr(self.ui,"lineEdit_%s"%n).clear()
                self.imgbdata=0
                self.ui.label_empimg.clear()
            except sqlite3.IntegrityError:
                self.ui.lineEdit_fempid.setStyleSheet("QLineEdit{\n""border: 3px solid red;\n""border-radius: 20px;\n""\n""}")
                self.ui.lineEdit_fempid.clear()    
        else:
            for n in self.linecontainer:
                getattr(self.ui,"lineEdit_%s"%n).setStyleSheet("QLineEdit{\n""border: 3px solid red;\n""border-radius: 20px;\n""\n""}")





#class for making the admin pannel
class AdminPannel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_AdminPannel()
        self.ui.setupUi(self)
        self.db_emp=sqlite3.connect("db/emp_database.db")
        self.cur_empdb=self.db_emp.cursor()
        self.db_menu=sqlite3.connect("db/menu_database.db")
        self.cur_menudb=self.db_menu.cursor()


        self.ui.pushButton_addemp.pressed.connect(lambda: self.addemp())
        self.ui.pushButton_additems.pressed.connect(lambda: self.additems())

    def additems(self):
        self.additem=AddMenuItem(self.cur_menudb,self.db_menu)
        self.additem.show()

    def addemp(self):
        self.addemps=AddEmp(self.cur_empdb,self.db_emp)
        self.addemps.show()
        
#class for making employee login screen
class EmpLogin(QMainWindow):
    def __init__(self,obj):
        QMainWindow.__init__(self)
        self.ui=Ui_EmpLoginWindow()
        self.ui.setupUi(self)
        self.obj=obj
        self.db_emp=sqlite3.connect("db/emp_database.db")
        self.cur_empdb=self.db_emp.cursor()
        #connecting buttons
        self.ui.pushButton_eback.pressed.connect(lambda: self.elback())
        self.ui.pushButton_elogin.pressed.connect(lambda: self.emplogin())

    def emplogin(self):
        self.cur_empdb.execute("SELECT id FROM emp_db")
        self.id_data=self.cur_empdb.fetchall()   
        for i in self.id_data:
            if self.ui.lineEdit_euserid.text()==i[0]:
                print(i[0])
                self.cur_empdb.execute("SELECT pass FROM emp_db WHERE id=?",(i[0],))
                self.passwd=self.cur_empdb.fetchone()[0]
                if self.ui.lineEdit_epass.text()==self.passwd:
                    self.emppannel=EmpScreen(i[0])
                    self.emppannel.show()
                    # self.db_emp.close()
                    self.close()
                    break
                else:
                    self.ui.lineEdit_epass.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border: 3px solid red;\n""}\n""")
        else:
            self.ui.lineEdit_euserid.setStyleSheet("QLineEdit{\n""color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""border: 3px solid red;\n""}\n""")

        
    #back  function from employee screen
    def elback(self):
        self.obj.show()
        self.db_emp.close()
        
        self.close()

#class for making admin login screen
class AdminLogin(QMainWindow):
    def __init__(self,obj):
        QMainWindow.__init__(self)
        self.ui=Ui_AdminLogin()
        self.ui.setupUi(self)
        self.obj=obj
        #connecting buttons
        self.ui.pushButton_aback.pressed.connect(lambda : self.alback())
        self.ui.pushButton_alogin.pressed.connect(lambda : self.adlogin())
    #function for connecting admin button
    def adlogin(self):
        global admin_id
        global admin_pass
        print(self.ui.lineEdit_auserid.text())
        print(self.ui.lineEdit_apass.text())
        if self.ui.lineEdit_auserid.text()==admin_id and self.ui.lineEdit_apass.text()==admin_pass:
            print("login success")
            self.adminpannel=AdminPannel()
            self.adminpannel.show()
            self.close()
            self.obj.close()

        else:
            print("login failed")
    #function for connecting back button from admin login screen
    def alback(self):
        print("Back Working")
        self.obj.show()
        self.close()
        



#class for making the main login screen
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self)
        # self.db = sqlite3.connect("db/menu_database.db")
        # self.cur=self.db.cursor()
        # self.cur.execute("CREATE TABLE menu_db(item_name TEXT UNIQUE,category TEXT,subcategory TEXT,price REAL)")

        self.ui.pushButton_admin.pressed.connect(lambda : self.alscropen())
        self.ui.pushButton_emp.pressed.connect(lambda: self.elscropen())
    #function for opening employee login screen
    def elscropen(self):
        self.hide()
        self.emplogin=EmpLogin(self)
        self.emplogin.show()
    #function for opening admin login screen
    def alscropen(self):
        self.hide()
        self.adminlogin=AdminLogin(self)
        self.adminlogin.show()


#class for making splash screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
    
      ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)
        
       
       ## SHOW ==> Splash Screen
        ########################################################################
        self.show()
        
        
        ## ==> END ##

    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.login = LoginWindow()
            self.login.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1
    
        
          



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())