from turtle import *

def forma(direcao, qtLados, angulo, tamanho):
    for count in range(qtLados):
        forward(tamanho)
        if direcao == 'esq':
            left(angulo)
        elif direcao == 'dir':
            right(angulo)

shape('turtle')

speed(1000)
color('Purple')
pensize(5)

# Pentágono
forma('esq', 5, 72, 100)

penup()
forward(200)
pendown()

# Héxagono
forma('esq', 6, 60, 100)

penup()
backward(300)
pendown()

# Circulo
forma('esq', 360, 1, 1)

done()