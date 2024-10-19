from random import *

print('Serviço de escolha de nome para animais de estimação')
print('-----------------------')

running = True
mascNames = [
    "Thor",
    "Max",
    "Rex",
    "Apollo",
    "Simba"
]

femNames = [
    "Luna",
    "Bella",
    "Mia",
    "Nina",
    "Zoe"
]

neutralNames = [
    "Charlie",
    "Sky",
    "Nala",
    "Alex",
    "Sam"
]

def showMenu():
    print('''Menu:
    gerar -> Obter nome.
    add -> Adicionar nome.  
    del -> Remover nome.
    nomes -> Imprimir nomes.
    sair -> sair.''')
showMenu()

while running == True:
    menuChoice = str(input('> ').lower())

    if menuChoice == 'gerar' or menuChoice == 'g':
        quantidade = int(input('\nVocê tem quantos animais?: '))
        for i in range(quantidade):
            print('''
O seu animal é:
1 -> Macho
2 -> Fêmea
3 -> Outro''')
            sex = int(input('> '))
            print('\nVocê deve chamar o seu animal de estimação de:')
            if sex == 1: print(choice(mascNames),'\n')
            elif sex == 2: print(choice(femNames),'\n')
            elif sex == 3: print(choice(neutralNames),'\n')
            else: print('Insira uma opção válida!')
        running = False

    elif menuChoice == 'add' or menuChoice == 'a':
        itemToAdd = str(input('Adicione o nome: '))
        print('''Esse nome é:
1 -> Masculino
2 -> Feminino
3 -> Neutro''')
        
        itemSex = int(input('> '))
        if itemSex == 1 and itemToAdd not in mascNames: mascNames.append(itemToAdd)
        elif itemSex == 2 and itemToAdd not in femNames: femNames.append(itemToAdd)
        elif itemSex == 3 and itemToAdd not in neutralNames: neutralNames.append(itemToAdd)
        else:
            print('O nome já existe na lista!')

    elif menuChoice == 'del' or menuChoice == 'd':
        itemToDel = str(input('Adicione o nome: '))
        print('''Esse nome é:
1 -> Masculino
2 -> Feminino
3 -> Neutro''')
        
        itemSex = int(input('> '))
        if itemSex == 1 and itemToDel in mascNames: mascNames.remove(itemToDel)
        elif itemSex == 2 and itemToDel in femNames: femNames.remove(itemToDel)
        elif itemSex == 3 and itemToDel in neutralNames: neutralNames.remove(itemToDel)
        else:
            print('O nome não existe na lista!')
    elif menuChoice == 'nomes' or menuChoice == 'n':
        print('Nomes masculinos:', mascNames)
        print('Nomes femininos:', femNames)
        print('Nomes neutros:', neutralNames)
    elif menuChoice == 'sair' or menuChoice == 's':
        running = False
    else:
        print('Insira uma opção válida!')