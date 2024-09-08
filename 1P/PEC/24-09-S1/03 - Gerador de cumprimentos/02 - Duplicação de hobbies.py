from random import *

print('Gerador de Cumprimentos')
print('-----------------------')

executa = True
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

print('''
Menu:
    c -> Obter cumprimento.
    a -> Adicionar hobby.  
    d -> Remover hobby.
    p -> Imprimir hobbies.
    q -> sair.    
''')

while executa == True:
    menuChoice = str(input('> ').lower())

    if menuChoice == 'c':
        print(f'Aqui está seu cumprimento {nome}:')
        print(f'Você é {choice(adjetivos)} em {choice(hobbies)}!')
        print('De nada!')
        executa = False
    elif menuChoice == 'a':
        itemToAdd = str(input('Adicione o hobby: '))
        if itemToAdd not in hobbies:
            hobbies.append(itemToAdd)
        else:
            print('O hobby já existe na lista!')
    elif menuChoice == 'd':
        itemToDelete = str(input('Insira o hobby a ser removido: '))
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print('O hobby não está na lista!')
    elif menuChoice == 'p':
        print(hobbies)
    elif menuChoice == 'q':
        executa = False
    else:
        print('Insira uma opção válida!')