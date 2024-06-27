# Clase Persona (superclase)
class Persona:  # clase padre
    def _init_(self, id, nombre):
        self._id = id  # privado
        self.nombre = nombre

    # metodos para llamar y obtern encapsulado
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id


# Clase Usuario hereda de Persona
class Usuario(Persona):
    def _init_(self, id, nombre, contraseña):
        super()._init_(id, nombre)  # herencia de clase persona
        self._contraseña = contraseña
        self.tipo_transporte = None  # se defien por teclado

    def get_contraseña(self):
        return self._contraseña  # obtencion de encapsulado

    def set_contraseña(self, contraseña):
        self._contraseña = contraseña  # obtencion de encapsulado

    def set_tipo_transporte(self, tipo_transporte):
        self.tipo_transporte = tipo_transporte

    def get_tipo_transporte(self):
        return self.tipo_transporte


# degino calse padre posicion actual
class PosicionActual:
    def __init__(self):
        self.latitud = "00.22.33"
        self.longitud = "00.11.99"


class Destino(PosicionActual):
    def __init__(self):
        super().__init__()  # heredo de clase PosicionActual
        self.latitud = "11.20.03"
        self.longitud = "22.88.33"


class Usuario:
    def __init__(self, id_usuario, nombre, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contrasena = contrasena
        self.tipo_transporte = None

    def get_id(self):
        return self.id_usuario

    def get_tipo_transporte(self):
        return self.tipo_transporte


class Ruta:
    def __init__(self, posicion_actual, destino, usuario):
        self.posicion_actual = posicion_actual
        self.destino = destino
        self.usuario = usuario

    def calcular_ruta(self):
        lat_actual = self.posicion_actual.latitud
        lon_actual = self.posicion_actual.longitud
        lat_destino = self.destino.latitud
        lon_destino = self.destino.longitud

        print(f"Calculando la mejor ruta desde ({lat_actual}, {lon_actual}) hacia ({lat_destino}, {lon_destino}) "
              f"utilizando {self.usuario.get_tipo_transporte()}.")

    def mostrar_mensaje(self):
        print(f"El cliente {self.usuario.nombre}, de ID {self.usuario.get_id()}, "
              f"sale desde la posición actual hacia el destino en {self.usuario.get_tipo_transporte()} por ruta1.")


# Crear usuario
id_usuario = input("Ingrese el ID del usuario: ")
nombre_usuario = input("Ingrese el nombre del usuario: ")
contraseña_usuario = "password123"  # Contraseña establecida directamente

# Crear un objeto Usuario
usuario1 = Usuario(id_usuario, nombre_usuario, contraseña_usuario)

# Ingresar tipo de transporte para el usuario1
tipo_transporte = input("Ingrese el tipo de transporte: ")
usuario1.tipo_transporte = tipo_transporte  # Asignación del atributo tipo_transporte

# Crear objetos posición actual y destino
posicion_actual = PosicionActual()
destino = Destino()

# Crear objeto de la clase Ruta
ruta1 = Ruta(posicion_actual, destino, usuario1)

# Imprimir lo que definí en los métodos calcular_ruta y mostrar_mensaje
ruta1.calcular_ruta()
ruta1.mostrar_mensaje()