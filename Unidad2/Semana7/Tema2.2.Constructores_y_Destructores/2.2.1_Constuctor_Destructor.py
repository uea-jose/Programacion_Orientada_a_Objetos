#UNIDAD 2 
#Tema 2.2.1 Contructor y Destructor
#(Semana 07) Tarea: Constructores y Destructores
# Clase Servidor que simula la conexión y desconexión de un servidor
class Servidor:
    # Constructor de la clase Servidor
    def __init__(self, direccion_ip): #crea instancia actual del objeo
        # Inicializa el atributo direccio_ip con el valor  argumento
        self.direccion_ip = direccion_ip
        # Imprime un mensaje indicando que el servidor está conectado
        print(f"Servidor: '{self.direccion_ip}'.. Conectanose")
    
    # Destructor de la clase Servidor
    def __del__(self):
        # Imprime un mensaje indicando que el servidor está desconectado
        print(f"Servidor en '{self.direccion_ip}' desconexión.")

# Clase Conexion que simula la apertura y cierre de una conexión de red
class Conexion:
    # Constructor de la clase Conexion
    def __init__(self, estado):
        # Inicializa el atributo 'estado' 
        self.estado = estado
        # Imprime un mensaje indicando que la conexión está establecida
        print(f"Conexión '{self.estado}' establecida.")
    
    # Destructor de la clase Conexion
    def __del__(self):
        # Imprime un mensaje indicando que la conexión está cerrada
        print(f"Conexión '{self.estado}' cerrada.")

# Creación de una instancia de la clase Servidor
mi_servidor = Servidor("200.223.111.124")
# Eliminación explícita de la instancia de la clase Servidor
del mi_servidor

# Creación de una instancia de la clase Conexion
mi_conexion = Conexion("Servicio")
# Eliminación explícita de la instancia de la clase Conexion
del mi_conexion
