# Criar uma classe que represente o Jogo: Pedra, Papel, Tesoura. O jogo é jogado entre um jogador e o computador. 
# Crie um método principal (main()) para executar a classe.
from random import choice

class Jokenpo:
    humano = None
    pc = None
    alternativas = [
        'PEDRA',
        'PAPEL',
        'TESOURA'
    ]

    def rodadaHumano(self, rodada):
        self.humano = rodada.upper()
    
    def rodadaPc(self):
        self.pc = choice(self.alternativas)
    
    def vencedor(self):
        if self.humano == self.pc:
            return "Empate!"
        elif \
        (self.humano == 'PEDRA' and self.pc == 'TESOURA') or \
        (self.humano == 'PAPEL' and self.pc == 'PEDRA') or \
        (self.humano == 'TESOURA' and self.pc == 'papel'):
            return "Você venceu!"
        else:
            return "O computador venceu!"
        
def main():
    jogo = Jokenpo()
    print("// -- Jokenpo python -- //")
    print("Escolha uma opção: 'Pedra', 'Papel', 'Tesoura' ou 'Sair':")
    while True:
        usuario = str(input("> ").upper())
        if usuario == 'SAIR':
            print("Encerrando o jogo.")
            break
        if usuario not in jogo.alternativas:
            print('Escolha inválida. Tente novamente.')
        else:
            jogo.rodadaHumano(usuario)
            jogo.rodadaPc()
            print(jogo.vencedor())
        
if __name__ == "__main__":
    main()