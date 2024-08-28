# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, value):
        self._id_producto = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        # Aquí usamos un diccionario para almacenar los productos usando ID como clave
        self.productos = {}
        # Aquí usamos un conjunto para almacenar nombres únicos de productos
        self.nombres_unicos = set()
        # Aquí usamos un conjunto para verificar IDs de productos duplicados
        self.ids_producto = set()
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open('Inventario.txt', 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    # Aquí utilizamos un diccionario para guardar los productos
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
                    # Aquí agregamos el nombre del producto al conjunto de nombres únicos
                    self.nombres_unicos.add(nombre)
                    # Aquí agregamos el ID del producto al conjunto de IDs
                    self.ids_producto.add(id_producto)
        except FileNotFoundError:
            print("Advertencia: No se encontró el archivo 'Inventario.txt'. Se creará un nuevo archivo.")

    def guardar_inventario(self):
        with open('Inventario.txt', 'w') as file:
            # Aquí recorremos los productos en el diccionario
            for producto in self.productos.values():
                file.write(str(producto) + '\n')

    def agregar_producto(self, producto):
        if producto.id_producto not in self.ids_producto:
            # Aquí usamos un diccionario para agregar un nuevo producto
            self.productos[producto.id_producto] = producto
            # Aquí agregamos el nombre del producto al conjunto de nombres únicos
            self.nombres_unicos.add(producto.nombre)
            # Aquí agregamos el ID del producto al conjunto de IDs
            self.ids_producto.add(producto.id_producto)
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' agregado correctamente.")
        else:
            print(f"Error: El ID '{producto.id_producto}' ya existe. Por favor, use un ID único.")

    def id_unico(self, id_producto):
        # Aquí verificamos si el ID ya existe en el conjunto
        return id_producto not in self.ids_producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            # Aquí eliminamos un producto del diccionario
            producto = self.productos.pop(id_producto)
            # Aquí eliminamos el nombre del producto del conjunto de nombres únicos
            self.nombres_unicos.discard(producto.nombre)
            # Aquí eliminamos el ID del producto del conjunto de IDs
            self.ids_producto.discard(id_producto)
            self.guardar_inventario()
            print(f"Producto con ID '{id_producto}' eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Aquí usamos .get para acceder a un producto en el diccionario
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto con ID '{id_producto}' actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            # Aquí mostramos todos los productos usando un diccionario
            for producto in self.productos.values():
                print(producto)

    def listar_ids(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("IDs disponibles:")
            # Aquí listamos los IDs de los productos usando un diccionario
            for id_producto, producto in self.productos.items():
                print(f"- {id_producto}, {producto.nombre}")

    def buscar_producto(self, nombre):
        encontrado = False
        # Aquí buscamos productos en el diccionario
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def resumen_inventario(self):
        # Aquí utilizamos una tupla para retornar un resumen del inventario
        total_productos = len(self.productos)
        total_nombres_unicos = len(self.nombres_unicos)
        return total_productos, total_nombres_unicos

# Función del menú principal
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto ID\n2. Eliminar Producto x ID\n3. Actualizar Producto x ID\n4. Buscar Producto x Nombre\n5. Mostrar Inventario\n6. Resumen del Inventario\n7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '7':
            break
        elif opcion == '1':
            while True:
                id_producto = input("Ingrese el ID del producto (ej. EC-001): ")
                if inventario.id_unico(id_producto):
                    break
                else:
                    print(f"Error: El ID '{id_producto}' ya existe. Por favor, use un ID único.")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: ").replace(',', '.'))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            inventario.listar_ids()
            id_producto = input("Ingrese el ID del producto a eliminar (ej. EC-001): ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            inventario.listar_ids()
            id_producto = input("Ingrese el ID del producto a actualizar (ej. EC-001): ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            # Aquí mostramos un resumen utilizando una tupla
            total_productos, total_nombres_unicos = inventario.resumen_inventario()
            print(f"Total de productos: {total_productos}")
            print(f"Total de nombres únicos: {total_nombres_unicos}")

if __name__ == "__main__":
    menu()
