from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 480)
        MainWindow.setStyleSheet("""
#MainWindow,#centralwidget{
background-color:#8ab6f9;
}
#frame1,#frame2,#frame3{
background-color:#8ab6f9;
}
#label1,#label2{
color:black;
}
#box1, #box2{
background-color:#cadcfc;
color:black;
font-size:15px;
border:1px solid black;
border-radius:15px;
padding:8px;
}
#btn1,#btn2,#btn3,#btn4,#btn5{
border:1px solid white;
background-color:#1d71ba;
color:white;
border-radius:10px;
font-weight:bold;
}
#table{
border-radius:15px;
background-color:#cadcfc;
font-size:18px;
font-weight:bold;
}
QHeaderView::section{
border:none;
color:white;
background-color:#00246b;
border-bottom: 3px solid #1d71ba;
text-align:left;
padding-left:5px;
}
#table::item{
border-bottom: 1px solid black;
padding-left:3px;
color:black;
}
""")

        # Create the main widget and set it as central widget
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.widget)

        # Create frame1 and set its parent to the main widget
        self.frame1 = QtWidgets.QFrame(parent=self.widget)
        self.frame1.setGeometry(QtCore.QRect(10, 10, 581, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.frame1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame1.setObjectName("frame1")

        # Create widget1 inside frame1 and set its parent as frame1
        self.widget1 = QtWidgets.QWidget(parent=self.frame1)
        self.widget1.setGeometry(QtCore.QRect(110, 10, 371, 89))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")

        # Create labels and text edits, set their parents correctly

        self.label2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label2)

        self.box2 = QtWidgets.QLineEdit(parent=self.widget1)
        self.box2.setMaximumSize(QtCore.QSize(250, 35))
        self.box2.setPlaceholderText("")
        self.box2.setObjectName("box2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.box2)

        # Create frame3 and set its parent to the main widget
        self.frame3 = QtWidgets.QFrame(parent=self.widget)
        self.frame3.setGeometry(QtCore.QRect(10, 170, 581, 301))
        self.frame3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame3.setObjectName("frame3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame3)
        self.gridLayout.setObjectName("gridLayout")

        # Create the table and set its parent to frame3
        self.table = QtWidgets.QTableWidget(parent=self.frame3)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        self.item = QtWidgets.QTableWidgetItem()
        self.item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.item.setFont(font)
        self.table.setHorizontalHeaderItem(0, self.item)
        self.item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, self.item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(50)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setMinimumSectionSize(30)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)

        # Create frame2 for buttons
        self.frame2 = QtWidgets.QFrame(parent=self.widget)
        self.frame2.setGeometry(QtCore.QRect(10, 110, 581, 61))
        self.frame2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame2.setObjectName("frame2")

        # Create buttons inside frame2
        self.btn1 = QtWidgets.QPushButton(parent=self.frame2)
        self.btn1.setGeometry(QtCore.QRect(60, 10, 91, 41))
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/project1icon/add-fill.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn1.setIcon(icon)
        self.btn1.setIconSize(QtCore.QSize(20, 20))
        self.btn1.setObjectName("btn1")

        self.btn2 = QtWidgets.QPushButton(parent=self.frame2)
        self.btn2.setGeometry(QtCore.QRect(160, 10, 91, 41))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/project1icon/upload-line.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn2.setIcon(icon1)
        self.btn2.setIconSize(QtCore.QSize(20, 20))
        self.btn2.setObjectName("btn2")

        self.btn3 = QtWidgets.QPushButton(parent=self.frame2)
        self.btn3.setGeometry(QtCore.QRect(260, 10, 81, 41))
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icons/project1icon/delete-back-2-line.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn3.setIcon(icon2)
        self.btn3.setIconSize(QtCore.QSize(20, 20))
        self.btn3.setObjectName("btn3")

        self.btn4 = QtWidgets.QPushButton(parent=self.frame2)
        self.btn4.setGeometry(QtCore.QRect(350, 10, 91, 41))
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\icons/project1icon/delete-bin-6-line.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn4.setIcon(icon3)
        self.btn4.setIconSize(QtCore.QSize(20, 20))
        self.btn4.setObjectName("btn4")

        self.btn5 = QtWidgets.QPushButton(parent=self.frame2)
        self.btn5.setGeometry(QtCore.QRect(450, 10, 81, 41))
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\icons/project1icon/save-3-line.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn5.setIcon(icon4)
        self.btn5.setIconSize(QtCore.QSize(20, 20))
        self.btn5.setObjectName("btn5")

        # Set the window title and labels after setup
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label2.setText(_translate("MainWindow", "ADD TASK  :"))
        self.item = self.table.horizontalHeaderItem(0)
        self.item.setText(_translate("MainWindow", "Sno"))
        self.item = self.table.horizontalHeaderItem(1)
        self.item.setText(_translate("MainWindow", "TASK"))
        self.btn1.setText(_translate("MainWindow", "ADD"))
        self.btn2.setText(_translate("MainWindow", "UPDATE"))
        self.btn3.setText(_translate("MainWindow", "CLEAR"))
        self.btn4.setText(_translate("MainWindow", "DELETE"))
        self.btn5.setText(_translate("MainWindow", "SAVE"))
