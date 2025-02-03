from PyQt6 import QtCore, QtGui, QtWidgets
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox,QApplication,QWidget
import sqlite3
import csv


#to connect and create db
from ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):  # Make sure MainWindow inherits from QMainWindow or QWidget
    def __init__(self):
         super().__init__()
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)  # Pass self (MainWindow) to setupUi method


#==========================================================
         #create database
         database = QSqlDatabase.addDatabase("QSQLITE")
         database.setDatabaseName('main.db')

         if database.open():
         # Get the database name
          database_name = database.databaseName()
          print("Database Name:", database_name)
         else:
             print("Failed to open the database")

         query = QSqlQuery()    
         query.exec(""" 
                    CREATE TABLE IF NOT EXISTS task(
                    Sno INTEGER PRIMARY KEY AUTOINCREMENT,
                    Task TEXT
                    )""")
         
#========================================================================     
         def l_table():
          self.ui.table.setRowCount(0)
          query = QSqlQuery("SELECT * FROM task")
          row = 0
          while query.next():
            Id = query.value(0)
            tsk = query.value(1)

            #ADD VALUes into table
            self.ui.table.insertRow(row)
            #self.ui.table.setItem(row, 0,self.ui.item(str(Id)))
            item = QtWidgets.QTableWidgetItem(str(Id))  # Create a new QTableWidgetItem
            self.ui.table.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(str(tsk))
            self.ui.table.setItem(row, 1,item)
            row += 1
      
        #to show the all previous data in data.db
#===============================================================
        #add all things which are going to be insert in database
        #it extract the data from input and put it on database
       
         def insert():
           task =  self.ui.box2.text()
           query = QSqlQuery()
           query.prepare("""INSERT INTO task(task)
                            VALUES (?)""")
           query.addBindValue(task)
           query.exec()
           self.ui.box2.clear()
           l_table()

      
         def delete():
            select_row = self.ui.table.currentRow()
            if select_row == -1:
              print("please select row")
            else:
             Id = int(self.ui.table.item(select_row,0).text())
             print(Id)

             query = QSqlQuery()
            # SQL query to delete a row where the id is 5 (for example)
             query.prepare("DELETE FROM task WHERE Sno = :Sno")
             query.bindValue(":Sno", Id)  # Bind the value for the placeholder
             # Execute the query
             if query.exec():
               print("Row deleted successfully")

            l_table()


         def update():
          task =  self.ui.box2.text()
          select_row = self.ui.table.currentRow()
          if select_row == -1:
              print("please select row")
          else:
             Id = int(self.ui.table.item(select_row,0).text())

             query = QSqlQuery()
             print(task)
             query.prepare("UPDATE task SET task = :task WHERE Sno = :Sno")
             query.bindValue(":Sno", Id)
             query.bindValue(":task", task)
             if query.exec():
                self.ui.box2.clear()
                print("Row updated successfully")
          l_table()


         def clear():
             query = QSqlQuery()
             query.prepare("DROP TABLE IF EXISTS task")
             query.exec() 
             query.exec(""" 
                    CREATE TABLE IF NOT EXISTS task(
                    Sno INTEGER PRIMARY KEY AUTOINCREMENT,
                    Task TEXT
                    )""")
            
             l_table()

         def save():
            query = QSqlQuery()
            # SQL query to select all rows from the table
            query.prepare("SELECT * FROM task")
            # Execute the query
            if query.exec():
            # Open the CSV file to write
               with open('output.csv', mode='w', newline='') as file:
                  writer = csv.writer(file)
                  # Write column headers (get column names)
                  columns = [query.record().fieldName(i) for i in range(query.record().count())]
                  writer.writerow(columns)
                  # Write all rows
                  rows = []
                  while query.next():
                     row = [query.value(i) for i in range(query.record().count())]
                     rows.append(row)
                  # Write all rows at once
                  writer.writerows(rows)

               print("All data has been saved to output.csv")
            else:
             print("Failed to execute query:", query.lastError().text())
             print("Failed to connect to the database")



         l_table()
        #events
        # self.ui.btn1.clicked.connect(add)
         self.ui.btn1.clicked.connect(insert)
         self.ui.btn2.clicked.connect(update)
         self.ui.btn3.clicked.connect(clear)
         self.ui.btn4.clicked.connect(delete)
         self.ui.btn5.clicked.connect(save)


# Now continue with your main script
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()  # This will now work correctly
    window.show()
    app.exec()
