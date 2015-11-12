# coding: utf-8
import turtle
import tunnel


Donatello = turtle.Turtle()
Donatello.color('purple')
Raphael = turtle.Turtle()
Raphael.color('red')
Michelangelo = turtle.Turtle()
Michelangelo.color('orange')
Leonardo = turtle.Turtle()
Leonardo.color('blue')


Ninjaturtles = {"Donatello":Donatello,
                "Michelangelo":Michelangelo,
                "Raphael": Raphael,
                "Leonardo":Leonardo}

playerself = "Michelangelo"



def tupdate(hvem, hva, hvor):
    if hva == "goto":
        Ninjaturtles[hvem].goto(hvor[0], hvor[1])


def cmdup():
    pos = Ninjaturtles[playerself].position()
    list = [pos[0], pos[1] + 100]
    tunnel.gi_beskjed(playerself,"goto",list)


def cmddown():
    pos = Ninjaturtles[playerself].position()
    list= [pos[0], pos[1] - 100]
    tunnel.gi_beskjed(playerself, "goto",list)

def cmdright():
    pos = Ninjaturtles[playerself].position()
    list = [pos[0] + 100, pos[1]]
    tunnel.gi_beskjed(playerself, "goto",list)

def cmdleft():
    pos = Ninjaturtles[playerself].position()
    list= [pos[0] - 100, pos[1]]
    tunnel.gi_beskjed(playerself, "goto",list)



turtle.onkey(cmdup, "Up")
turtle.onkey(cmdup, "w")

turtle.onkey(cmddown, "Down")
turtle.onkey(cmddown, "s")

turtle.onkey(cmdright, "Right")
turtle.onkey(cmdright, "d")

turtle.onkey(cmdleft, "Left")
turtle.onkey(cmdleft,  "a")

if __name__ == '__main__':
    turtle.onkey(turtle.reset, "space")
    tunnel.init(tupdate)


turtle.listen()
turtle.mainloop()