class Pet:
    def __init__(self, tipo, nome, idade, peso, raca, cor, castrado=False):
        self.__tipo = tipo
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__castrado = castrado


class Pessoa:
    def __init__(self, cpf, nome, endereço):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereço = endereço
        self.__meus_pets = []

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    def cadastrar_pet(self, pet):
        pass

    def excluir_pet(self, nome):
        pass

    def mostrar_meus_pets(self):
        pass
