import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-11-2026 Grupo B")

        rejilla = QGridLayout()

        rejilla.addWidget(QLabel("Zoa activada"),0,0,1,1)
        rejilla.addWidget(QCheckBox(),0,1,1,1)

        layoutDias = QVBoxLayout()
        layoutDias.addWidget(QCheckBox("Luns"))
        layoutDias.addWidget(QCheckBox("Martes"))
        layoutDias.addWidget(QCheckBox("Miercoles"))
        layoutDias.addWidget(QCheckBox("Xoves"))
        layoutDias.addWidget(QCheckBox("Venres"))
        layoutDias.addWidget(QCheckBox("Sabado"))
        layoutDias.addWidget(QCheckBox("Domingo"))
        layoutDias.addWidget(QPushButton("Aceptar"))

        grupoDias = QGroupBox("Dias")
        grupoDias.setLayout(layoutDias)
        rejilla.addWidget(grupoDias,0,2,4,1)

        rejilla.addWidget(QLabel("Hora do comenzo de rego"),1,0,1,1)
        rejilla.addWidget(QLineEdit(),1,1,1,1)

        rejilla.addWidget(QLabel("Duración rego"),2,0,1,1)
        linea = QSlider(Qt.Orientation.Horizontal)
        rejilla.addWidget(linea,2,1,1,1)

        layoutOpcions = QHBoxLayout()
        semanalOAnual = QComboBox()
        semanalOAnual.addItems(["Semanal","Anual"])
        layoutOpcions.addWidget(semanalOAnual)
        layoutOpcions.addWidget(QCheckBox("Antixiada"))
        layoutOpcions.addWidget(QCheckBox("Chuvia"))
        grupoOpcions = QGroupBox("Opcions")
        grupoOpcions.setLayout(layoutOpcions)
        rejilla.addWidget(grupoOpcions,3,0,1,2)

        rejilla.addWidget(QPushButton("Configuracion zoa 1"),4,0,1,1)
        rejilla.addWidget(QPushButton("Configuracion zoa 2"), 4, 1, 1, 1)
        rejilla.addWidget(QPushButton("Consola"), 4, 2, 1, 1)


        centro = QWidget()
        centro.setLayout(rejilla)
        self.setCentralWidget(centro)

app = QApplication(sys.argv)
ventana = FiestraPrincipal()
ventana.show()
app.exec()