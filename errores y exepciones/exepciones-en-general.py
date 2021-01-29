try:
    dato1 = int(input("ingrese un numero para dividir :"))
    dato2 = int(input("ingrese un numero para dividir :"))
    operacion = dato1/dato2
    print(f"el resultado de la división es -->{operacion}")

except:
    print("Error Se Capturo Una Exepción , De Manera General")


print("""me ejecuto por que el programa sigue funcionando aunque tenga
exepciones por que todas són capturadas de manera general""")