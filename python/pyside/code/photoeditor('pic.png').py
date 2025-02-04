#image editor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QPixmap
from PIL import Image,ImageEnhance,ImageFilter
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QGridLayout,QLineEdit,QListWidget,QComboBox

#app settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("app")
main_window.resize( 620,480)

#all objects/widget codes
path = 'pic.png'

btn_folder = QPushButton("load image")
file_list = QListWidget()

clrr = QPushButton("color")
cont = QPushButton("contras")
blur = QPushButton("blur")
mirror = QPushButton("mirror")
gray = QPushButton("gray")

#box
box = QComboBox()
box.addItem("original")
box.addItem("mirror")
box.addItem("blur")
box.addItem("gray")
box.addItem("left")
box.addItem("right")

pbox = QLabel("picture place")
    
#design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(box)
col1.addWidget(clrr)
col1.addWidget(cont)
col1.addWidget(mirror)
col1.addWidget(blur)
col1.addWidget(gray)

col2.addWidget(pbox)

master_layout.addLayout(col1,30)
master_layout.addLayout(col2,70)

main_window.setLayout(master_layout)

#add functionality
def load():
    pbox.hide()
    imag = QPixmap(path)
    w,h = pbox.width(),pbox.height()
    imag = imag.scaled(w,h, Qt.KeepAspectRatio)
    pbox.setPixmap(imag)
    pbox.show()

def bw():
   pbox.hide()
   with Image.open('pic.png') as pic:
     black_white = pic.convert("L")
     black_white.save("bw.png")
     path = 'bw.png'
     imag = QPixmap(path)
     w,h = pbox.width(),pbox.height()
     imag = imag.scaled(w,h, Qt.KeepAspectRatio)
     pbox.setPixmap(imag)
     pbox.show()

def blr():
   pbox.hide()
   with Image.open('pic.png') as pic:
     blur = pic.filter(ImageFilter.BLUR)
     blur.save("blur.png")
     path = 'blur.png'
     imag = QPixmap(path)
     w,h = pbox.width(),pbox.height()
     imag = imag.scaled(w,h, Qt.KeepAspectRatio)
     pbox.setPixmap(imag)
     pbox.show()

def contra():
   
   pbox.hide()
   with Image.open('pic.png') as pic:
     contras = ImageEnhance.Contrast(pic)
     contras = contras.enhance(2.4)
     contras.save('contra.png')
     path = 'contra.png'
     imag = QPixmap(path)
     w,h = pbox.width(),pbox.height()
     imag = imag.scaled(w,h, Qt.KeepAspectRatio)
     pbox.setPixmap(imag)
     pbox.show()

def mirr():
   pbox.hide()
   with Image.open('pic.png') as pic:
     mirror = pic.transpose(Image.FLIP_LEFT_RIGHT)
     mirror.save("mirror.png")
     path = 'mirror.png'
     imag = QPixmap(path)
     w,h = pbox.width(),pbox.height()
     imag = imag.scaled(w,h, Qt.KeepAspectRatio)
     pbox.setPixmap(imag)
     pbox.show()

def clr():
   pbox.hide()
   with Image.open('pic.png') as pic:
     color = ImageEnhance.Color(pic).enhance(2.5)
     color.save("color.png")
     path = 'color.png'
     imag = QPixmap(path)
     w,h = pbox.width(),pbox.height()
     imag = imag.scaled(w,h, Qt.KeepAspectRatio)
     pbox.setPixmap(imag)
     pbox.show()

btn_folder.clicked.connect(load)
gray.clicked.connect(bw)
mirror.clicked.connect(mirr)
cont.clicked.connect(contra)
blur.clicked.connect(blr)
clrr.clicked.connect(clr)

#loop for window
main_window.show()
app.exec_()
