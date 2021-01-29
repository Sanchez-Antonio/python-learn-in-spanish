#los diccionarios nos permiten además de almacenar cualquier tipo de valor 
# identificar cada elemento por una clave (Key).
#Para definir un diccionario, se encierra el listado de valores entre llaves. 
# Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos.
diccionario = {"ramón":1999,"jonny":2000,"alexis":2001,"luis":2000}

print("a continuación las edades de mis amigos con su nombre:) -->")
#con un for usando el metodo itemps recorre la clave y valor de cada objeto (key),(value)
for key,value in  diccionario.items():
    print(key,value)

#para mostrar el valor de una determinada clave -->
diccionario["alexis"]
#para cambiar el valor de una determinada clave
diccionario["alexis"]=99
#borrar algúna clave con su valor
del(diccionario["jonny"])
#se pueden usar operadores para  trabajar valores (valor +=1) usando de referencia la clave
diccionario["alexis"]+=1
#tambien se pueden sumar distintos valores de claves alexis + luis
suma=diccionario["alexis"]+ diccionario["luis"]
print(suma)

#agregar diccionario dentro de una lista
lista=[]
lista.append(diccionario)
