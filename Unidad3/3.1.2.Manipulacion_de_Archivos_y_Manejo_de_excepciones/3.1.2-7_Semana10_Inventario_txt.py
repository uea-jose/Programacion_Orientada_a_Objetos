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
        self.productos = []  # Lista para almacenar los productos en el inventario
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open('Inventario.txt', 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("Advertencia: No se encontró el archivo 'Inventario.txt'. Se creará un nuevo archivo.")

    def guardar_inventario(self):
        with open('Inventario.txt', 'w') as file:
            for producto in self.productos:
                file.write(str(producto) + '\n')

    def agregar_producto(self, producto):
        if not any(p.id_producto == producto.id_producto for p in self.productos):
            self.productos.append(producto)
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' agregado correctamente.")
        else:
            print(f"Error: El ID '{producto.id_producto}' ya existe. Por favor, use un ID único.")

    def id_unico(self, id_producto):
        return not any(p.id_producto == id_producto for p in self.productos)

    def eliminar_producto(self, id_producto):
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print(f"Producto con ID '{id_producto}' eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
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
            for producto in self.productos:
                print(producto)

    def listar_ids(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("IDs disponibles:")
            for producto in self.productos:
                print(f"- {producto.id_producto}, {producto.nombre}")

    def buscar_producto(self, nombre):
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

if __name__ == "__main__":
    menu()
