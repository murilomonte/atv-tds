from random import *

print('Gerador de Cumprimentos')
print('-----------------------')

adjetivos = [
    'maravilhoso',
    'acima da média',
    'excelente',
    'explêndido',
    'magnifico',
    'incrível'
]

hobbies = [
    'andar de biscicleta',
    'programar',
    'fazer chá'
]

nome = str(input('Qual o seu nome?: '))
print(f'Aqui está seu cumprimento {nome}:')

print(f'Você é {choice(adjetivos)} em {choice(hobbies)}!')
print('De nada!')