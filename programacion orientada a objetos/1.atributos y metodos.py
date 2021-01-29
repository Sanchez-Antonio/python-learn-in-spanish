
#------------------encapsulamiento----------------------------------- 
#creación de la clase
class makepeople():
#propiedades del metodo padre
    eyes = 2
    life = False
    hands = 2
    foot = 2
    hair = True
#metodo
    def resucitar(self): #self(hace referencia al propio objeto, es decir el parametro que se le pasa es el objeto) 
        self.life = True    #self.para contatenar con el objeto(self)
#metodo para verificar el estado
    def estado(self):
        if self.life == True:
            print("esta vivo")
        else:
            print("está muerto")
#---------------------------------encapsulamiento------------------
# se encuentra encapsulada la clase, sus intancias solo són
# accesibles desde afuera con metodos


#instanciar la clase(se crea el objeto)
alexcibor = makepeople()
#segundo objeto instanciado a la clase padre
cristiancibor = makepeople()
print(f"el cibor alex se encuentra--> {alexcibor.life}")

#llamo al metodo para cambiar una de sus propiedades y darle vida
alexcibor.resucitar()

print(f"el cibor alex se encuentra -->{alexcibor.life}")
#uso un metodo para imprimir el estado del cibor ya que 
#está encapsulado desde afuera
print(alexcibor.estado())

print("-------segunda instancia estado--------")
print(cristiancibor.estado())
