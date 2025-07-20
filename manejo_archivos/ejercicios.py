# Leer un archivo de manera básica 1

# archivo = open('archivo_prueba.txt', 'r')  # 'r' = leer
# contenido = archivo.read()
# archivo.close()
# print(contenido)



#----------------------------------------------------


# Leer un archivo usando with (READ) 2

# with open('archivo_prueba.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print(contenido)


#----------------------------------------------------


# Crea un archivo y si existe lo sobreescribe (WRITE) 3

# with open('archivo_python.txt', 'w') as archivo:
#     archivo.write('\nAguante Racing!')

#----------------------------------------------------


# Agrega contenido al archivo existente (APPEND) 4


# with open('archivo_python.txt', 'a') as archivo:
#     archivo.write('\nAguante Racing!')


#----------------------------------------------------

# Leer el archivo línea por línea

with open('archivo_prueba.txt') as archivo:
    for linea in archivo:
        print(linea.strip())