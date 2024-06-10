#POLIMORFISMO
#Defino 2 clase de CAJERO ATM_RETITRO_ ATM_DEPOSITARIO_ ATM MIXTO PARA  PARTICAR PLOMORMISMOS
#DEFINO CLASE ATM
class ATM:
    def __init__(self,cassete):
        self.cassete =cassete
    def tipoATM(self):
        pass
#clase hijas tipo de cajero
class ATM_RETIRO(ATM):
    def tipoATM(self):
        print(f"ATM Solo para hacer retiros, cassete = {self.cassete}")
#calse de ATM DEPOSITRAIO
class ATM_DEPOSITRAIO(ATM):
    def tipoATM(self):
        print(f"ATM Solo para depósitos, cassete = {self.cassete}")

#creo obejtos para instacnias clases
new_ATM_RETIRO = ATM_RETIRO("10")
#LLAMO AL METODO TIPO DE CAJERO y veo el tipo de cassete
new_ATM_RETIRO.tipoATM()

#LLAMO AL METODO TIPO DE CAJERO y veo el tipo de cassete
new_ATM_DEPOSITRAIO = ATM_DEPOSITRAIO("20")
new_ATM_DEPOSITRAIO.tipoATM()
#...












