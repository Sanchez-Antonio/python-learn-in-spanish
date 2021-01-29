class coche():
    def __init__(self):
        self.__puertas=4
        self.__estructura ="metal"
        self.__gasolina = False
        self.__espejos = True

    def arrancar(self): #metodos con recursividad
        self.__gasolina = True
        if self.__chequeo()== True:
            print("el auto se reviso y está funcionando correctamente y con carga de gasolina")
        else :
            print("un error inesperado en el chequeo del auto")

    def __chequeo(self):#metodo encapsulado __
            print("REALIZANDO CHEKEO INTERNO")
            if self.__puertas == 4 and self.__estructura =="metal" and self.__gasolina == True and self.__espejos == True:
                print("el coche está funcionando correctamente")
                return True
            else: 
                print("algo fallo revisa que todo esté en orden ") 
                return False  


stratus = coche()

stratus.arrancar()

#encapsulamiento de metodos,  __ solo es posible acceder desde la misma clase
# de manera global no es posible acceder a dichos metodos