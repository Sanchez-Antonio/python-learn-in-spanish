from collections import deque
#libreria para crear colas

#(pilas)el primero que entra es el ultimo que sale
lista=["ladrillo2"]
#agrega un valor al final
lista.append("ladrillo1")
#vacia el valor del final
lista.pop()
print(lista)

#(colas)el primero que entra , primero se va
colas=deque()
colas=(["persona3","persona2","persona1"])
colas.pop()
print(colas)