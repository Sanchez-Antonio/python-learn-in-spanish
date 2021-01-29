
saldo=0
gamespersonal=[]
while True:
    print("""\t \n***GOOGLE COINS***\n-compra juegos con coins virtuales\n
    1.Comprar coins
    2.Consultar Saldo
    3.ver lista de juegos comprados
    4.Compra juegos
    5.Salir Del Programa""")
    print()
    
    opcion=int(input("Ingresa una opción a continuacion -> "))
    
    game1=["silent hill"]
    game2=["San Andreas"]
    game3=["Dead Frontier"]
    
    if opcion==1:
        tarjeta=len(str(input("ingrese los 10 digítos de su tarjeta de credito a continuacion -> ")))
        if tarjeta>=10:
            bcoins=float(input("Ingrese a continuacion cuanto dinero desea cargar a su cartera de bit coins-->$ "))
            saldo+=bcoins
            print(f"\nFelicidades El Pago Se Realizo Con Exito SU Saldo EN BITCOINS ES DE --> ${saldo}")
            print("\tGracias Por Usar Nuestro Servicio DE Pago :3")
        else:
            print("\nLO Sentimos NO Ingreso El NUmero COrrecto Intente De Nuevo")
    elif opcion==2:
        print(f"\tSu Saldo Actual Es De --> ${saldo}")
        print("\t\n-google coins le desea un lindo día-")
    elif opcion==3:
        print(f"Actualmente Cuenta Con Los Siguientes Juegos --> {gamespersonal}")
    elif opcion==4:
        print(f"Actualmente Cuenta Los Siguientes Juegos***{gamespersonal}***")
        print("\nSi Desea COmprar uno de lo siguientes juegos digíte la opcion\n")
        seleccion=int(input(f"1. $500 {game1}\n2.$1000 {game2}\n3.$5000 {game3}\n--> "))
        if seleccion==1 and saldo>=500:
                saldo-=500
                print("TOTAL DE COBRO = $500")    
                gamespersonal.append(game1)
                print("!COMPRA REALIZADA CON EXITO¡")
                print(f"Su Saldo Actual Es De--> ${saldo}")
        elif seleccion==2 and saldo>=1000:
            saldo-=100
            print("TOTAL DE COBRO = $1000")
            gamespersonal.append(game2)
            print("!COMPRA REALIZADA CON EXITO¡")
            print(f"Su Saldo Actual Es De--> ${saldo}")
        elif seleccion==3 and saldo>=5000:
            saldo-=5000
            print("TOTAL DE COMPRO = $5000")
            gamespersonal.append(game3)
            print("!COMPRA REALIZADA CON EXITO¡")
            print(f"SU Saldo Actual Es De --> ${saldo}")
        else:
            print("*NO CUENTA CON EL SALDO SUFICIENTE , INGRESE MÁS SALDO Y REGRESE DE NUEVO*")
    elif opcion==5:
        print("!GRACIAS POR USAR NUESTRA TIENDA DE COMPRAS¡")        
        break
    else:
        print("ALGO SALIO MAL, INTENTELO DE NUEVO")