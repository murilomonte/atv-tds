# 1. Atributos:
# - Número do cartão (gerado automaticamente e composto de 8 caracteres alfanuméricos)
# - Data e hora de entrada (registrada automaticamente no momento da criação do cartão)
# - Status do cartão (ativo ou finalizado)
# - Data e hora de saída (registrada quando o cartão é finalizado)
# - Valor total (calculado no momento da saída com base no tempo de permanência e tarifa por hora)

# 2. Métodos sugeridos
# - Um método para registrar saída, que define a data e hora de saída, altera o status para "finalizado" e calcula o valor total a ser pago.
# - Um método para consultar o valor acumulado, permitindo ao cliente verificar o custo do estacionamento antes de finalizar.
# - Um método para calcular o valor a ser pago, condiderando:
    # - Até 2h de permanência, R$ 8,00
    # - Acima de 2h de permanência cobrar R$ 0,50 a cada fração de 15 min

# 4. Requisitos de Validação:
# - O número do cartão deve ser único e composto de exatamente 5 caracteres numericos.
# - O status só pode ser alterado para "finalizado" se a saída for registrada.
# - O tempo de permanência deve ser calculado em horas completas e frações, considerando uma tarifa fixa por hora.
# - A data e hora de saída não podem ser anteriores à data e hora de entrada.

# 5. Teste:
# - Crie pelo menos três objetos da classe, representando cartões de estacionamento diferentes.
# - Demonstre os métodos implementados e suas validações em ação.
from random import randint, choices
from datetime import datetime
import string

class CartaoEstac:
    def __init__(self, entrada):
        self.__numC = self.__get_numCartao() # alfanum 8 char
        self.__statusC = 'Ativo' # ativo or finalizado
        self.__entrada = self.__val_dataHora(entrada)
        self.__saida = None
        self.__tarifa = 4 # 4 reais por hora; 0.50 para cada 15min quando acima de 2h
    
    @property
    def numC(self):
        return self.__numC
    
    @property
    def statusC(self):
        return self.__statusC

    @property
    def tarifa(self):
        return self.__tarifa
    
    @property
    def entrada(self):
        return self.__entrada
    
    @property
    def saida(self):
        return self.__saida

    def __str__(self) -> str:
        return f'## Cartão de Estacionamento\nNúmero ID: {self.__numC}\nStatus: {self.__statusC}\nTarifa: R${self.__tarifa * 2} p/ 2 horas\nEntrada: {self.__entrada}\nSaida: {self.__saida}\n'
    
    def __get_numCartao(self):
        digitos = ''.join(choices(string.digits, k=5))
        letras = ''.join(choices(string.ascii_letters, k=3))
        return digitos + letras

    def __val_dataHora(self, momento, formato="%d/%m/%Y %H:%M"):
        try:
            momentoVal = datetime.strptime(momento, formato)
            return momentoVal
        except ValueError:
            raise ValueError("Data e hora inválidas!")
        
    def registrar_saida(self, saida):
        self.consultar_valor(saida)
        self.__saida = saida
        self.__statusC = 'Finalizado'
        print(self.__str__())
        print('Volte sempre!')
    
    def consultar_valor(self, saida):
        valDoRestante, valTotal = self.__get_valor(saida)
        if valDoRestante == 0:
            print(f'## Consulta\nHora: {saida}\nTarifa: R${self.__tarifa}\nTotal a pagar: R${valTotal}')
        else:
            print(f"## Consulta:\nHora: {saida}\nTarifa: R${self.__tarifa}\nValor por tempo excedente: R${valDoRestante}\nTotal a pagar: R${valTotal}\n")
 
    def __get_valor(self, saida):
        saida = self.__val_dataHora(saida)
        if saida <= self.__entrada:
            raise ValueError("Data e hora inválidas!")
        
        totalMin = (saida - self.__entrada).total_seconds() / 60
        
        if totalMin > 120:
            minRestante = (totalMin - 120)
            valDoRestante = ((minRestante / 15) * 0.5)
            valTotal = valDoRestante + (self.__tarifa * 2)
        else:
            valDoRestante = 0
            valTotal = self.__tarifa * 2
        return round(valDoRestante, 2), round(valTotal, 2)

def main():
    cartao = CartaoEstac("12/07/2024 20:23")
    # print(cartao)
    cartao.consultar_valor("13/07/2024 00:25")
    cartao.registrar_saida("13/07/2024 01:25")

if __name__ == "__main__":
    main()