# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):

        #Constructor de la clase Producto.

        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getter para id_producto
    @property
    def id_producto(self):
        return self._id_producto

    # Setter para id_producto
    @id_producto.setter
    def id_producto(self, value):
        self._id_producto = value

    # Getter para nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para nombre
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # Getter para cantidad
    @property
    def cantidad(self):
        return self._cantidad

    # Setter para cantidad
    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    # Getter para precio
    @property
    def precio(self):
        return self._precio

    # Setter para precio
    @precio.setter
    def precio(self, value):
        self._precio = value

    def __str__(self):

        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        #Constructor de la clase Inventario.
        self.productos = []  # Lista para almacenar los productos en el inventario

    def agregar_producto(self, producto):

        #Agrega un producto al inventario.

        if not any(p.id_producto == producto.id_producto for p in self.productos):
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado correctamente.")
        else:
            print(f"Error: El ID '{producto.id_producto}' ya existe. Por favor, use un ID único.")

    def id_unico(self, id_producto):
        #Verifica si un ID de producto es único en el inventario.

        return not any(p.id_producto == id_producto for p in self.productos)

    def eliminar_producto(self, id_producto):

        #Elimina un producto del inventario por ID.

        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            self.productos.remove(producto)
            print(f"Producto con ID '{id_producto}' eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):

        #Actualiza la cantidad o el precio de un producto existente.

        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto con ID '{id_producto}' actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):

        #Muestra todos los productos en el inventario.

        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

    def listar_ids(self):

        #Muestra todos los IDs disponibles en el inventario junto con los nombres.

        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("IDs disponibles:")
            for producto in self.productos:
                print(f"- {producto.id_producto}, {producto.nombre}")

    def buscar_producto(self, nombre):

        #Busca productos por nombre y los muestra.


        encontrado = False
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

# Función del menú principal
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto ID\n2. Eliminar Producto x ID\n3. Actualizar Producto x ID\n4. Buscar Producto x Nombre\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            # Verificar si el ID del producto ya existe; si es así, solicita uno nuevo
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
            # Eliminar un producto del inventario
            inventario.listar_ids()
            id_producto = input("Ingrese el ID del producto a eliminar (ej. EC-001): ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Actualizar la cantidad o el precio de un producto existente
            inventario.listar_ids()
            id_producto = input("Ingrese el ID del producto a actualizar (ej. EC-001): ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Buscar un producto por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()

if __name__ == "__main__":
    menu()
