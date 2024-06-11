#3 HARENCIA
class Cuenta:
    pass
    def __init__(self,numero, tipo): #defino constructor
        #atributos
        self.numero = numero
        self.tipo =tipo
        #defino comporatmiento
    def descripcion(self):
        return '{}: es una cuenta de tipo :{}'.format(self.numero,self.tipo)

#CREAR CLASE PARA HEREDAR
class Ahorro(Cuenta):
    def ahorro(self,tipoAhorro):
        return '{}: es una cuenta de tipo :{}'.format(self.numero,tipoAhorro)
class Flexible(Cuenta):
    def flexible(self,tipoFlexible):
        return '{}: es una cuenta de tipo :{}'.format(self.numero,tipoFlexible)

class Corriente(Cuenta):
    def corriente(self,tipoCorriente):
        return '{} es una cuenta de tipo {}'.format(self.numero,tipoCorriente)

#VAMOS A CREAR OBJETOS PARA INSTANCIA LAS CLASES
#OBJETO1 de la clase herencia Ahorro
nueva_cuenta1 = Ahorro('349839930100','Cuenta_Ahorro')
##llamo el metddo heredado descripcion
print(nueva_cuenta1.descripcion())

#OBJETO2 de la clase herencia flexible
nueva_cuenta2 = Flexible('2202034519','Cuenta_FELXIBLE')
##llamo el metddo heredado descripcion
print(nueva_cuenta2.descripcion())

#OBJETO2 de la clase herencia CORRIENTE
nueva_cuenta3 = Corriente('2204410001','Cuenta_Corriente')
##llamo el metddo heredado descripcion
print(nueva_cuenta3.descripcion())