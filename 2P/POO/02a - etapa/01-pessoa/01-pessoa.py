# Com base na classe Pessoa descrita link abaixo:
# X 1. Altere o código de forma a impedir que uma pessoa "casada"  possa se casar novamente. Exceções: Quando a pessoa se tornar "viúva" ou "divorciada"

# 2. Crie um método: "ter_filhos". Condição para este método ser executado:
# a) Pessoa ser do sexo: "Feminino"
# b) Segunda pessoa ser do sexo: "Masculino" . Ex: maria.ter_filho(joao), nesse caso maria é um objeto do tipo "Pessoa" do sexo: "feminino" e joao é um objeto do tipo "Pessoa" do sexo: "masculino". Esse método tem que retornar um novo objeto do tipo "Pessoa"
# c) acrescentar os atributos: Pai e Mãe (tipo: Pessoa).
# d) Inserir na lista: filhos, todos os objetos gerados.

from random import choice as choice


class Pessoa:
    seq = 0

    def __init__(
        self,
        nome,
        peso,
        altura,
        sexo,
        idade=0,
        estado="vivo",
        est_civil="solteiro",
        conjuge=None,
        mae=None,
        pai=None,
    ):
        Pessoa.seq += 1
        self.__id = Pessoa.seq

        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__mae = mae
        self.__pai = pai
        self.__mae_adotiva = None
        self.__pai_adotivo = None
        self.__conjuge = conjuge
        self.filhos = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def conjuge(self):
        return self.__conjuge

    @property
    def est_civil(self):
        return self.__est_civil

    @nome.setter
    def nome(self, valor):
        if self.__est_civil == "casado":
            nome_antigo = self.__nome.split(" ")
            nome_conjuge = self.__conjuge.nome.split(" ")
            novo_nome = valor.split(" ")
            for i in novo_nome:
                if (i not in nome_antigo) and (i not in nome_conjuge):
                    print("nome inválido!")
                    return
            self.__nome = valor
            print("Alteração efetuada com sucesso!")

    def casar(self, conjuge):
        # verificar se as instancias estão em posições diferentes de memória
        if type(conjuge) != Pessoa:
            print("Só é possível casar-se com pessoas.")
        elif self.id == conjuge.id:
            print("Não é possível casar-se consigo mesmo.")
        elif self.__estado == "falecido" or conjuge.__estado == "falecido":
            print("Não é casar quando um dos dois está falecido.")
        elif (
            self.__est_civil != "casado" or self.__est_civil in ["divorciado", "viuvo"]
        ) and (
            conjuge.__est_civil != "casado"
            or conjuge.__est_civil in ["divorciado", "viuvo"]
        ):
            self.__est_civil = "casado"
            self.__conjuge = conjuge
            self.__conjuge.__est_civil = "casado"
            self.__conjuge.__conjuge = self
            print(f"{self.__nome} casou-se com {conjuge.nome}\n")

    def morrer(self):
        # alterar o estado para "morto"
        if self.__estado != "falecido":
            self.__estado = "falecido"
            # verificar se a pessoa que morreu era casada e alterar o conjuge reséctivo para "viuvo"
            if self.conjuge:
                self.__est_civil = None
                self.conjuge.__est_civil = "viuvo"
                self.conjuge.__conjuge = self.__conjuge = None
            print(f'{self.__nome} morreu.')
        else:
            print(f"{self.nome} já está morto(a).")

    def divorciar(self):
        # mudar o estado civil das pessoas para "divorciado"
        if self.__est_civil != "divorciado":
            self.__est_civil = self.__conjuge.__est_civil = "divorciado"
            self.__conjuge = self.__conjuge.__conjuge = None
            print(f'Divorcio realizado.')
        else:
            print("Não é possível divorciar-se novamente estando divorciado.")
        pass

    def ter_filhos(self, pessoa, nome_crianca):
        if type(pessoa) != Pessoa:
            print("Só é possível ter filhos com pessoas.")

        elif self.id == pessoa.id:
            print("Não é possível ter filhos consigo mesmo.")

        elif self.__estado == "falecido" or pessoa.__estado == "falecido":
            print("Não é possível ter filhos com alguém falecido.")

        elif self.__sexo == pessoa.__sexo:
            print("Não é possível ter filhos com uma pessoa do mesmo sexo.")

        else:
            # Retornar uma nova pessoa
            filho = Pessoa(
                nome=nome_crianca,
                sexo=choice(["F", "M"]),
                idade=0,
                altura=choice([48, 53]),
                peso=choice([2.5, 4]),
                mae=self,
                pai=pessoa,
            )
            # criar o vinculo
            self.filhos.append(filho)
            pessoa.filhos.append(filho)
            print(f'{self.__nome} e {self.__conjuge.__nome} tiveram um filho(a).')

    def adotar_filhos(self, crianca):
        if type(crianca) != Pessoa:
            print("Só é possível adotar pessoas.")

        elif crianca.__mae or crianca.__pai:
            print("Não é possível adotar crianças com um pai ou mãe")

        elif self.id == crianca.id:
            print("Não é possível adotar a si mesmo.")

        elif self.__estado == "falecido" or crianca.__estado == "falecido":
            print("Não é possível realizar uma adoção onde um dos dois está falecido.")

        else:
            self.filhos.append(crianca)
            if self.__sexo == "F":
                crianca.__mae_adotiva = self
                if self.__conjuge:
                    self.__conjuge.filhos.append(crianca)
                    crianca.__pai_adotivo = self.conjuge
            elif self.__sexo == "M":
                crianca.__pai_adotivo = self
                if self.__conjuge:
                    self.__conjuge.filhos.append(crianca)
                    crianca.__mae_adotiva = self.conjuge
            print(f'{self.__nome} e {self.__conjuge.__nome} adotaram uma criança.')

    def __str__(self):
        nomes_filhos = []
        for filho in self.filhos:
            nomes_filhos.append(filho.nome)
        return (
            f"Nome: {self.__nome}\n"
            f"Idade: {self.__idade}\n"
            f"Peso: {self.__peso}kg\n"
            f"Altura: {self.__altura}cm\n"
            f"Sexo: {self.__sexo}\n"
            f"Estado: {self.__estado}\n"
            f"Estado Civil: {self.__est_civil}\n"
            f"Mãe: {self.__mae.nome if (self.__mae) else 'Desconhecida'}\n"
            f"Pai: {self.__pai.nome if (self.__pai) else 'Desconhecido'}\n"
            f"Mãe Adotiva: {self.__mae_adotiva.nome if (self.__mae_adotiva) else 'Nenhuma'}\n"
            f"Pai Adotivo: {self.__pai_adotivo.nome if (self.__pai_adotivo) else 'Nenhum'}\n"
            f"Cônjuge: {self.__conjuge.nome if (self.__conjuge) else 'Nenhum'}\n"
            f"Filhos: {nomes_filhos if (self.filhos) else 'Nenhum'}\n"
        )


####### execução ########

maria = Pessoa(
    nome="Maria",
    idade=30,
    peso=65,
    altura=170,
    sexo="F",
    mae=Pessoa("Francisca", 65, 60, 1.6, "F"),
)  # maria -> solteira

joao = Pessoa(nome="João", idade=25, peso=66, altura=170, sexo="M")  # joão -> solteiro

alice = Pessoa(
    nome="Alice",
    idade=15,
    peso="65",
    altura=170,
    sexo="F",
    estado="vivo",
    est_civil="solteiro",
    conjuge=None,
)

ana = Pessoa(
    nome="Ana",
    idade=31,
    peso=65,
    altura=170,
    sexo="F",
    mae=Pessoa("Francisca", 65, 60, 1.6, "F"),
)

print("# Casando consigo mesma")
maria.casar(maria)
print(maria)

print("# Casando com outra pessoa")
maria.casar(joao)
print(maria)

print("# Falencendo")
maria.morrer()
print(maria)

print("# Tentando casar com um falecido")
joao.casar(maria)

print("# Casando-se novamente")
joao.casar(ana)
print(joao)

print("# Gerando bebês")
ana.ter_filhos(joao, "Ariel")
joao.ter_filhos(ana, "Alex")
print(ana)

print("# Adotando pessoas")
ana.adotar_filhos(alice)
print(ana)
print(alice)
