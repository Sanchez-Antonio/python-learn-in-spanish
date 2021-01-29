class carros():
    #se le llama metodo costructor def __init__(estado inicial)
    def __init__(self): #espesifica el estado inicial
                        #se contatenan con self
        self.__llantas=4 #con 2 __ encapsulo la variable para que solo sea modificable desde adentro de la clase
        self.color=None
        self.puertas=4  #a estas propiedades se les llama(estado inicial)
        self.encender=False
        #espesifica el estado inicial <---
        

#metodo para cambiar el valor de la propiead encender en cualquier objeto
   
    def activacion(self):
        self.encender = True
#metodo con 1 parametro , para comprobar si funciona o no el coche
    def informacion(self, parametro2):
        self.encender = parametro2
        if self.encender == True:
            print("FUNCIONA CORRECTO EL CARRO")
        else: 
            print("NO FUNCIONA CORRECTO EL STRATUS")
    #metodo apra ver la propiedad de las llantas
    def ver(self):
        return self.__llantas
#instancia
stratus = carros()
#metodo para cambiar el encender
stratus.activacion()
#se llama otro metodo y se le pasa el parametro
print(stratus.informacion(True)) 
print(stratus.informacion(False))
print(stratus.encender)
#al final queda en false ya  que fue el ultimo parametro que se le paso

#aunque se modifique el atributo si está protedigo desde el exterior es inmutable
stratus.__llantas =20
#imprimo con un metodo ya que está privado el atributo
print(stratus.ver())