''' while = mientras
hasta que la condición se cumpla va iterar si no se cumple , simplemente no entra al while
example -->

contador del 1 al 100 '''


#mientras el contador sea menor o igual que 100 seguira iterando 

contador=0

while contador <= 100:
    print(f"Iterando el valor actual es -->\t{contador}")
    contador +=1 
    
#cada vez que itera el contador va sumando 1 (contador +=1 ) para logar ser 101 y ya no entrar
'''cuando sale del bucle simplemente imprime lo que está fuera, si "NO" el while directamente
imprime el mensaje'''

print("Salí del bucle")


