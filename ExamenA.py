import sys

from PyQt6.QtWidgets import *


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-11-2026 grupo A")

        self.principal = QWidget()

        self.configuracion1 = QGridLayout()

        self.textoZoa = QLabel("Zoa activada")
        self.checkZoa = QCheckBox()

        self.configuracion1.addWidget(self.textoZoa,0,0)
        self.configuracion1.addWidget(self.checkZoa,0,1)

        self.textoHora = QLabel("Hora de comexo de rego")
        self.lineHora = QLineEdit()

        self.configuracion1.addWidget(self.textoZoa,1,0)
        self.configuracion1.addWidget(self.lineHora,1,1)

        self.textoDuracion = QLabel("Duración rego")
        self.rueda = QDial()

        self.configuracion1.addWidget(self.textoDuracion,2,0)
        self.configuracion1.addWidget(self.rueda,2,1)

        self.layoutDias = QHBoxLayout()
        self.luns = QCheckBox("Luns")
        self.martes = QCheckBox("Martes")
        self.mercores = QCheckBox("Mercores")
        self.xoves = QCheckBox("Xoves")
        self.venres = QCheckBox("Venres")
        self.sabado = QCheckBox("Sabado")
        self.domingo = QCheckBox("Domingo")
        self.layoutDias.addWidget(self.luns)
        self.layoutDias.addWidget(self.martes)
        self.layoutDias.addWidget(self.mercores)
        self.layoutDias.addWidget(self.xoves)
        self.layoutDias.addWidget(self.venres)
        self.layoutDias.addWidget(self.sabado)
        self.layoutDias.addWidget(self.domingo)

        self.grupoDias = QGroupBox("Dias")
        self.grupoDias.setLayout(self.layoutDias)
        self.configuracion1.addWidget(self.grupoDias,3,0,1,3)

        self.layoutOpcions = QVBoxLayout()
        self.diario = QRadioButton("Diario")
        self.semanal = QRadioButton("Semanal")
        self.antixiada = QCheckBox("Antixiada")
        self.chuvia = QCheckBox("Chuvia")
        self.layoutOpcions.addWidget(self.diario)
        self.layoutOpcions.addWidget(self.semanal)
        self.layoutOpcions.addWidget(self.antixiada)
        self.layoutOpcions.addWidget(self.chuvia)
        self.grupoOpcions = QGroupBox("Opcions")
        self.grupoOpcions.setLayout(self.layoutOpcions)
        self.configuracion1.addWidget(self.grupoOpcions,0,2,3,1)

        self.aceptar = QPushButton("Aceptar")
        self.configuracion1.addWidget(self.aceptar,5,2,1,1)

        self.centro1 = QWidget()
        self.centro1.setLayout(self.configuracion1)

        self.etiqueta = QLabel("Etiqueta")
        self.configuracion2 = QGridLayout()
        self.configuracion2.addWidget(self.etiqueta)
        self.centro2 = QWidget()
        self.centro2.setLayout(self.configuracion2)

        self.consola = QTextEdit()
        self.configuracion3 = QGridLayout()
        self.configuracion3.addWidget(self.consola)
        self.centro3 = QWidget()
        self.centro3.setLayout(self.configuracion3)

        self.stacked = QStackedLayout()
        self.elegir = QComboBox()
        self.elegir.addItems(["Configuración zoa 1","Configuración zoa 2","Consola"])
        self.stacked.addWidget(self.elegir)
        self.stacked.addWidget(self.centro1)
        self.stacked.addWidget(self.centro2)
        self.stacked.addWidget(self.centro3)

        self.stacked.setCurrentIndex(0)

        self.principal.setLayout(self.stacked)

        self.setCentralWidget(self.principal)

app = QApplication(sys.argv)
ventana = FiestraPrincipal()
ventana.show()
app.exec()