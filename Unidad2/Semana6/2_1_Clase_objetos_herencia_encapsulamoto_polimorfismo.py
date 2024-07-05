# Definicion de Clase Padre
class Operador_Command_Center:
    def __init__(self, nombre, ultimatix):
        # Definir atributos de la clase Padre
        self.nombre = nombre
        self.ultimatix = ultimatix

    # Método para mostrar información básica
    def mostrar_informacion_basica(self):
        print("-------INFORMACION TRABAJADOR-------")
        print(f"Nombre: {self.nombre}")
        print(f"Ultimatix: {self.ultimatix}")

# Clases Heredadas
# Defino una clase Operador Tipo Monitoreo
class Operador_Monitoreo(Operador_Command_Center):
    def __init__(self, nombre, ultimatix, rol):
        super().__init__(nombre, ultimatix)  # Llamo al constructor de la clase padre Operador_Command_Center
        self.rol = rol  # Atributo propio de la clase Operador_Monitoreo

    # Método para mostrar información detallada
    def mostrar_informacion_detallada(self):
        super().mostrar_informacion_basica()  # Llamo al método heredado de la clase padre
        print(f"Rol: {self.rol}")

# Defino una clase Operador Tipo Respaldo
class Operador_Respaldo(Operador_Command_Center):
    def __init__(self, nombre, ultimatix, rol):
        super().__init__(nombre, ultimatix)  # Llamo al constructor de la clase padre Operador_Command_Center
        self.rol = rol  # Atributo propio de la clase Operador_Respaldo

    # Método para mostrar información detallada
    def mostrar_informacion_detallada(self): #polimorfismo
        super().mostrar_informacion_basica()  # Llamo al método heredado de la clase padre
        print(f"Rol: {self.rol}")

# Defino una clase Operador Tipo Batch
class Operador_Batch(Operador_Command_Center):
    def __init__(self, nombre, ultimatix, rol):
        super().__init__(nombre, ultimatix)  # Llamo al constructor de la clase padre Operador_Command_Center
        self.rol = rol  # Atributo propio de la clase Operador_Batch

    # Método para mostrar información detallada
    def mostrar_informacion_detallada(self): #polimorfismo
        super().mostrar_informacion_basica()  # Llamo al método heredado de la clase padre
        print(f"Rol: {self.rol}")
# Defino una Clase Actividad para calcular el sueldo

class Actividad:
    def __init__(self, rol, sueldo=0):
        self.rol = rol
        self.__sueldo = sueldo  # Atributo privado

    def Rol_Monitoreo(self):
        nombre_rol = self.Rol_Monitoreo.__name__
        print(f"---------------ROL: {nombre_rol}--------------")
        print("Actividades: Monitoreo y Comunicacion de Alertas")
    def Rol_Respaldos(self):
        nombre_rol = self.Rol_Monitoreo.__name__
        print(f"---------------ROL: {nombre_rol}--------------")
        print("Actividades: Restauracion y Respaldos")  
    def Rol_Batch(self):
        nombre_rol = self.Rol_Monitoreo.__name__
        print(f"---------------ROL: {nombre_rol}--------------")
        print("Actividades: Ejecucion y Monitore del Cajas Controladoras")    
    def sueldo_segun_actividad(self): #poimorfimso con carga
        if self.rol == "Monitoreo":
            self.__sueldo = 775 #encapsulamiento
            self.Rol_Monitoreo()
            print(f"Sueldo = {self.__sueldo}")
        elif self.rol == "Respaldo":
            self.Rol_Respaldos()
            self.__sueldo = 995 #encapsulamiento
            print(f"Sueldo = {self.__sueldo}")
        elif self.rol == "Batch":
            self.Rol_Batch()
            self.__sueldo = 1220  #encapsulamiento
            print(f"Sueldo = {self.__sueldo}")
        else:
            self.__sueldo = 465  # Sueldo base
        return self.__sueldo





# Ejemplo de uso

# Ejemplo de uso
# Crear objeto ejemplo de la clase Monitoreo
operador_monitoreo = Operador_Monitoreo("Juan", "831726", "Monitoreo")
operador_monitoreo.mostrar_informacion_detallada()

# Ejemplo de uso
# Crear objeto ejemplo de la clase Respaldo
operador_respaldo = Operador_Respaldo("Yorvi", "731524", "Respaldos")
operador_respaldo.mostrar_informacion_detallada()

# Ejemplo de uso
# Crear objeto ejemplo de la clase Batch
operador_respaldo = Operador_Respaldo("Carol", "100229", "Batch")
operador_respaldo.mostrar_informacion_detallada()

print("===========ACTIVIDADES Y SUELDOS============")
# Ejemplo de uso obejtos para la actividad Monitoreo
actividad_monitoreo = Actividad("Monitoreo")
actividad_monitoreo.sueldo_segun_actividad()

# Ejemplo de uso obejtos para la actividad Respaldo
actividad_respaldo = Actividad("Respaldo")
actividad_respaldo.sueldo_segun_actividad()

# Ejemplo de uso obejtos para la actividad Respaldo
actividad_batch = Actividad("Batch")
actividad_batch.sueldo_segun_actividad()