#---------clase padre
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

    def estado(self):
        print(f"*Las Siguientes Propiedades*\nMarca({self.marca})\nmodelo({self.modelo})\nenmarcha({self.enmarcha})\nfrena({self.frena})\nacelera({self.acelera})")

#------clase con herencia de vehiculos
class Moto(Vehiculos):
        
        levantar = ""

        def reparar(self): #nuevo metodo solo para moto + los que ya heredo
             self.levantar = "reparando moto"
   
        def estado(self):#sustituye el metodo estado ya heredado (estado) *sobre escritura de metodos
            print(f"*Las Siguientes Propiedades*\nMarca({self.marca})\nmodelo({self.modelo})\nenmarcha({self.enmarcha})\nfrena({self.frena})\nacelera({self.acelera})\n({self.levantar})")

motoItalika = Moto("honda","2000")
motoItalika.reparar()
motoItalika.estado()
#si creo otra instancia que herede de moto,  hereda el metodo estado de moto ylos que tenga además de los que la clase SUPER PADRE ya había heradado a moto
print("--------------------")
#clase camion que hereda de vehiculos
class camion(Vehiculos): #creo una sub clase que herade de vehiculos

    def carga(self,cargar): #nuevo metodo cargar para los tipo camion
        self.cargado=cargar
        if self.cargado:
            return "está cargado el camion"
        else:
            return "no está cargado el camion"

troca = camion("extermador","1900")#creo otra instancia, pasandole los parametros de la clase padre
troca.arranca()
troca.acelerar()
troca.frenar()
troca.estado()
print(troca.carga(True)) #paso el parametro cargar para saber si está o no cargado y que retorne un mensaje 
