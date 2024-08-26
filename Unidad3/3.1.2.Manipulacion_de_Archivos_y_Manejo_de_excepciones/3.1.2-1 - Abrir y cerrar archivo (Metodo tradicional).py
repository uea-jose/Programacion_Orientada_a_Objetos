import os

# Verifica si el archivo existe antes de intentar abrirlo en modo lectura.
if os.path.exists('ejemplo_lectura.txt'):
    # Abre el archivo en modo lectura y lo cierra después de imprimir su contenido.
    archivo = open('ejemplo_lectura.txt', 'r')
    print(archivo.read())  # Imprime el contenido del archivo
    archivo.close()  # Cierra el archivo
else:
    # Si el archivo no existe, informa al usuario.
    print("El archivo 'ejemplo_lectura.txt' no existe.")

# Abre el archivo en modo escritura (creándolo si no existe), escribe en él y luego lo cierra.
archivo = open('ejemplo_escritura.txt', 'w')
archivo.write('Este es un nuevo archivo.')  # Escribe en el archivo
archivo.close()  # Cierra el archivo

# Abre el archivo en modo añadir, añade una nueva línea y luego lo cierra.
archivo = open('ejemplo_escritura.txt', 'a')
archivo.write('\nAñadiendo una segunda línea.')  # Añade nueva línea de texto al archivo
archivo.close()  # Cierra el archivo

# Verifica si el archivo al que se desea leer existe antes de abrirlo.
if os.path.exists('ejemplo_escritura.txt'):
    # Abre el archivo en modo lectura y lo cierra después de imprimir su contenido.
    archivo = open('ejemplo_escritura.txt', 'r')
    print(archivo.read())  # Imprime el contenido del archivo
    archivo.close()  # Cierra el archivo
else:
    # Si el archivo no existe, informa al usuario.
    print("El archivo 'ejemplo_escritura.txt' no existe.")
