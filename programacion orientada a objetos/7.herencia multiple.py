class Vehiculos():
    def __init__(self,marca,modelo):
            self.marca=marca
            self.modelo=modelo
            self.enmarcha = False
            self.acelera=   False
            self.frena=     False
    
    def arranca(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

class electricos():
    def __init__(self):
        self.poder ="100"

    def cargar(self):
        return "dispositivo cargado correctamente"

    def bateria(self):
        return self.poder

class bicisElectricas(Vehiculos,electricos):#sintaxis(hereda sus metodos y propieades pero solo 1 costructor)
    pass   #da prioridad a el primer parametro de clase, heradando a si su costructor
#por eso se le pasan parametros por que heredo el costrctor de la primera clase
viciE=bicisElectricas("mercurio","5000")

print(viciE.cargar())

#-al querer llamar al metodo bateria da error al no encontrar la variable del costructor segundo ya que no lo heredo (self.poder)

#print(viciE.bateria())

