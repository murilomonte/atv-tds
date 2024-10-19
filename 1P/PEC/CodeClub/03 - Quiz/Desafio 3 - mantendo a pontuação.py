print('''
Qual é a casa de Hogwarts de Luna Lovegood? 
a - Grifinória
b - Conserina
c - Lufa Lufa
d - Corvinal
''')
score = 0
resposta = input('Resposta: ')

if resposta == 'd':
    print('Correto! :)')
    score += 1
else:
    print('Incorreto :(')

print('''
Qual o patrono de Harry potter?
a - Gato Preto
b - Lhama
c - Cervo
''')
resposta = input('Resposta: ')

if resposta == 'c':
    print('Correto! :)')
    score += 1
else:
    print('Incorreto :(')

print('''
Qual é o nome do vilão principal da série Harry Potter?
a - Voldemort
b - Bellatrix Lestrange
c - Lucius Malfoy
d - Dolores Umbridge  
''')
resposta = input('Resposta: ')

if resposta == 'a':
    print('Correto! :)')
    score += 1
else:
    print('Incorreto :(')

print('Pontuação:', score)
print('Obrigado por jogar!')
