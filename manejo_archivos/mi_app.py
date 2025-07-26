""" 
importo pyqt y los modulos necesarios de pyqt5

    QApplication   ->   aplicacion general
    QWidget        ->   ventana basica
    QLabel         ->   texto en pantalla 
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


""" inicio la aplicacion """
app = QApplication(sys.argv)

"""  creo la ventana principal """
ventana = QWidget()
ventana.setWindowTitle("HOLAA")
ventana.setGeometry(100, 100, 400, 200)

"""  creo una etiqueta de texto """
etiqueta = QLabel("asdasd", ventana)
etiqueta.move(50, 80)

""" muestro la ventana """
ventana.show()
sys.exit(app.exec_())
