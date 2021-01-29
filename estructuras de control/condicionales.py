'''basicamente las condicionales establecen una condición que de cumplirse entra dentro del cuerpo
y ejecuta el codigo , tambien se pueden encadenar otras y además en caso contrario establecer un cuerpo
de codigo en caso de que no se cumpla nada'''
#if establece una condición
#elif encadena otra condición al if , pero no al contrario.
'''else significa de lo contrario y se cumple sin una condición , simplemente se cumple de no cumplirse
la condición que se encadeno al else'''

opcion=int(input("ingrese un numero del 1 al 2,\n*1 si es noche \n*2 si es de día\n-->"))

if (opcion==1):
    print("Buenas Noches Señor")
elif    (opcion==2):
    print("Ben Día Señor")
else:
    print("NO DIGÍTO UN DATO DEL TIPO NUMERO, O  INGRESO UN NUMERO MAYOR A 2 , VUELBA A INTENTARLO")