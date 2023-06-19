from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
QButtonGroup, QMessageBox
)

app = QApplication([])
window = QWidget()
button_group = QButtonGroup()
window.setWindowTitle('Симулятор подбрасывания монеты')
window.resize(400, 200)
window.move(800, 800)

title = QLabel('Подбросьте монетку')
btn = QPushButton('Подбросить')

layoutV = QVBoxLayout()
layoutH = QHBoxLayout()
layoutH1 = QHBoxLayout()

layoutH.addWidget(title, alignment = Qt.AlignCenter)
layoutH1.addWidget(btn, alignment = Qt.AlignCenter)

layoutV.addLayout(layoutH)
layoutV.addLayout(layoutH1)
window.setLayout(layoutV)


def rand_num():
    number = randint(1, 2)
    if number == 1:
        orel()    
    else:
        reshka()
def orel():
    victory_win = QMessageBox()
    victory_win.setText('Орёл')
    victory_win.exec()
    #title.setText('Орёл')
def reshka():
    victory_lose = QMessageBox()
    victory_lose.setText('Решка')
    victory_lose.exec()
    #title.setText('Решка')
btn.clicked.connect(rand_num)

window.show()
app.exec_()