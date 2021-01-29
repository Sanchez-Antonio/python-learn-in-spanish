#raise (lanza exepciones de forma voluntaria)

dato = int(input("ingresa cuantas veces has estado en la carcel :"))
if dato <=1 :
    print("FELICIDADES QUEDASTE REGISTRADO")
else:
    raise ValueError ("EL PROGRAMA CALLO INESPERADAMENTE") 

#se coloca cualquier nombre de error reservado y se le le
#puede asignar un mensaje personalizado



#programa que, crear un error para romper el programa en caso
#de que la persona hubiese estado más de 2 veces en la carcel 