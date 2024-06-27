# Calcular el Area de un Rombo

# nomenclatura de la forma snake_case
# Area Rombo A= (1/2)(D X d)
# Diagonal_Ma =Diagonal Mayor

# Diagonal_Ma= Diagonasl Menor
def calcular_area_rombo(Diagonal_Mayor, diagonal_menor):
    area_rombo = (1 / 2) * Diagonal_Mayor * diagonal_menor
    return area_rombo


# Definir variables
# Solicitar las diagonales por teclado
while True:
    Diagonal_Mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
    # Verificar si diagonal_mayor es mayor que diagonal_menor
    if Diagonal_Mayor > diagonal_menor:
        break
    else:
        print("(D>d)La diagonal mayor debe ser mayor que la diagonal menor ingrese nuevamente.")

# Llamar al método calcular_area_rombo
area_del_rombo = calcular_area_rombo(Diagonal_Mayor, diagonal_menor)

# Mostrar en pantalla

if isinstance(Diagonal_Mayor, float) and isinstance(diagonal_menor, float):
    print(f"El área del rombo de {Diagonal_Mayor} x {diagonal_menor} e=: {area_del_rombo}")
else:
    print("Tipos ingrese enteros o decimales")