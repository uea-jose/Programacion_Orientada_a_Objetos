#Defino la clase Clima Diario
class ClimaDiario:
    def __init__(self,dias): #constructor con parametro de entra dias
        self.dias = dias
        #ingresar datos por consola y limitar a nimero dias
        self.temperatura =[0 for i in range(dias)]
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    #defino metodo para el ingreso de datos
    def ingresarTemperatura(self):
        for i in range(self.dias):
            dia = self.dias_semana[i]
            self.temperatura[i] = float(input(f"Ingrese en °C la temperatura del {dia}: "))


#defino clase calular temperatuira promedio
# Defino la clase ClimaTemperatura que hereda de ClimaDiario
class ClimaTemperatura(ClimaDiario):
    # Limitar el ingreso de valores a 7 días
    def __init__(self):
        ClimaDiario.__init__(self, 7)

    # Método para calcular el promedio de temperaturas
    def calcularPromedio(self):
        # Calcular el promedio de las temperaturas
        promedio = sum(self.temperatura) / self.dias
        return promedio

# Instancio objeto
obj_promedio1 = ClimaTemperatura()
# Invoco ingreso de datos temperatura
obj_promedio1.ingresarTemperatura()
# Invoco para calcular el promedio
print(f"\nEl promedio semanal de las temperaturas es: {obj_promedio1.calcularPromedio():.2f}:°C")









