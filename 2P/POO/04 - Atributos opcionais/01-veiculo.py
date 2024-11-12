# Exercício: Classe Veiculo
# Objetivo:
# Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de controle de veículos. A atividade deve explorar a criação de construtores, atributos obrigatórios e opcionais, e o uso de métodos para exibir e atualizar as informações do veículo.Requisitos:

#     Atributos obrigatórios:
#     chassi (string)
#     marca (string): marca do veículo.
#     modelo (string): modelo do veículo.
#     ano (int): ano de fabricação do veículo.

# Atributos opcionais:

#     placa (string): placa do veículo.
#     cor (string): cor do veículo (padrão: "Não especificada").
#     proprietario (string): nome do proprietário do veículo (padrão: "Não especificado").
#     quilometragem (int): quilometragem atual do veículo (padrão: 0).

# Especificações da Classe

#     Método __init__: define os atributos obrigatórios e permite incluir os opcionais com valores padrão.
#     Método __str__: imprime todas as informações do veículo, incluindo os atributos opcionais.

class Veiculo:
    def __init__(self, chassi, marca , modelo, ano, placa = 'sem placa', cor = 'Não especificada', proprietario = 'Não especificado', quilometragem = 0 ):
        self.cadastro(chassi, marca , modelo, ano, placa, cor, proprietario, quilometragem)

    def __str__(self):
        return (f"Informações do Carro:\n"
                f"Chassi: {self.chassi}\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Ano: {self.ano}\n"
                f"Placa: {self.placa}\n"
                f"Cor: {self.cor}\n"
                f"Proprietário: {self.proprietario}\n"
                f"Quilometragem: {self.quilometragem}")

    def cadastro(self, chassi, marca , modelo, ano, placa = 'sem placa', cor = 'Não especificada', proprietario = 'Não especificado', quilometragem = 0 ):
        self.mudar_chassi(chassi)
        self.mudar_marca(marca)
        self.mudar_modelo(modelo)
        self.mudar_ano(ano)
        self.mudar_placa(placa)
        self.mudar_cor(cor)
        self.mudar_proprietario(proprietario)
        self.mudar_quilometragem(quilometragem)

    def mudar_chassi(self, chassi):
        self.chassi = chassi

    def mudar_marca(self, marca):
        self.marca = marca

    def mudar_modelo(self, modelo):
        self.modelo = modelo

    def mudar_ano(self, ano):
        self.ano = ano

    def mudar_placa(self, placa):
        self.placa = placa

    def mudar_cor(self, cor):
        self.cor = cor

    def mudar_proprietario(self, proprietario):
        self.proprietario = proprietario

    def mudar_quilometragem(self, quilometragem):
        if quilometragem >= 0:
            self.quilometragem = quilometragem
        else:
            self.quilometragem = "A quilometragem inválida."

def main():
    carro1 = Veiculo('12345ABC', 'Toyota', 'Corolla', 2020, 'XYZ-1234', 'Preto', quilometragem = 15000)
    print(carro1)
    print()
    carro1.cadastro('32145ABC', 'Mazda', 'MX-5', '1992', cor = 'Vermelho', quilometragem = -1)
    print(carro1)
    print()
    carro1.mudar_proprietario('Murilo')
    carro1.mudar_quilometragem(100)
    print(carro1)

if __name__ == '__main__':
    main()