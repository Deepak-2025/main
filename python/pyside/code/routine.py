import sys
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow,QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery
#from routine import Ui_routine
import csv



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView,QLineEdit, QApplication, QFrame, QGridLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_routine(object):
    def setupUi(self, routine):
        if not routine.objectName():
            routine.setObjectName(u"routine")
        routine.resize(616, 557)
        routine.setStyleSheet(u"#app{\n"
"\n"
"background-color:#854f6c;\n"
"}\n"
"#date{\n"
"border:1px solid white;\n"
"border-radius:20px;\n"
"background-color:#522b5b;\n"
"color:white;\n"
"font-size:17px;\n"
"font-weight:bold;\n"
"}\n"
"#date:hover{\n"
"background-color:#f1916d;\n"
"color:black;\n"
"}\n"
"#btn1,#btn2,#btn3{\n"
"background-color:#552b5b;\n"
"color:black;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"border:2px solid #f1916d;\n"
"border-radius:15px;\n"
"}\n"

"\n"
"#box2{\n"
"background-color:#f5d7db;\n"
"color:black;\n"
"font-weight:bold;\n"
"}\n"

"#btn1:hover{\n"
"background-color:#f1916d;\n"
"}\n"
"#btn3:hover{\n"
"background-color:#f1916d;\n"
"}#btn2:hover{\n"
"background-color:#f1916d;\n"
"}\n"

"\n"
"#table{\n"
"margin-top:50px;\n"
"background-color:#f5d7db;\n"
"color:black;\n"
"gridline-color:black;\n"
"}\n"
"")
        self.app = QWidget(routine)
        self.app.setObjectName(u"app")
        self.formLayoutWidget_3 = QWidget(self.app)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 500, 571, 51))
        self.form1 = QGridLayout(self.formLayoutWidget_3)
        self.form1.setObjectName(u"form1")
        self.form1.setContentsMargins(0, 0, 0, 0)
        self.btn2 = QPushButton(self.formLayoutWidget_3)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMaximumSize(QSize(150, 150))
        self.btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.form1.addWidget(self.btn2, 0, 0, 1, 1)
        self.btn1 = QPushButton(self.formLayoutWidget_3)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMaximumSize(QSize(150, 150))
        self.btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.form1.addWidget(self.btn1, 0, 1, 1, 1)
        self.btn3 = QPushButton(self.formLayoutWidget_3)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMaximumSize(QSize(150, 150))
        self.btn3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.form1.addWidget(self.btn3, 0, 2, 1, 1)
        self.table = QTableWidget(self.app)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        self.it = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, self.it)
        self.it1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, self.it1)
        self.it2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, self.it2)
        if (self.table.rowCount() < 10):
            self.table.setRowCount(10)
            self.font = QFont()
            self.font.setFamilies([u"Sans Serif Collection"])
            self.font.setPointSize(15)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(21, 61, 571, 431))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif Collection"])
        self.table.setFont(font2)
        self.table.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table.setFrameShape(QFrame.Shape.StyledPanel)
        self.table.setAutoScroll(True)
        self.table.setAutoScrollMargin(16)
        self.table.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.table.setAlternatingRowColors(False)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.table.setShowGrid(True)
        self.table.setSortingEnabled(False)
        self.table.setCornerButtonEnabled(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.horizontalHeader().setDefaultSectionSize(100)
        self.table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setMinimumSectionSize(15)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.box2 = QLineEdit(self.app)
        self.box2.setObjectName(u"box2")
        self.box2.setGeometry(QRect(350, 77, 240, 30))
        self.box2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.box2.setText("")
        self.date = QLabel(self.app)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(21, 11, 571, 60))
        self.date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        routine.setCentralWidget(self.app)
        self.retranslateUi(routine)
        QMetaObject.connectSlotsByName(routine)
    # setupUi

    def retranslateUi(self, routine):
        routine.setWindowTitle(QCoreApplication.translate("routine", u"MainWindow", None))
        self.btn2.setText(QCoreApplication.translate("routine", u"ADD", None))
        self.btn1.setText(QCoreApplication.translate("routine", u"UPDATE", None))
        self.btn3.setText(QCoreApplication.translate("routine", u"SAVE", None))
        # Set table headers
        item = self.table.horizontalHeaderItem(0)
        item.setText(QCoreApplication.translate("routine", u"ID", None))
        item1 = self.table.horizontalHeaderItem(1)
        item1.setText(QCoreApplication.translate("routine", u"TIME", None))
        item2 = self.table.horizontalHeaderItem(2)
        item2.setText(QCoreApplication.translate("routine", u"WORK", None))
        self.date.setText(QCoreApplication.translate("routine", u"TextLabel", None))
    # retranslateUi

class routin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_routine()
        self.ui.setupUi(self)

        dt = QDateTime.currentDateTime()
        dat = dt.toString("dd/MM/yyyy")
        time = dt.toString("hh:mm:ss AP")
        self.ui.date.setText(dat + "\n" + time)

        #table header designing
        header = self.ui.table.horizontalHeader()
        header.setStyleSheet("QHeaderView::section{background-color:#522b5b;color:white;}")

#=====================================================
        # Create or connect to a SQLite database
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName('test.db')

        if database.open():
            #QMessageBox.information(self,"INFORMATION","database connected successfully")
            print("Database connected successfully.")
        else:
            QMessageBox.information(self,"ERROR","Failed to open the database")
            print("Failed to open the database")

        query = QSqlQuery()    
        query.exec("""
                    CREATE TABLE IF NOT EXISTS test(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time TEXT,
                    work TEXT
                    )""")

#=====================================================
        # Initialize the table with data from the database
        def l_table():
            self.ui.table.setRowCount(0)  

            query = QSqlQuery("SELECT * FROM test")
            row = 0
            while query.next():
                # Retrieve values from the query result
                d = query.value(0)  
                tm = query.value(1)  
                wrk = query.value(2)  

                # Insert a new row in the table
                self.ui.table.insertRow(row)

                # Create QTableWidgetItems for each column and set their text
                item = QTableWidgetItem(str(d))  
                self.ui.table.setItem(row, 0, item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(self.ui.font)

                item = QTableWidgetItem(str(tm))  
                self.ui.table.setItem(row, 1, item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(self.ui.font)

                item = QTableWidgetItem(str(wrk))  
                self.ui.table.setItem(row, 2, item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(self.ui.font)

                row += 1
#=====================================================
#=====================================================
        # Insert data into the table
        def insert():
            work = self.ui.box2.text()  
            time = self.ui.box2.text() 
            query = QSqlQuery()
            query.prepare("INSERT INTO test(time, work) VALUES (?, ?)")
            query.addBindValue(time)  #
            query.addBindValue(work) 

            if query.exec():  
                QMessageBox.information(self,"INFORMATION","NEW ROW CREATED SUCCESSFULLY")
                self.ui.box2.clear() 
                l_table()  
            else:
                QMessageBox.information(self,"ERROR","unable to create new row!")
#=====================================================
        # Update the selected row
        def update():
            work = self.ui.box2.text()
            select_row = self.ui.table.currentRow()
            select_column = self.ui.table.currentColumn()
            if select_row == -1 & select_column == -1:
                QMessageBox.information(self,"INFORMATION","Please select a cell to update.")
            elif select_column == 1:
                Id = int(self.ui.table.item(select_row,0).text())
                query = QSqlQuery()
                query.prepare("UPDATE test SET time = :time WHERE id = :id")
                query.bindValue(":id", Id)
                query.bindValue(":time", work)
                if query.exec():
                    self.ui.box2.clear()
                    QMessageBox.information(self,"success","data inserted successfully")
                    l_table() 
                else:
                    QMessageBox.information(self,"ERROR","failed to update data in time column!")
            elif select_column == 2:
                Id = int(self.ui.table.item(select_row, 0).text())
                query = QSqlQuery()
                query.prepare("UPDATE test SET work = :work WHERE id = :id")
                query.bindValue(":id", Id)
                query.bindValue(":work", work)
                if query.exec():
                    self.ui.box2.clear()
                    QMessageBox.information(self,"success","data inserted successfully")
                    l_table() 
                else:
                    QMessageBox.information(self,"ERROR","failed to update data in work column!")
            elif select_column == 0 and select_row >0:
                Id = int(self.ui.table.item(select_row, 0).text())
                query = QSqlQuery()
                query.prepare("DELETE FROM test WHERE id = :id")
                query.bindValue(":id", Id)  
                if query.exec():
                    self.ui.box2.clear()
                    QMessageBox.information(self,"success","selected row delete from table successfully! ")
                    l_table()  
                else:
                    QMessageBox.information(self,"ERROR","row not delete!")
            elif select_column == 0 and select_row == 0:
                 query = QSqlQuery()
                 query.prepare("DROP TABLE IF EXISTS test")
                 query.exec() 
                 QMessageBox.information(self,"CLEAER","all table data are deleted successfully!")
                 query.exec("""
                    CREATE TABLE IF NOT EXISTS test(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time TEXT,
                    work TEXT
                    )""")
                 l_table()
#=====================================================
        def save():
                query = QSqlQuery()
                # SQL query to select all rows from the table
                query.prepare("SELECT * FROM test")
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
                    QMessageBox.information(self, "saved","data is successfully saved in output.csv file")
                else:
                  QMessageBox.information(self,"ERROR","unable to fetch table or recheck the table name")
#=====================================================
        # Populate the table on start
        l_table()
        # Connect buttons to functions
        self.ui.btn2.clicked.connect(insert)  
        self.ui.btn1.clicked.connect(update)  
        self.ui.btn3.clicked.connect(save)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = routin()
    window.show()
    sys.exit(app.exec())
