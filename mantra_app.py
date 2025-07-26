import json

class Acciones:
    def __init__(self):
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open('tareas/tareas.json', 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []
        
    def guardar_tareas(self):
        with open('tareas/tareas.json', 'w') as archivo:
            json.dump(self.tareas, archivo, indent=4)

    def agregar_tarea(self, tarea):
        self.tareas.append({"nombre": tarea, "hecha": False})
        self.guardar_tareas()
        print(f"Tarea ' {tarea} ' agregada con éxito")        

acciones = Acciones()
tarea_nueva = (str(input('Ingresa la tarea que deseas realizar: ')))
acciones.agregar_tarea(tarea_nueva)