#for #recorre (itera)objetos 
#for normal

lista=[1,2,3,"jonny","alexis","ramón"]
for i in  lista:
    print(i)

#for con funcion de rango
for i in range(0,5):
    print(i)

#for saltado de 2 en 2
for i in range(0,10,2):
    print(i)

#for para multiplicar listas por indice
prueba=[1,2,3]
indice=0
for i in prueba:
    prueba[indice]*=10
    indice+=1
print(prueba)
#tambien se pueden crear listas de rangos con for
print(list(range(1,411111111111111111)))