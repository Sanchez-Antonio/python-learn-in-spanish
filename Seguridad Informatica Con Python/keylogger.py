import pynput.keyboard

def presionada(key):
        print(f"la tecla presionada es : {key}")

def liberar(key):
    print(f"tecla liberada  :{key}")

def convertir():
    pass

with pynput.keyboard.Listener(on_press=presionada, on_release=liberar) as listen:
    listen.join()