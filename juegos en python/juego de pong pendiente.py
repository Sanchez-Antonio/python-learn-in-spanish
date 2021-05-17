import turtle

#ventana y juego base
windows = turtle.Screen()
windows.title("Juego De Pong")
windows.bgcolor("black")
windows.setup(width = 800,height=600)
windows.tracer(0)

#--------------
#jugador A
jugadorA = turtle.Turtle()
#metodo para aparicion instantanea
jugadorA.speed(0)
#forma que tendra
jugadorA.shape("square")
jugadorA.color("white")
#quita la linea de movimiento de donde partio el objeto
jugadorA.penup()
#ubicación del objeto
jugadorA.goto(-350,0)
#cambio del tamaño del objeto
jugadorA.shapesize(stretch_wid=5,stretch_len=1)

#------------jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5,stretch_len=1)


#------------PELOTA
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
#separar los ejer de x y y, para cambiar las cordenadas en las que se ira moviendo
pelota.dx = 3
pelota.dy= 3

#linea de división del campo
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)


#funcion jugador A
def jugadorA_UP():
#y = a cordenada de jugador A
    y=jugadorA.ycor()
    y +=20
    #refrescado de la cordenada
    jugadorA.sety(y)
#teclado
windows.listen()
windows.onkeypress(jugadorA_UP,"w")
#------------------------------------
def jugadorA_down():
    y=jugadorA.ycor()
    y -=20
    jugadorA.sety(y)
windows.listen()
windows.onkeypress(jugadorA_down,"s")

#jugador B Funcion
def jugadorB_UP():
    y=jugadorB.ycor()
    y +=20
    jugadorB.sety(y)
windows.listen()
windows.onkeypress(jugadorB_UP,"Up")

def jugadorB_down():
    y=jugadorB.ycor()
    y -=20
    jugadorB.sety(y)
windows.listen()
windows.onkeypress(jugadorB_down,"Down")




#bucle de refrescado
while True:
    windows.update()
#movimiento de la pelota llamando a los metodos que ya use en pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor()+ pelota.dx)


#bordes
if pelota.ycor()> 290:
    pelota.dy *=-1
if pelota.ycor()< -290 :
    pelota.dy *=-1