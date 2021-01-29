#creo las distintas clases
class Felino():
    def desplazamiento(self):
        print("-Tengo Instinto Por La Caza Nato-")

class Reptil():
    def desplazamiento(self):
        print("-Me Desplazo Por Terrenos Piedrosos A Grandes Vecocidades-")

class Marino():
    def desplazamiento(self):
            print("-Puedo Sobrevivir Bajo El Agua Y Nado Veloz-")

#creo una funcion para pasar por parametro el objeto así, puedo llamar
#el metodo correspondiente de la clase en la que se encuentre
#el obeto
#por medio de una función simple
def desplazamientovehiculos(objeto):
    objeto.desplazamiento()


creacion=Reptil()
#llamo a la funcion y le paso por parametro (la instancio u objeto)
desplazamientovehiculos(creacion)