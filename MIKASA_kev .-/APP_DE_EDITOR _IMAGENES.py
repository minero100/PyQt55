from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('El q lo lea es gay ')

main_win.show()


app = QApplication([])
main_win = QWidget()
main_win.resize(300, 200)
main_win.setWindowTitle('Creanlo o no ')
statement  = QLabel('!Los mamiferos con la tula mas grandes son los burros¡')
btn_yes = QPushButton('Si')
btn_no = QPushButton('No')

line1 = QHBoxLayout ()
line2 = QHBoxLayout ()
line1.addWidget(statement, alignment = Qt.AlignCenter)
line2.addWidget(btn_yes)
line2.addWidget(btn_no)
line3 = QVBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)
main_win.setLayout(line3)
main_win.show()
app.exec_()