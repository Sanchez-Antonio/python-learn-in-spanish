#contador hasta el 100

def contador(numero):
    if numero <=100:
        print(numero)
        numero +=1
        contador(numero)
    else:
        print("SE TERMINO EL CONTEO  llego al 100 :)")
print(contador(10))

#conteo regresivo
#se llama así misma y re ejecuta el bloque
#de codigo , hasta ya no entrar en el if y se ejecuta el else
def bomb(seconds):
    seconds-=1
    if seconds >=0:
        print(seconds)
        bomb(seconds)
    else: 
        print("PUM¡¡¡¡¡¡¡")

print(bomb(10))


