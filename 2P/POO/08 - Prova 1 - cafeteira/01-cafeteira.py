# Aluno: Murilo Pereira Monte
class Cafeteira:
    def __init__(self, cap_max=500):
        self.__nivel_agua = 0
        self.__capacidade_reservatorio = cap_max
        self.__tipo_cafe = None
        self.__temperatura = 0
        self.__ligado = False
        self.__tipos_cafe = ['EXPRESSO', 'CAPPUCCINO', 'LATTE', 'CLASSICO']
        print('# Cafeteira criada!')
        
    def __str__(self):
        return (
            '## Máquina de café\n'
            f'   Nível da água: {self.__nivel_agua}\n'
            f'   Capacidade máxima: {self.__capacidade_reservatorio}\n'
            f'   Tipo cafe: {self.__tipo_cafe}\n'
            f'   Temperatura: {self.__temperatura}\n'
            f'   Ligado: {self.__ligado}\n'
        )
    def __verificar_status(self):
        if self.__ligado == False:
            raise ValueError('Você não pode fazer isso enquanto a cafeteira estiver desligada.')
    
    def ligar(self):
        if self.__ligado:
            print('Máquina já ligada.')
        else:
            self.__ligado = True
        print(f'Ligado: {self.__ligado}')
    
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        else:
            print('Máquina já desligada.')
        print(f'Ligado: {self.__ligado}')
        
    # adiciona água ao reservatório, respeitando o limite máximo.
    def adicionar_agua(self, quantidade):
        if self.__nivel_agua + quantidade > self.__capacidade_reservatorio:
            raise ValueError('Quantidade de água maior que a capacidade do reservatório.')
        else:
            self.__nivel_agua += quantidade
        print(f'Nível da água: {self.__nivel_agua}\n')
            
    # ajusta a temperatura da água, validando os limites.
    def __aquecer_agua(self, temp):
        self.__verificar_status()
        if 70 <= temp <= 100:
            self.__temperatura = temp
        else:
            raise ValueError('Temperatura fora do limite. A temperatura deve ser entre 70°C a 100°C')
        print(f'Temperatura: {self.__temperatura}')
        
    # seleciona o tipo de café.
    def __selecionar_tipo(self, tipo):
        self.__verificar_status()
        if tipo.upper() in self.__tipos_cafe:
            self.__tipo_cafe = tipo.upper()
        else:
            raise ValueError('Tipo de café inválido.')
        print(f'Tipo cafe: {self.__tipo_cafe}')

    # prepara o café se a máquina estiver ligada, com água suficiente e na temperatura adequada.
    def preparar_cafe(self, quant_cafe, temp, tipo='classico'):
        self.__verificar_status()
        print('## Novo café')
        if (quant_cafe > self.__nivel_agua) or (self.__nivel_agua == 0):
            raise ValueError('Quantide de água insuficiente.')
        print('Preparando café.')
        self.__aquecer_agua(temp)
        self.__selecionar_tipo(tipo)
        self.__nivel_agua -= quant_cafe
        print('Café pronto!')
        print(f'Nível da água: {self.__nivel_agua}\n')
        
def main():
    cafeteira1 = Cafeteira(cap_max = 500)
    cafeteira1.ligar() # Ligando máquina
    cafeteira1.adicionar_agua(500) # Adicionando água
    cafeteira1.preparar_cafe(quant_cafe = 250, temp = 100, tipo = 'cappuccino') # Café 1
    cafeteira1.preparar_cafe(quant_cafe = 100, temp = 70, tipo = 'latte') # Cafe 2
    cafeteira1.desligar()

    cafeteira2 = Cafeteira(cap_max = 1000)
    cafeteira2.ligar() # Ligando máquina
    cafeteira2.adicionar_agua(1000) # Adicionando água
    cafeteira2.preparar_cafe(quant_cafe = 500, temp = 100, tipo = 'classico') # Café 1
    cafeteira2.preparar_cafe(quant_cafe = 450, temp = 70, tipo = 'expresso') # Cafe 2
    cafeteira2.desligar()
    
    print('\nTeste de validação.')
    cafeteira3 = Cafeteira(cap_max = 250)
    cafeteira3.ligar()
    cafeteira3.adicionar_agua(500) # Erro
    cafeteira3.preparar_cafe(quant_cafe = 500, temp = 100, tipo = 'classico') # Erro
    cafeteira3.preparar_cafe(quant_cafe = 450, temp = 70, tipo = 'expresso') # Erro
    
if __name__ == '__main__':
    main()