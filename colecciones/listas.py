"""La lista en Python son variables que almacenan arrays, 
internamente cada posición puede ser un tipo de datos distinto. se ponen entre corchetes y són
las más manejables"""



lista = [["ramón","jonny","alexis"],["oscar","luis david"]]

lista2 = ["pedro","roberto",21,13.5,"hola"]
#print(lista2[1:])

lista3= [1,2,3,4,6]
#remplazamos el objeto del inidice 4 por el objeto 5
lista3[4]=5
#agregamos el 6 que remplazamos 
lista3.append(6)
lista4 = [7,8,9,10]
#unimos 2 listas
lista5= lista3 + lista4
#print(lista5)

abecedario = ["a","b","c","d"]
#remplazamos del inidce 2 al 4 por A Y B 
abecedario[2:4]= "A","B"
#print(abecedario)

#anidadas
list1=[1,2]
list2=[3,4]
list3=[5,6]
list4=["seis","siete"]
list5=[list1,list2,list3,list4]
           #de la list2 , quiero el valor del inidice 1
#print(list5[1][1])