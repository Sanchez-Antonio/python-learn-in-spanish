#se capturan las execiones para no frenar el programa por un error
try:
    dato1 = int(input("ingre un numero para dividir :"))
    dato2 = int(input("Ingrese un segundo numero :"))
    resultado = dato1/dato2
    print(f"El Resultado ES --> {resultado}")

except ValueError as DatoErroneo: #se puede apodar el error con as *** y el apodo
    print("El Tipo De Dato Fue Erroneo") #se ejcuta el bloque del exept al capturarla

except ZeroDivisionError : # sin apodo
    print("No Se Puede Dividir Por 0")
#caso contrario al exept se puede usar else , para ejecutarse cuando el
#exep no capture un error
else:
    print("me ejecuto si el exept no entra en ningun error")
#SI NO SE CAPTURA EL ERROR SE DETIENE EL PROGRAMA

finally:#se ejecuta pase lo que pase, error o no 
    print(">:)")