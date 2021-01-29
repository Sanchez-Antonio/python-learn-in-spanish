class carro():#clase
    def __init__(self):#costructor
        self.__llantas = 4 #___deniega el acceso a los atributos y metodos internos de la clase desde el exterior

#funcion para retnronar el atributo la clase
    def ver(self):
        return self.__llantas

#instanciamiento
stratus = carro()
# no se puede modificar un atributo desde el exterior
stratus.__llantas = 10
#solo se puede ver llamando un metodo ya que es privado y solo se accede
#desde dentro de la clase
print(stratus.ver())

