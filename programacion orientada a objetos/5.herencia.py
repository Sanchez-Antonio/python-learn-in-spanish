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


#al heredar se hereda todo, metodos, y metodo costructor etc.
class Moto(Vehiculos):#sintaxis para heradar(vehiculos -->hereda a motos)
    pass


motoItalika = Moto("honda","2000")
motoItalika.estado()