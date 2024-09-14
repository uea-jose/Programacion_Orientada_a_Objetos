# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.informacion = (autor, titulo)  # Tupla para autor+titulo no cambia

    # Método para retornar atributos
    def __str__(self):
        return (f"Titulo: {self.titulo}, Autor: {self.autor}, Categoria: {self.categoria}, ISBN: {self.isbn}")

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar los libros prestados

    # Método para añadir un libro a la lista de libros prestados
    def prestar_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)
        else:
            print(f"El libro {libro.titulo} ya está prestado a {self.nombre}")

    # Método para devolver un libro
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} no está prestado a {self.nombre}")

    # Método para mostrar los libros prestados
    def mostrar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para la gestión de libros
        self.usuarios = {}  # Diccionario para la gestión de usuarios
        self.ids_usuario = set()  # Conjunto para la gestión de IDs de usuario

    # Método para añadir libro
    def add_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro {libro.titulo} ya existe")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo} añadido correctamente")

    # Método para quitar libro
    def del_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"El libro con ISBN {isbn} eliminado")
        else:
            print(f"El libro con ISBN {isbn} no existe")

    # Método para agregar usuario
    def add_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuario:
            print(f"El usuario {usuario.nombre} ya existe")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuario.add(usuario.id_usuario)
            print(f"El usuario {usuario.nombre} creado")

    # Método para eliminar usuario
    def del_usuario(self, id_usuario):
        if id_usuario in self.ids_usuario:
            del self.usuarios[id_usuario]
            self.ids_usuario.remove(id_usuario)
            print(f"El usuario {id_usuario} eliminado")
        else:
            print(f"El usuario {id_usuario} no existe")

    # Método para prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"El libro con ISBN {isbn} no está disponible")
            return

        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no existe")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        usuario.prestar_libro(libro)
        print(f"Libro {libro.titulo} prestado a {usuario.nombre}")

    # Método para devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"El libro con ISBN {isbn} no está en el catálogo")
            return

        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no existe")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        usuario.devolver_libro(libro)
        print(f"Libro {libro.titulo} devuelto por {usuario.nombre}")

    # Método para buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio, "").lower() == valor.lower():
                resultados.append(str(libro))
        return resultados

    # Método para listar libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no existe")
            return []
        usuario = self.usuarios[id_usuario]
        return usuario.mostrar_libros_prestados()

# Menú interactivo
def iniciar_menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Añadir usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.add_libro(libro)

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.del_libro(isbn)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.add_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("Ingrese el ID del usuario a eliminar: ")
            biblioteca.del_usuario(id_usuario)

        elif opcion == "5":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario que recibe el libro: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario que devuelve el libro: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            criterio = input("Ingrese el criterio de búsqueda (titulo, autor, categoria): ")
            valor = input("Ingrese el valor de búsqueda: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            if resultados:
                print("\nLibros encontrados:")
                for resultado in resultados:
                    print(resultado)
            else:
                print("No se encontraron libros con ese criterio")

        elif opcion == "8":
            id_usuario = input("Ingrese el ID del usuario para listar los libros prestados: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if libros_prestados:
                print("\nLibros prestados:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print("No hay libros prestados para este usuario o el usuario no existe")

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

# Llamar a la función para iniciar el menú
iniciar_menu()
