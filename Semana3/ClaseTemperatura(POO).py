class ClimaDiario:
    def __init__(self, dias):  # Constructor con parámetro de entrada dias
        self.dias = dias
        # Ingresar datos por consola y limitar a número de días
        self.__temperatura = [0 for i in range(dias)]
        self.__dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Defino método para el ingreso de datos
    def ingresarTemperatura(self):
        for i in range(self.dias):
            dia = self.__dias_semana[i]
            self.__temperatura[i] = float(input(f"Ingrese en °C la temperatura del {dia}: "))

    # Métodos getter para los atributos encapsulados
    def get_temperatura(self):
        return self.__temperatura

    def get_dias_semana(self):
        return self.__dias_semana


# Defino la clase ClimaTemperatura que hereda de ClimaDiario
class ClimaTemperatura(ClimaDiario):
    # Limitar el ingreso de valores a 7 días
    def __init__(self):
        super().__init__(7)  # Usando super() para llamar al constructor de la clase base

    # Método para calcular el promedio de temperaturas
    def calcularPromedio(self):
        # Calcular el promedio de las temperaturas
        temperatura = self.get_temperatura()
        promedio = sum(temperatura) / self.dias
        return promedio


# Instancio objeto
obj_promedio1 = ClimaTemperatura()
# Invoco ingreso de datos temperatura
obj_promedio1.ingresarTemperatura()
# Invoco para calcular el promedio
print(f"\nEl promedio semanal de las temperaturas es: {obj_promedio1.calcularPromedio():.2f}°C")