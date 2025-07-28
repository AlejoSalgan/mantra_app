from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QCheckBox, QApplication, QLabel
)
from PyQt5.QtGui import QIcon, QPixmap

import sys
from logica_mantra_app import DB, Acciones

class TareasApp(QWidget):
    def __init__(self, acciones):
        super().__init__()
        self.acciones = acciones
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setWindowIcon(QIcon("logo_mantra.png"))

        logo = QLabel()
        logo.setObjectName("logo")
        self.layout.addWidget(logo)

        self.setWindowTitle("MANTRA")
        self.setGeometry(100, 100, 400, 400)


        self.input_tarea = QLineEdit()
        self.input_tarea.setObjectName("btnInput")
        self.input_tarea.setPlaceholderText("Escribí una nueva tarea")
        self.layout.addWidget(self.input_tarea)

        self.btn_agregar = QPushButton("Agregar Tarea")
        self.btn_agregar.setObjectName("btnAgregar")
        self.btn_agregar.clicked.connect(self.agregar_tarea)
        self.layout.addWidget(self.btn_agregar)

        self.tareas_layout = QVBoxLayout()
        self.tareas_layout.setContentsMargins(10, 10, 10, 10)
        self.tareas_layout.setSpacing(6)
        self.layout.addLayout(self.tareas_layout)

        self.setLayout(self.layout)
        self.mostrar_tareas()

    def agregar_tarea(self):
        nombre = self.input_tarea.text()
        if nombre:
            self.acciones.agregar_tarea(nombre)
            self.input_tarea.clear()
            self.mostrar_tareas()

    def mostrar_tareas(self):
        # Limpia el layout anterior
        while self.tareas_layout.count():
            item = self.tareas_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for id, nombre, hecha in self.acciones.listar_tareas():
            fila = QHBoxLayout()

            check = QCheckBox(nombre)
            check.setObjectName("tarea")
            check.setChecked(hecha == 1)
            check.setFixedHeight(40)  # Alto fijo para todos los checkboxes
            check.setMinimumWidth(250)  # Ancho mínimo para alinear
            check.stateChanged.connect(lambda estado, i=id: self.acciones.marcar_como_hecha(i) if estado else None)
            fila.addWidget(check)

            btn_eliminar = QPushButton("Eliminar")
            btn_eliminar.setObjectName('btnEliminar')
            btn_eliminar.clicked.connect(lambda _, i=id: self.eliminar_tarea(i))
            fila.addWidget(btn_eliminar)

            contenedor = QWidget()
            contenedor.setLayout(fila)
            self.tareas_layout.addWidget(contenedor)

    def eliminar_tarea(self, id_tarea):
        self.acciones.eliminar_tarea(id_tarea)
        self.mostrar_tareas()


if __name__ == "__main__":
    db = DB()
    acciones = Acciones(db)

    app = QApplication(sys.argv)
    
    with open('estilos.qss', 'r') as estilos:
        estilo = estilos.read()
        app.setStyleSheet(estilo)

    ventana = TareasApp(acciones)
    ventana.show()
    sys.exit(app.exec_())
