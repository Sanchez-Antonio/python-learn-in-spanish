"""{}colección no ordenada y sin elementos repetidos. Los usos básicos de éstos incluyen 
verificación de pertenencia y eliminación de entradas duplicadas."""
coleccion= {1,2,3,4,5}
coleccion.add(1)
#se agrego el 1 con el metodo add pero no se agraga ya que no se puede duplicar 1 mismo objeto
coleccion.add(6)
print(coleccion)
#ahora se agrega el 6 correctamente ya que no ahí otro objeto igual 

#se puede preguntar si se encuntra algun objeto en particular en una coleccion  con in 
#y arrojara un valor verdadero  o falso. Si es verdad o no . 
print(1 in coleccion)

#uso de conjunto para la eliminación de objetos duplicados
lista=[1,2,3,3,3,3,4,4,4,5,5,5]
#creamos un conjunto vacio y luego le pasamos la lista para almacenar los valores de la lista sin repetir
conjunto=set(lista)
print(conjunto)
#ahora hago hago lo contrario creo una lista y le paso el conjunto para convertirlo a lista , ya sin valores repetidos
new=list(conjunto)
print(new)