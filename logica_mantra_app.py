import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("tareas.db")
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                hecha INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

class Acciones:
    def __init__(self, db):
        self.conn = db.conn
        self.cursor = db.cursor

    def agregar_tarea(self, nombre):
        self.cursor.execute("INSERT INTO tareas (nombre) VALUES (?)", (nombre,))
        self.conn.commit()
        print(f"Tarea '{nombre}' agregada.")

    def listar_tareas(self):
        self.cursor.execute("SELECT id, nombre, hecha FROM tareas")
        return self.cursor.fetchall()


    def marcar_como_hecha(self, id_tarea):
        self.cursor.execute("UPDATE tareas SET hecha = 1 WHERE id = ?", (id_tarea,))
        self.conn.commit()
        print(f"Tarea {id_tarea} marcada como hecha.")

    def eliminar_tarea(self, id_tarea):
        self.cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
        self.conn.commit()
        print(f"Tarea {id_tarea} eliminada.")

if __name__ == "__main__":
    db = DB()
    acciones = Acciones(db)

    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar como hecha")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            acciones.listar_tareas()
        elif opcion == "2":
            nombre = input("Nueva tarea: ")
            acciones.agregar_tarea(nombre)
        elif opcion == "3":
            num = int(input("Número de tarea a marcar como hecha: "))
            acciones.marcar_como_hecha(num)
        elif opcion == "4":
            num = int(input("Número de tarea a eliminar: "))
            acciones.eliminar_tarea(num)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

