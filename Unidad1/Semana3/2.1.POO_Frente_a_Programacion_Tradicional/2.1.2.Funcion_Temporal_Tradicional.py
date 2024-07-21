#inicilizao variable dias
dias = 7

#funcion para ingreso de datos diarios de temp

def ingresar_temperatura(): # funcion qye me ingresa y devuele el arry temperatuar
    temperatura = [0] * dias
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    #defino array de temperaturas
    for i in range(dias):
        dia = dias_semana[i]
        temperatura[i] = float(input(f"Ingrese en °C la temperatura del {dia}: "))
    return temperatura

#funcion para calulo promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / dias
    return promedio

##llamo a la funcion ingresar tempetarura
temperaturas = ingresar_temperatura()
##llamo a la funcion promedio e imprimod
print(f"\nEl promedio semanal de las temperaturas es: {calcular_promedio(temperaturas):.2f}°C")