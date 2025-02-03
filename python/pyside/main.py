import sys
from PySide6.QtCore import Qt, QDateTime,QCoreApplication, QMetaObject, QRect,QSize, Qt
from PySide6.QtWidgets import (QApplication,QFormLayout,QLayout,QPlainTextEdit,QStackedWidget, QHBoxLayout, QTableWidgetItem, QMainWindow,QMessageBox,QAbstractItemView,QLineEdit,QFrame, QGridLayout, QLabel,QPushButton,QTableWidget, QWidget)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtGui import (QCursor,QIcon,QFont)
import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 510)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"#page{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4e73df, stop:1 #6f42c1);\n"
"}\n"
"#page1{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #4e73df, stop:1 #6f42c1);\n"
"}\n"
"#page2{\n"
"/*background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #3498db);*/\n"
"background-color:black;\n"
"}\n"
"\n"
"/*style for page(0)and page1 content */\n"
"\n"
"#loginbg_2,#loginbg{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y1:1, stop:0 #6f42c1, stop:1 #4e73df);\n"
"border:2px solid white;\n"
"border-radius:15px;\n"
"}\n"
"#input1,#input2,#input1_2,#input2_2,#input1_3,#input2_3{\n"
"background-color:transparent;\n"
"border:1px solid white;\n"
"border-radius:15px;\n"
"color:white;\n"
"font-size:14px;\n"
"padding-left:10px;\n"
"}\n"
"#regi_btn{\n"
"background-color:transparent;\n"
"color:blue;\n"
"border:None;\n"
"border-bottom:1px solid blue;\n"
"}\n"
"#btn1,#btn1_2{\n"
" background-color: white;\n"
"    color: blac"
                        "k;\n"
"   border-top: 1px solid red;\n"
"	border-left: 1px solid red;\n"
"	border-right: 2px solid black;\n"
"    border-bottom:2px solid black;\n"
"    border-radius: 20px;\n"
"    font-size: 14px;\n"
"font-weight:bold;\n"
"}\n"
"#btn1:hover{\n"
"   border-top: 2px solid black;\n"
"	border-left: 2px solid black;\n"
"	border-right:1px solid red;\n"
"    border-bottom:1px solid red;\n"
"}\n"
"#btn1_2:hover{\n"
"   border-top: 2px solid black;\n"
"	border-left: 2px solid black;\n"
"	border-right:1px solid red;\n"
"    border-bottom:1px solid red;\n"
"}\n"
"\n"
"#label_9{\n"
"color:white;\n"
"}\n"
"/*cssfor page2*/\n"
"\n"
"#frame2{\n"
"border-radius:20px;\n"
"}\n"
"#d1{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #2C3E50, stop: 1 #4CA1AF);\n"
"border-top:2px solid white;\n"
"border-bottom:2px solid white;\n"
"border-right:2px solid white;\n"
"border-bottom-right-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"\n"
"}\n"
"#lightoff,#lighton{\n"
"background-color:transparent;\n"
"border:"
                        "None;\n"
"}\n"
"#dashboard,#about,#logout{\n"
"text-align:left;\n"
"background-color:transparent;\n"
"border:None;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"color:white;\n"
"}\n"
"#dashboard:hover{\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"}\n"
"#about:hover{\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"}\n"
"#logout:hover{\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"}\n"
"#menu,#menuo,#user{\n"
"background-color:transparent;\n"
"border:None;\n"
"}\n"
"#dp2{\n"
"background-color:transparent;\n"
"}\n"
"#frame3{\n"
"background-color:transparent;\n"
"}\n"
"#dpage1{\n"
"border-radius:20px;\n"
"background-color:transparent;\n"
"}\n"
"#dpage1_1{\n"
"background-color:transparent;\n"
"}\n"
"#usernaam{\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"font-family:Poppins;\n"
"}\n"
"#d2{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #2C3E50, stop: 1 #4CA1AF);\n"
"border:1px solid white;\n"
"border-radius:20px;\n"
"}\n"
""
                        "#dd2_f2{\n"
"background-color: transparent;\n"
"border-radius:20px;\n"
"}\n"
"#dtop1,#dtop2,#dtop3{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #2C3E50, stop: 1 #4CA1AF);\n"
"border:1px solid white;\n"
"border-radius: 20px;\n"
"}\n"
"#dpage2{\n"
"background-color:transparent;\n"
"}\n"
"#dp2_f1{\n"
"background-color:white;\n"
"border:1px solid black;\n"
"border-radius:10px;\n"
"}\n"
"#dp2_l2,#dp2_l1{\n"
"color:black;\n"
"background-color:white;\n"
"border:1px solid black;\n"
"font-weight:bold;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.frame1 = QStackedWidget(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setEnabled(True)
        self.frame1.setStyleSheet(u"")
        self.frame1.setFrameShadow(QFrame.Shadow.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_7 = QGridLayout(self.page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.loginbg_2 = QFrame(self.page)
        self.loginbg_2.setObjectName(u"loginbg_2")
        self.loginbg_2.setMinimumSize(QSize(400, 400))
        self.loginbg_2.setMaximumSize(QSize(400, 400))
        self.loginbg_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginbg_2.setFrameShadow(QFrame.Shadow.Raised)
        self.btn1_2 = QPushButton(self.loginbg_2)
        self.btn1_2.setObjectName(u"btn1_2")
        self.btn1_2.setGeometry(QRect(80, 310, 251, 41))
        self.btn1_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input1_2 = QLineEdit(self.loginbg_2)
        self.input1_2.setObjectName(u"input1_2")
        self.input1_2.setGeometry(QRect(100, 90, 251, 31))
        self.input1_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.input1_2.setClearButtonEnabled(False)
        self.input2_2 = QLineEdit(self.loginbg_2)
        self.input2_2.setObjectName(u"input2_2")
        self.input2_2.setGeometry(QRect(100, 190, 251, 31))
        self.label_2 = QLabel(self.loginbg_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 30, 171, 31))
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input2_3 = QLineEdit(self.loginbg_2)
        self.input2_3.setObjectName(u"input2_3")
        self.input2_3.setGeometry(QRect(100, 240, 251, 31))
        self.input1_3 = QLineEdit(self.loginbg_2)
        self.input1_3.setObjectName(u"input1_3")
        self.input1_3.setGeometry(QRect(100, 140, 251, 31))
        self.input1_3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.input1_3.setClearButtonEnabled(False)
        self.label_5 = QLabel(self.loginbg_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 90, 49, 31))
        self.label_6 = QLabel(self.loginbg_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 140, 49, 31))
        self.label_7 = QLabel(self.loginbg_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 190, 61, 31))
        self.label_8 = QLabel(self.loginbg_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 230, 61, 51))
        self.label_8.setWordWrap(True)

        self.gridLayout_7.addWidget(self.loginbg_2, 0, 0, 1, 1)

        self.frame1.addWidget(self.page)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.loginbg = QFrame(self.page1)
        self.loginbg.setObjectName(u"loginbg")
        self.loginbg.setMinimumSize(QSize(400, 400))
        self.loginbg.setMaximumSize(QSize(400, 400))
        self.loginbg.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginbg.setFrameShadow(QFrame.Shadow.Raised)
        self.btn1 = QPushButton(self.loginbg)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(80, 290, 251, 41))
        self.btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.input1 = QLineEdit(self.loginbg)
        self.input1.setObjectName(u"input1")
        self.input1.setGeometry(QRect(90, 140, 251, 31))
        self.input1.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.input1.setClearButtonEnabled(False)
        self.input2 = QLineEdit(self.loginbg)
        self.input2.setObjectName(u"input2")
        self.input2.setGeometry(QRect(90, 200, 251, 31))
        self.label = QLabel(self.loginbg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 40, 81, 31))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.regi_btn = QPushButton(self.loginbg)
        self.regi_btn.setObjectName(u"regi_btn")
        self.regi_btn.setGeometry(QRect(230, 250, 91, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.regi_btn.setFont(font1)
        self.regi_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_9 = QLabel(self.loginbg)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 240, 111, 16))
        self.label_10 = QLabel(self.loginbg)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 140, 71, 31))
        self.label_11 = QLabel(self.loginbg)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 200, 61, 31))

        self.gridLayout.addWidget(self.loginbg, 0, 0, 1, 1)

        self.frame1.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.gridLayout_3 = QGridLayout(self.page2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame2 = QFrame(self.page2)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"")
        self.frame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.d1 = QFrame(self.frame2)
        self.d1.setObjectName(u"d1")
        self.d1.setMinimumSize(QSize(40, 70))
        self.d1.setMaximumSize(QSize(40, 1500))
        self.d1.setFrameShape(QFrame.Shape.StyledPanel)
        self.d1.setFrameShadow(QFrame.Shadow.Raised)
        self.menuo = QPushButton(self.d1)
        self.menuo.setObjectName(u"menuo")
        self.menuo.setGeometry(QRect(0, 20, 40, 40))
        self.menuo.setMinimumSize(QSize(40, 40))
        self.menuo.setMaximumSize(QSize(40, 40))
        self.menuo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"projecticons/manuopen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuo.setIcon(icon)
        self.menuo.setIconSize(QSize(22, 22))
        self.about = QPushButton(self.d1)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(10, 230, 130, 35))
        self.about.setMinimumSize(QSize(130, 35))
        self.about.setMaximumSize(QSize(130, 35))
        self.about.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"projecticons/about.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.about.setIcon(icon1)
        self.about.setIconSize(QSize(22, 22))
        self.logout = QPushButton(self.d1)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(10, 390, 130, 35))
        self.logout.setMinimumSize(QSize(130, 35))
        self.logout.setMaximumSize(QSize(130, 35))
        self.logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"projecticons/logout.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout.setIcon(icon2)
        self.logout.setIconSize(QSize(22, 22))
        self.dashboard = QPushButton(self.d1)
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setGeometry(QRect(10, 130, 130, 35))
        self.dashboard.setMinimumSize(QSize(130, 35))
        self.dashboard.setMaximumSize(QSize(130, 35))
        self.dashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"projecticons/dashboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard.setIcon(icon3)
        self.dashboard.setIconSize(QSize(20, 20))
        self.dashboard.setAutoRepeatInterval(0)
        self.menu = QPushButton(self.d1)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 20, 40, 40))
        self.menu.setMinimumSize(QSize(40, 40))
        self.menu.setMaximumSize(QSize(40, 40))
        self.menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"projecticons/manu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon4)
        self.menu.setIconSize(QSize(22, 22))
        self.lightoff = QPushButton(self.d1)
        self.lightoff.setObjectName(u"lightoff")
        self.lightoff.setGeometry(QRect(0, 70, 40, 30))
        self.lightoff.setMinimumSize(QSize(40, 30))
        self.lightoff.setMaximumSize(QSize(40, 30))
        self.lightoff.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"projecticons/darkoff.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lightoff.setIcon(icon5)
        self.lightoff.setIconSize(QSize(35, 35))
        self.lighton = QPushButton(self.d1)
        self.lighton.setObjectName(u"lighton")
        self.lighton.setGeometry(QRect(0, 70, 40, 30))
        self.lighton.setMinimumSize(QSize(40, 30))
        self.lighton.setMaximumSize(QSize(40, 30))
        self.lighton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"projecticons/darkon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lighton.setIcon(icon6)
        self.lighton.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.d1)

        self.dp2 = QFrame(self.frame2)
        self.dp2.setObjectName(u"dp2")
        self.dp2.setFrameShape(QFrame.Shape.StyledPanel)
        self.dp2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.dp2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 0, 5, 0)
        self.frame3 = QStackedWidget(self.dp2)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setEnabled(True)
        self.frame3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame3.setLineWidth(1)
        self.dpage1 = QWidget()
        self.dpage1.setObjectName(u"dpage1")
        self.gridLayout_6 = QGridLayout(self.dpage1)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.dpage1_1 = QFrame(self.dpage1)
        self.dpage1_1.setObjectName(u"dpage1_1")
        self.dpage1_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.dpage1_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.dpage1_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.d2 = QFrame(self.dpage1_1)
        self.d2.setObjectName(u"d2")
        self.d2.setMinimumSize(QSize(460, 50))
        self.d2.setMaximumSize(QSize(16777215, 50))
        self.d2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.d2.setFrameShape(QFrame.Shape.StyledPanel)
        self.d2.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.d2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_4.setFormAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(0)
        self.formLayout_4.setContentsMargins(0, 0, 20, 0)
        self.usernaam = QLabel(self.d2)
        self.usernaam.setObjectName(u"usernaam")
        self.usernaam.setMaximumSize(QSize(160, 50))
        self.usernaam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.usernaam)

        self.user = QPushButton(self.d2)
        self.user.setObjectName(u"user")
        self.user.setMaximumSize(QSize(50, 50))
        icon7 = QIcon()
        icon7.addFile(u"projecticons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user.setIcon(icon7)
        self.user.setIconSize(QSize(30, 30))

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.user)


        self.gridLayout_5.addWidget(self.d2, 0, 0, 1, 1)

        self.dd2_f2 = QFrame(self.dpage1_1)
        self.dd2_f2.setObjectName(u"dd2_f2")
        self.dd2_f2.setFrameShape(QFrame.Shape.StyledPanel)
        self.dd2_f2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.dd2_f2)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 5)
        self.dtop1 = QFrame(self.dd2_f2)
        self.dtop1.setObjectName(u"dtop1")
        self.dtop1.setMinimumSize(QSize(460, 50))
        self.dtop1.setMaximumSize(QSize(16777215, 100))
        self.dtop1.setFrameShape(QFrame.Shape.StyledPanel)
        self.dtop1.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.dtop1, 0, 0, 1, 2)

        self.dtop3 = QFrame(self.dd2_f2)
        self.dtop3.setObjectName(u"dtop3")
        self.dtop3.setFrameShape(QFrame.Shape.StyledPanel)
        self.dtop3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.dtop3, 1, 1, 1, 1)

        self.dtop2 = QFrame(self.dd2_f2)
        self.dtop2.setObjectName(u"dtop2")
        self.dtop2.setFrameShape(QFrame.Shape.StyledPanel)
        self.dtop2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.dtop2, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.dd2_f2, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.dpage1_1, 0, 0, 1, 1)

        self.frame3.addWidget(self.dpage1)
        self.dpage2 = QWidget()
        self.dpage2.setObjectName(u"dpage2")
        self.gridLayout_8 = QGridLayout(self.dpage2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dp2_f1 = QFrame(self.dpage2)
        self.dp2_f1.setObjectName(u"dp2_f1")
        self.dp2_f1.setFrameShape(QFrame.Shape.StyledPanel)
        self.dp2_f1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.dp2_f1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.dp2_l1 = QLabel(self.dp2_f1)
        self.dp2_l1.setObjectName(u"dp2_l1")
        self.dp2_l1.setMinimumSize(QSize(0, 50))
        self.dp2_l1.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Modern No. 20"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.dp2_l1.setFont(font2)
        self.dp2_l1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.dp2_l1, 0, 0, 1, 1)

        self.dp2_l2 = QPlainTextEdit(self.dp2_f1)
        self.dp2_l2.setObjectName(u"dp2_l2")

        self.gridLayout_9.addWidget(self.dp2_l2, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.dp2_f1, 0, 0, 1, 1)

        self.frame3.addWidget(self.dpage2)

        self.gridLayout_4.addWidget(self.frame3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.dp2)


        self.gridLayout_3.addWidget(self.frame2, 0, 1, 1, 1)

        self.frame1.addWidget(self.page2)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.frame1)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.formLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.frame1.setCurrentIndex(2)
        self.frame3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn1_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.input1_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Name Here", None))
        self.input2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Password", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"REGISTRATION", None))
        self.input2_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Re-Enter Password", None))
        self.input1_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your course ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Course :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" confirm password ", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.input1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.input2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.regi_btn.setText(QCoreApplication.translate("MainWindow", u"Register Here", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Create New Account", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Username :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.menuo.setText("")
        self.about.setText(QCoreApplication.translate("MainWindow", u"  about", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"  logout", None))
        self.dashboard.setText(QCoreApplication.translate("MainWindow", u"  dashboard", None))
        self.menu.setText("")
        self.lightoff.setText("")
        self.lighton.setText("")
        self.usernaam.setText(QCoreApplication.translate("MainWindow", u"deepak singh thakur", None))
        self.user.setText("")
        self.dp2_l1.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.dp2_l2.setPlainText(QCoreApplication.translate("MainWindow", u"Welcome to [Your Company/Project Name]!\n"
"\n"
"At [Your Company Name], we are passionate about delivering exceptional solutions to our clients and users. Our mission is to [describe your main mission, purpose, or value proposition], and we strive to make a meaningful impact in everything we do.\n"
"\n"
"Who We Are\n"
"\n"
"Founded in [Year], we started as a small team with a big vision. Our team is made up of [brief description of your team or expertise], each bringing unique skills and experiences to help bring our mission to life. From [specific expertise or services], we\u2019ve worked tirelessly to ensure our [product/service/solution] is innovative, reliable, and tailored to the needs of our customers.\n"
"\n"
"What We Do\n"
"\n"
"We offer [briefly describe the products/services your company offers]. Whether you're looking for [feature 1], [feature 2], or [feature 3], we've got you covered! We are dedicated to providing solutions that are [adjective like \"cutting-edge,\" \"user-friendly,\" or \"high-qu"
                        "ality\"] and always have our users' best interests in mind.", None))
    # retranslateUi

class routin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #================================================================================
    # database connection

    #================================================================================


    #================================================================================
    #preloader
        self.ui.menuo.setVisible(False)
        self.ui.lighton.setVisible(False)

        self.ui.input2.setEchoMode(QLineEdit.Password)
        self.ui.input2_2.setEchoMode(QLineEdit.Password)
        self.ui.input2_3.setEchoMode(QLineEdit.Password)


    #================================================================================

    #================================================================================
    #events
        self.ui.btn1_2.clicked.connect(lambda:self.ui.frame1.setCurrentWidget(self.ui.page1))
        self.ui.btn1_2.clicked.connect(self.check1)
        self.ui.btn1_2.clicked.connect(self.clear)

        self.ui.regi_btn.clicked.connect(lambda:self.ui.frame1.setCurrentWidget(self.ui.page))

        self.ui.btn1.clicked.connect(lambda:self.ui.frame1.setCurrentWidget(self.ui.page2))
        self.ui.btn1.clicked.connect(self.check2)
        self.ui.btn1.clicked.connect(self.clear)

        self.ui.menu.clicked.connect(self.mnu)
        self.ui.menuo.clicked.connect(self.mnuo)

        self.ui.lightoff.clicked.connect(self.light)
        self.ui.lighton.clicked.connect(self.lighton)

        self.ui.dashboard.clicked.connect(lambda:self.ui.frame3.setCurrentWidget(self.ui.dpage1))

        self.ui.about.clicked.connect(lambda:self.ui.frame3.setCurrentWidget(self.ui.dpage2))

        self.ui.logout.clicked.connect(lambda:self.ui.frame1.setCurrentWidget(self.ui.page1))
    #================================================================================

    #================================================================================
    #functions

    def check1(self):
            if not self.ui.input2_3.text():
             self.ui.regi_btn.clicked.connect(lambda:self.ui.frame1.setCurrentWidget(self.ui.page))
            else:     
                name = self.ui.input1_2.text()
                print("name: ",name)
                course = self.ui.input1_3.text()
                print("course ",course)
                password = self.ui.input2_2.text()
                print("password:",password)
                cp = self.ui.input2_3.text()
                print("confirm ",cp)

    def check2(self):
            username = self.ui.input1.text()
            print(username)
            pas = self.ui.input2.text()
            print(pas)

    def clear(self):
        self.ui.input1_3.clear()
        self.ui.input1_2.clear()
        self.ui.input2_2.clear()
        self.ui.input2_3.clear()
        self.ui.input2.clear()
        self.ui.input1.clear()

    def mnu(self):
        self.ui.menu.setVisible(False)
        self.ui.menuo.setVisible(True)
        self.ui.d1.setMinimumSize(QSize(150, 70))
        self.ui.d1.setMaximumSize(QSize(40, 1500))
  
    
    def mnuo(self):
        self.ui.menuo.setVisible(False)
        self.ui.menu.setVisible(True)
        self.ui.d1.setMinimumSize(QSize(40, 70))

    #light and lighton function need more work    

    def light(self):
        self.ui.lighton.setVisible(True)
       # self.ui.dd2_f2.setStyleSheet("background-color:black;")
       # self.ui.dp2_f1.setStyleSheet("background-color:black;")
        self.ui.dp2_l2.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #000000, stop: 1 #434343);color:white;border:1px solid white;font-weight:bold;")
        self.ui.dp2_l1.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #000000, stop: 1 #434343);color:white;border:1px solid white;font-weight:bold;")
        das_item = "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #000000, stop: 1 #434343);"
        self.ui.d1.setStyleSheet(das_item)
        self.ui.d2.setStyleSheet(das_item)
        self.ui.dtop1.setStyleSheet(das_item)
        self.ui.dtop2.setStyleSheet(das_item)
        self.ui.dtop3.setStyleSheet(das_item)
        self.ui.about.setStyleSheet("background-color:transparent;")
        self.ui.dashboard.setStyleSheet("background-color:transparent;")
        self.ui.lightoff.setStyleSheet("background-color:transparent;")
        self.ui.lighton.setStyleSheet("background-color:transparent;")
        self.ui.menu.setStyleSheet("background-color:transparent;")
        self.ui.menuo.setStyleSheet("background-color:transparent;")
        self.ui.logout.setStyleSheet("background-color:transparent;")
        self.ui.user.setStyleSheet("background-color:transparent;")
        self.ui.usernaam.setStyleSheet("background-color:transparent;")

    def lighton(self):
        self.ui.lighton.setVisible(False)
        self.ui.lightoff.setVisible(True)
        das_item = "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #2C3E50, stop: 1 #4CA1AF);"
        self.ui.d2.setStyleSheet(das_item)
        self.ui.d1.setStyleSheet(das_item)
        self.ui.dtop1.setStyleSheet(das_item)
        self.ui.dtop2.setStyleSheet(das_item)
        self.ui.dtop3.setStyleSheet(das_item)
       # self.ui.dd2_f2.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #000428, stop: 1 #004e92);")
        #self.ui.dp2_f1.setStyleSheet("background-color:white;")
        self.ui.dp2_l2.setStyleSheet("background-color:white;color:black;border:1px solid black;font-weight:bold;")
        self.ui.dp2_l1.setStyleSheet("background-color:white;color:black;border:1px solid black;font-weight:bold;")
    #================================================================================
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = routin()
    window.show()
    sys.exit(app.exec())
