# Exercitando o processo de abstração, modele uma classe Relógio_Digital_Simples com seus estados e
# comportamentos. Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus
# atributos e execute os métodos criados. Recomendação: criar estados que possam ter seus valores alterados
# por seus métodos.

from datetime import datetime

class Relogio:
    def __init__(self):
        self.horario = datetime.now().time().strftime("%H:%M:%S")
        self.separar_hora()
        
    def __str__(self):
        return f'Hora: {self.hora}\nMinuto: {self.minuto}\nSegundo: {self.segundo}'
    
    def separar_hora(self):
        self.hora = self.horario[0:2]
        self.minuto = self.horario[3:5]
        self.segundo = self.horario[6:8]

    def valida_hora(self, hora):
        try:
            hora = datetime.strptime(hora, '%H:%M:%S')
            return hora
        except:
            return False
    def mostrar_hora(self):
        return self.horario
    
    def alterar_hora(self):
        self.horario = str(input('Qual hora deseja?: '))
        if not self.valida_hora(self.horario):
            raise ValueError("Horário inválido")
        self.separar_hora()
    
    def incrementar_hora(self):
        tempo = input('Quanto tempo adicionar? (HH:MM:SS): ')
        self.hora = int(self.hora) + int(tempo[0:2])
        self.minuto = int(self.minuto) + int(tempo[3:5])
        self.segundo = int(self.segundo) + int(tempo[6:8])
        self.horario = f'{self.hora}:{self.minuto}:{self.segundo}'
        if not self.valida_hora(self.horario):
            raise ValueError("Horário inválido")

def main():
    print('# Relógio digital')
    print('## Instância 1:')
    relogio = Relogio()
    relogio.alterar_hora()
    relogio.incrementar_hora()
    relogio.mostrar_hora()

    print('\n## Instância 2:')
    relogio1 = Relogio()
    relogio1.alterar_hora()
    relogio1.incrementar_hora()
    relogio1.mostrar_hora()

    print('\n## Método str')
    print('### Instância 1')
    print(relogio)

    print('n### Instância 2')
    print(relogio1)

    # print('# Relogio digital')
    # while True:
    #     print(f'\nHora atual: {relogio.mostrar_hora()}' )
    #     print('Digite um número:\n1 - Alterar hora\n2 - Incrementar hora\n3 - Mostrar hora\n4 - Sair')
    #     usuario = str(input('> '))
    #     if usuario == '1' or usuario.upper() == 'A':
    #         print('## Alterando hora:')
    #         relogio.alterar_hora()
    #     if usuario == '2' or usuario.upper() == 'I':
    #         print('## Incrementando Hora:')
    #         relogio.incrementar_hora() 
    #     if usuario == '3' or usuario.upper() == 'M':
    #         print(f'Hora atual: {relogio.mostrar_hora()}' )
    #     if usuario == '4' or usuario.upper() == 'S':
    #         break

if __name__ == '__main__':
    main()
        