from turtle import *

def forma(direcao, qtLados, tamanho):
    angulo = 360 / qtLados
    for count in range(qtLados):
        forward(tamanho)
        if direcao == 'esq':
            left(angulo)
        elif direcao == 'dir':
            right(angulo)

shape('turtle')
speed(5)
color('Purple')
pensize(5)

forma('esq', 3, 100)

done()