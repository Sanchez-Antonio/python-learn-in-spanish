import random




print("Adivino Tu Futuro")
inicio=(input("ingresa start para iniciar-->"))

while inicio=="start":
    print("PROGRAMA INICIADO")
    
    print("CON LAS ARTES OSCURAS ES POSIBLE SABER ALGO DE TI")

    nombre=input("AHORA INGRESA TU NOMBRE PARA CONTINUAR MUAJAJA-->")
    opcion=int(input("AHORA DIGÍTA 1 SI TE ATREVEZ A JUGAR--> SI NO VE CON MAMI A LLORAR-->"))
    
    if opcion==1:
        print("\n Bien HAZ ELIGIDO LA OPCIÓN 1 ")
        secreto=random.randint(0,4)
        print(f"(((QUE DEPARAN LOS DIOSES¡¡¡¡ PARA {nombre})))")
        if secreto==1:
            print(f"(((LOS DIOSES DEL OLIMPUS ME DICEN QUE {nombre}  Tendras Mucho Dinero¡¡¡)))")
            break
        elif secreto==2:
            print(f"(((LOS DIOSES DEL OLIMPUS ME DICEN QUE {nombre} Tendra Muchos Hijos :c¡¡¡)))")
            break
        elif secreto==3:
            print(f"(((LOS DIOSES DEL OLIMPUS REVELAN QUE {nombre} Tendras Un Accidente :c)))")
            break
        elif secreto==4:
            print(f"(((VEO  {nombre} Moriras En El 2033 :c ¡¡¡)))")
            break
    else:
        print("BALLA ALGO FUE MAL, INTENTA DE NUEVO EJEJE")
else: 
    print("no haz ingreso start correctamente")

print("***PROGRAMA FINALIZADO***")