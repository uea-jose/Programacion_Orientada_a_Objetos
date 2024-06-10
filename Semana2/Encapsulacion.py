#2. ENCAPSULAMIENTO
class Saldo:
    def __init__(self):
        self._Saldo__valor = 1256 #encapuslo el valor 120
        self.__valor = 120 #encapuslo el valor 120
        self.__limite =5000 #encapuslo el valor maximo de retiro
    #metodo get para traer el metodo para la variable encapusalda

    def get_cuenta(self):  #solo un metodo encapsulado que improme mensaje
        print("El valor de cuenta es:")
    def get_valor(self):
        return self.__valor

    #otro get para trader el metodo que obtenga la valrible encapusadla limiete
    def get_limite(self):
        return self.__limite

#Instancio la clase  Saldo  al crear un objeto para que funicione
CuentaSaldo = Saldo()
#creo objeto para llamar al valor oculto
#objeto._nombreClase__nombre atributo //llamo a los ocultos
print(CuentaSaldo.get_cuenta()) #llamo al mensaje
print(CuentaSaldo.get_valor()) #llamo el valor oculto del saldo
print(CuentaSaldo._Saldo__valor)
print("Cupo mAXIMO de retiro")
#llamo el 2 valir protegido el limiete
print(CuentaSaldo.get_limite())
