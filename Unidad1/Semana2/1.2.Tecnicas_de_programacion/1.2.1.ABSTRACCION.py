#ABSTRACCION
class Cajero:
    def __init__(self, marca, tipo, trato):
        self.marca = marca
        self.tipo = tipo
        self.trato = trato
    #metod par mostrar
    def detalles(self):
        print("Cajero Marca:    ",self.marca,"tipo:", self.tipo, " Trato:",self.trato)

#instanciar obejtos de la calse cajero D
#OBEJTO1 CAJERO TIPO PAGO
cajeroPago=Cajero("Diebol", "Pago", "ISLA")
#OBEJTO1 CAJERO TIPO RETIRO
cajeroRetiro=Cajero("NFC", "Retiro", "AGENCIA")
#OBEJTO1 CAJERO TIPO RECICLADOR
cajeroReciclador=Cajero("diebol", "Reciclador", "isla")

##llamo al metodo detalles de cada cajero e imprmire
cajeroPago.detalles()
cajeroRetiro.detalles()
cajeroReciclador.detalles()