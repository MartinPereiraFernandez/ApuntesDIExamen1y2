import sys

from PyQt6.QtWidgets import *


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-11-2026 grupo A")

        rejilla = QGridLayout()


        listaConfiguraciones = QComboBox()
        listaConfiguraciones.addItems(["Configuración zoa 1","Configuracion zoa 2","Configuracion zoa 3"])
        rejilla.addWidget(listaConfiguraciones,0,0,1,3)

        rejilla.addWidget(QLabel("Zoa activa"),1,0)
        rejilla.addWidget(QCheckBox(),1,1)

        grupoOpcions = QGroupBox("Opcións")
        filaOpcions = QVBoxLayout()
        filaOpcions.addWidget(QRadioButton("Diario"))
        filaOpcions.addWidget(QRadioButton("Semanal"))
        filaOpcions.addWidget(QCheckBox("Antixiada"))
        filaOpcions.addWidget(QCheckBox("Chuvia"))
        grupoOpcions.setLayout(filaOpcions)
        rejilla.addWidget(grupoOpcions,1,2,3,1)

        rejilla.addWidget(QLabel("Hora comenzo de rego"),2,0)
        rejilla.addWidget(QLineEdit(),2,1)


        rejilla.addWidget(QLabel("Duración rego"),3,0)
        rejilla.addWidget(QDial(),3,1)

        grupoDias = QGroupBox("Dias")
        filaDias = QHBoxLayout()
        filaDias.addWidget(QCheckBox("Luns"))
        filaDias.addWidget(QCheckBox("Martes"))
        filaDias.addWidget(QCheckBox("Mércores"))
        filaDias.addWidget(QCheckBox("Xoves"))
        filaDias.addWidget(QCheckBox("Venres"))
        filaDias.addWidget(QCheckBox("Sabado"))
        filaDias.addWidget(QCheckBox("Domingo"))
        grupoDias.setLayout(filaDias)
        rejilla.addWidget(grupoDias,4,0,1,3)

        rejilla.addWidget(QPushButton("Aceptar"),5,2)





        centro = QWidget()
        centro.setLayout(rejilla)
        self.setCentralWidget(centro)





app = QApplication(sys.argv)
ventana = FiestraPrincipal()
ventana.show()
app.exec()
