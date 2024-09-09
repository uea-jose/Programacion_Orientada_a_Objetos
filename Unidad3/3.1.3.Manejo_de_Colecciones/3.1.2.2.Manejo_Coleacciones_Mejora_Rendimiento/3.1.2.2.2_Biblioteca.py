#UINDAD 3
#Manipulación de archivos, manejo de excepciones y Manejo de Colecciones.
#Tema 3.2: Manejo de Colecciones
#Subtema 3.2.2: Utilización de colecciones para la mejora de rendimiento
#--------------------BILBIOTECA--------------

#Clase libro

class libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.informacion = (autor, titulo) # Tupla para autor+titulo no cambia

    #Metodo para retornar atribtudos
    def __str__(self):
        return (f"Titulo: {self.titulo}, Autor:{self.autor}, Categoria:{self.categoria},ISBN: {self.isbn}")

#Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.lista_usuarios = [] #defino lista para usarios

#CLase Biblioteca donde servirá paara la gestion de la librios/usarios/prestamos

class Biblioteca:
    def __init__(self):
        self.libros = {} #SE DEFINE DICCIONARO PARA LA GESTION DE LIBROS
        self.usuarios = {} #Defino diccionario para la gestión de usuarios
        self.ids_usuario = set() #Defino conjuntos para la gestion de id_user

    #metodo apara añadir libro
    def add_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libre {libro.titulo} ya existe")
        else:
            self.libros[libro.isbn] = libro
            self.ids_usuario.add(libro.isbn)
            print(f"Libro {libro.titulo} añadido correctamente")

    #metodo para quitar libro
    def del_libro(self, libro):
        if libro.isbn in self.libros:
            del self.libros[libro.isbn]
            print(f"El libro {libro.titulo} eliminado")
        else:
            print(f"El libro {libro.titulo} no existe")

    #Registro y eliminacion Usuarios
    #Agregar Usuario
    def add_usuario(self, usuario):
        if usuario.isbn in self.usuarios:
            print(f"El usuario {usuario.nombre} ya existe")
        else:
            self.usuarios[usuario.id_user] = usuario
            self.ids_usuario.add(usuario.id_user)
            print(f"El usuario: {usuario.nombre} creado")
    #Eliminar usuario
    def del_usuario(self, id_usuario):
        if id_usuario in self.ids_usuario:
            del self.usuarios[id_usuario]
            print(f"El usuario {id_usuario} eliminado")
        else:
            print(f"El usuario {id_usuario} no existe")

    #Prestar y devolver los libros



