#LAS FUNCIONES SÓN UTILES PARA REDUCIR LAS LINEAS DE CODIGO A USAR Y HACER MÁS SENCILLAS LAS COSAS
#return(indica el final de una función y el valor que devuelve)
#none es para crear una variable , none como tal es un valor
def mult(a=None,b=None):
    if a == None or b == None:
        print("ahí un valor vacio corrijalo")
        return
    else:
        return a*b
#funcion para imprimir tablas con for
def multiplicar(numero):
    for i in range (1,11):
        multiplicacion = numero * i
        print(multiplicacion)
#funcion para multiplicar con while(mientras)
def multi(numero):
    i=10
    contador=1
    while contador<= i:
        dato = contador * numero
        print(dato)
        contador +=1
#funcion con el retorno de una resta de 2 parametros
def restar (a,b):
    return a-b
# las listas si se pueden modificar si se pasan por
 #una función, aunque sea una lista global, las variables no,
 #solo se modifican las que están encapsuladas dentro de la misma

def flista(numero):
    for key,value in enumerate(numero): #enumerate devuelbe pequeñas tuplas
        numero[key]*=3              #con la enumeracion (clave,valor)
                #solo ahí que pasarle una lista para que itere
                #con cada objeto
 
 #función con parametros incognita
def valores(*parametro):  #pasandole ** al paremetro genera valores
    for i in parametro:   #diccionarios
        print(i)
               