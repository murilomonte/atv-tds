from random import *

#o usuário muda esta variável para terminar o jogo
jogando = True
pontuacao = 0

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=========
      
Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

#repetir, enquanto a variável 'jogando' estiver com valor 'True' (verdadeiro)
while jogando == True:
    print("\nEscolha uma porta (1,2 ou 3):")

    #pegue a porta escolhida e a armazene como um número inteiro (int)
    portaEscolhida = int(input())

    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    portaCerta = randint(1,3)

    #mostre ao jogador qual porta ele escolheu e qual era a porta certa
    print ("A porta escolhida foi a", portaEscolhida)
    print ("A porta certa é a", portaCerta)

    #o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida == portaCerta:
        pontuacao = pontuacao+1
        print ("Parabéns!")
    else:
        print ("Que peninha!")
        pontuacao = 0

    print("\nSua pontuação é:", pontuacao)

    #pergunte ao jogador se ele quer continuar jogando
    print ("\nVocê quer jogar de novo? (s/n)")
    resposta = input().upper()[0]

    #termina o jogo se o jogador digita 'n'
    if resposta == 'N':
        jogando = False
        