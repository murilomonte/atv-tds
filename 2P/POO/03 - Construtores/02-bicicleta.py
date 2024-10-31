# Implemente a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual,
# altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela,
# calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).

class Bicicleta:
    def __init__(self, velocidade, altura, pressao):
        self.definir_velocidade(velocidade)
        if 0 <= altura <= 5:
            self.altura_cela = altura
        else:
            raise ValueError('Altura inválida.')
        if 0 <= pressao <= 40:
            self.calibragem_pneus = pressao
        else:
            raise ValueError('Pressão inválida.')
    
    def __str__(self):
        return f'Velocidade atual: {self.veloc_atual}\nAltura da cela: {self.altura_cela}\nCalibragem dos pneus: {self.calibragem_pneus}'

    def definir_velocidade(self, velocidade):
        if 0 <= velocidade <= 30:
            self.veloc_atual = velocidade
        else:
            raise ValueError('Velocidade inválida.')
        
    def definir_altura_cela(self):
        if self.veloc_atual == 0:
            altura = int(input('Qual nova altura?: '))
            if 0 <= altura <= 5:
                self.altura_cela = altura
            else:
                print('Altura inválida')
        else:
            print('Impossível mudar a altura enquanto em movimento.')

    def calibrar_pneus(self):
        if self.veloc_atual == 0:
            pressao = int(input('Quanto quer calibrar?: '))
            if 0 <= pressao <= 40:
                self.calibragem_pneus = pressao
            else:
                print('Pressao inválida.')
        else:
            print('Imposível calibrar os pneus enquanto em movimento.')


def main():
    print('# Bicicleta')
    velocidade = int(input('Insira uma velocidade para a bicicleta: '))
    altura = int(input('Insira uma altura para a cela: '))
    pressao = int(input('Insira uma pressão para os pneus: '))

    bicicleta = Bicicleta(velocidade, altura, pressao)

    while True:
        print('Digite um número:\n1 - Alterar velocidade\n2 - Definir altura da cela\n3 - Calibrar pneus\n4 - Mostrar estado\n5 - Sair')
        usuario = str(input('> '))
        if usuario == '1' or usuario.upper() == 'V':
            velocidade = int(input('Qual a nova velocidade?: '))
            bicicleta.definir_velocidade(velocidade)

        if usuario == '2' or usuario.upper() == 'D':
            bicicleta.definir_altura_cela()

        if usuario == '3' or usuario.upper() == 'C':
            bicicleta.calibrar_pneus()

        if usuario == '4' or usuario.upper() == 'M':
            print(bicicleta)

        if usuario == '5' or usuario.upper() == 'S':
            break

if __name__ == '__main__':
    main()
