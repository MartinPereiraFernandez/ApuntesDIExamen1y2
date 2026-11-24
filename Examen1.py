import sys
from PyQt6.QtWidgets import *


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-11-2026 grupo A")

        rejilla = QGridLayout()

        self.configuracions = QComboBox()
        self.configuracions.addItems(["Configuración zoa 1", "Zoa 2", "Consola"])
        rejilla.addWidget(self.configuracions, 0, 0, 1, 3)

        self.textoZoa = QLabel("Zoa activada")
        rejilla.addWidget(self.textoZoa, 1, 0, 1, 1)
        self.checkZoa = QCheckBox()
        rejilla.addWidget(self.checkZoa, 1, 1, 1, 1)

        self.textoHora = QLabel("Hora de comezo de rego")
        rejilla.addWidget(self.textoHora, 2, 0, 1, 1)
        self.lineZoa = QLineEdit()
        rejilla.addWidget(self.lineZoa, 2, 1, 1, 1)

        layoutOpcions = QVBoxLayout()
        self.grupoOpcions = QGroupBox("Opcions")
        self.botonDiario = QRadioButton("Diario")
        layoutOpcions.addWidget(self.botonDiario)
        self.botonSemanal = QRadioButton("Semanal")
        layoutOpcions.addWidget(self.botonSemanal)
        self.checkAntixiada = QCheckBox("Antixiada")
        layoutOpcions.addWidget(self.checkAntixiada)
        self.checkChuvia = QCheckBox("Chuvia")
        layoutOpcions.addWidget(self.checkChuvia)
        self.grupoOpcions.setLayout(layoutOpcions)
        rejilla.addWidget(self.grupoOpcions, 1, 2, 3, 1)

        layoutDias = QHBoxLayout()
        self.grupoDias = QGroupBox("Dias")
        checkLunes = QCheckBox("Luns")
        layoutDias.addWidget(checkLunes)
        checkMartes = QCheckBox("Martes")
        layoutDias.addWidget(checkMartes)
        checkMiercoles = QCheckBox("Mercores")
        layoutDias.addWidget(checkMiercoles)
        checkJueves = QCheckBox("Xoves")
        layoutDias.addWidget(checkJueves)
        checkViernes = QCheckBox("Venres")
        layoutDias.addWidget(checkViernes)
        checkSabado = QCheckBox("Sabado")
        layoutDias.addWidget(checkSabado)
        checkDomingo = QCheckBox("Domingo")
        layoutDias.addWidget(checkDomingo)
        self.grupoDias.setLayout(layoutDias)
        rejilla.addWidget(self.grupoDias, 4, 0, 1, 3)

        self.textoDuracion = QLabel("Duración rego")
        rejilla.addWidget(self.textoDuracion, 3, 0, 1, 1)
        self.dial = QDial()
        rejilla.addWidget(self.dial, 3, 1, 1, 1)

        self.botonAceptar = QPushButton("Aceptar")
        rejilla.addWidget(self.botonAceptar, 5, 2, 1, 1)

        self.checkZoa.toggled.connect(self.alternarEstado)
        self.alternarEstado(False)

        centro = QWidget()
        centro.setLayout(rejilla)
        self.setCentralWidget(centro)

    def alternarEstado(self, activado: bool):
        self.textoHora.setEnabled(activado)
        self.lineZoa.setEnabled(activado)
        self.grupoOpcions.setEnabled(activado)
        self.grupoDias.setEnabled(activado)
        self.textoDuracion.setEnabled(activado)
        self.dial.setEnabled(activado)
        self.botonAceptar.setEnabled(activado)


app = QApplication(sys.argv)
ventana = FiestraPrincipal()
ventana.show()
app.exec()