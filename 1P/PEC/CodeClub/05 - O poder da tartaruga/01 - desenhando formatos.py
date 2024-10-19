from turtle import *

def forma(direcao, qtLados, angulo, tamanho):
    if direcao == 'esq':
        for i in range(qtLados):
            forward(tamanho)
            left(angulo)
    elif direcao == 'dir':
        for i in range(qtLados):
            forward(tamanho)
            right(angulo)

shape('turtle')

speed(5)
color('Purple')
pensize(5)

# Casa (quadrado)
forma('dir', 4, 90, 100)

# Teto (triângulo)
left(45)
forward(75)
right(90)
forward(25)
left(135)
forward(20)
right(90)
forward(10)
right(90)
forward(30)
left(45)
forward(30)

# Porta (retângulo)
penup()
right(45)
forward(100)
right(90)
forward(30)
right(90)

pendown()
forma('esq', 3, 90, 30)

done()