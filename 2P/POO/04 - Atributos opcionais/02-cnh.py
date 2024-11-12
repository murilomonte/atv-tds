# Utilizando o processo de abstração, implemente uma classe em python que represente uma
# carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor
# da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações
# possíveis. Crie objetos para testar os métodos implementados.

from datetime import datetime

class Cnh:
    def __init__(self, nome, validade, categoria, cpf, observacoes='Sem observações'):
        self.cpf = cpf
        self.cadastro(nome, validade, categoria, observacoes)

    def separar_data(self, data):
        self.dia = data[0:2]
        self.mes = data[3:5]
        self.ano = data[6:10]

    def __str__(self):
        return (f"Informações da CNH:\n"
                f"Nome: {self.nome}\n"
                f"Validade: {self.validade}\n"
                f"Categoria: {self.categoria}\n"
                f"CPF: {self.cpf}\n"
                f"Observações: {self.observacoes}")

    def cadastro(self, nome, validade, categoria, observacoes):
        self.add_nome(nome)
        self.add_validade(validade)
        self.add_categoria(categoria)
        self.add_observacoes(observacoes)

    def add_nome(self, nome):
        self.nome = nome

    def add_validade(self, validade):
        self.dataAtual = datetime.now().strftime("%d/%m/%Y")
        self.separar_data(self.dataAtual)

        if int(validade[6::]) - int(self.ano) == 10:
            self.validade = validade
        else:
            self.validade = 'Validade inválida.'

    def add_categoria(self, categoria):
        if categoria in 'ABCDE':
            self.categoria = categoria
        else:
            self.categoria = 'Categoria inválida.'

    def add_observacoes(self, observacoes):
        self.observacoes = observacoes

def main():
    pessoa1 = Cnh('Alice', '12/04/2033', 'H', 51551515151, 'Uso de lentes corretivas.')
    print(pessoa1)
    print()
    pessoa1.add_validade('12/04/2034')
    print(pessoa1)
    print()
    pessoa1.add_categoria('B')
    print(pessoa1)

if __name__ == '__main__':
    main()