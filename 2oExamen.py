import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layoutPrincipal = QVBoxLayout()

        self.tabla = QTableWidget()
        self.crearTabla()
        self.cambiaCorXenero()
        self.cambiaCorFalecido()

        self.layoutPrincipal.addWidget(self.tabla)

        self.centro = QWidget()
        self.centro.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.centro)

    def crearTabla(self):
        self.tabla.setColumnCount(4)
        self.tabla.setRowCount(3)
        self.tabla.setHorizontalHeaderLabels(["Nome","DNI","Xenero","Falecimiento"])

        self.checkAna = QTableWidgetItem()
        self.checkAna.setFlags(Qt.ItemFlag.ItemIsUserCheckable|Qt.ItemFlag.ItemIsEnabled)
        self.checkAna.setCheckState(Qt.CheckState.Unchecked)
        self.tabla.setItem(0,0,QTableWidgetItem("Ana Perez"))
        self.tabla.setItem(0, 1, QTableWidgetItem("1111R"))
        self.tabla.setItem(0, 2, QTableWidgetItem("Muller"))
        self.tabla.setItem(0, 3, self.checkAna)

        self.checkPaco = QTableWidgetItem()
        self.checkPaco.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        self.checkPaco.setCheckState(Qt.CheckState.Checked)
        self.tabla.setItem(1, 0, QTableWidgetItem("Paco Porras"))
        self.tabla.setItem(1, 1, QTableWidgetItem("2222T"))
        self.tabla.setItem(1, 2, QTableWidgetItem("Home"))
        self.tabla.setItem(1, 3, self.checkPaco)

        self.checkRoque = QTableWidgetItem()
        self.checkRoque.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        self.checkRoque.setCheckState(Qt.CheckState.Unchecked)
        self.tabla.setItem(2, 0, QTableWidgetItem("Roque Villas"))
        self.tabla.setItem(2, 1, QTableWidgetItem("3333H"))
        self.tabla.setItem(2, 2, QTableWidgetItem("Home"))
        self.tabla.setItem(2, 3, self.checkRoque)

    def cambiaCorXenero(self):
        for fila in range(self.tabla.rowCount()):
            xenero = self.tabla.item(fila,2).text()
            if xenero =="Home":
                color = QColor("lightblue")
            else:
                color = QColor("pink")

            for columna in range(self.tabla.columnCount()):
                self.tabla.item(fila,2).setBackground(color)

    def cambiaCorFalecido(self):
        for fila in range(self.tabla.rowCount()):
            if self.tabla.item(fila,3).checkState() == Qt.CheckState.Checked:
                self.tabla.item(fila,3).setBackground(QColor("red"))






app = QApplication(sys.argv)
ventana = FiestraPrincipal()
ventana.show()
app.exec()

