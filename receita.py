import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
                            QPushButton, QItemDelegate, QVBoxLayout, QCheckBox, QComboBox, QMainWindow,QGridLayout,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

class Janela(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.esquerda = 0
        self.topo = 0
        self.largura = 320
        self.altura = 505
        self.titulo = 'APP'
        
        QPushButton(self)

        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()




aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
