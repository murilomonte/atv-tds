# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# =====MENU========
# 1) Cadastar nome
# 2) Pesquisar nome
# 3) Listar todos os nome
# 4) Alterar
# 5) Excluir
# 0) Sair do programa
# ——————–
# Digite sua escolha:_


# Create -> Cadastrar
# Read   -> Pesquisar, Listar
# Update -> Alterar
# Delete -> Excluir


class NameManagement:
    def __init__(self, length: int) -> None:
        self.__max_length: int = length
        self.__names: list[str] = []

    def add_name(self, name: str) -> str:
        if len(self.__names) < self.__max_length:
            if name not in self.__names:
                self.__names.append(name)
                return "Nome adicionado"
            else:
                return "O nome já está na lista"
        else:
            return f"Só são permitidos {self.__max_length}"

    def search_name(self, name: str) -> int:
        if name in self.__names:
            for index, item in enumerate(self.__names):
                if item == name:
                    return index
        raise ValueError("Nome não encontrado.")

    def show_names(self) -> list[str]:
        return self.__names

    def update_name(self, name: str, new_name: str) -> str:
        if name in self.__names:
            name_index = self.search_name(name=name)
            self.__names[name_index] = new_name
            return f"Nome {name} alterado para: {new_name}"
        else:
            return "Nome não encontrado"

    def delete_name(self, name: str) -> str:
        if name in self.__names:
            name_index = self.search_name(name=name)
            self.__names[name_index] = ""
            self.__names.remove(name)
            return f"Nome {name} removido."
        else:
            return "Nome não encontrado"


def main() -> None:
    while True:
        try:
            length: int = int(input("Insira o tamanho máximo da lista: "))
            break
        except ValueError:
            print("Valor inválido.")

    nameManagement: NameManagement = NameManagement(length=length)
    print(
        """
\n========MENU========
1) Cadastar nomes
2) Pesquisar nomes
3) Listar todos os nomes
4) Alterar um nome
5) Excluir um nome
0) Sair do programa
——————–——————–——————–
            """
    )
    while True:
        try:  # teste - ok
            userInput: int = int(input("Digite sua escolha: "))
            if userInput == 1:  # teste - ok
                name: str = str(input("Qual nome deseja adicionar?: "))
                print(nameManagement.add_name(name=name))

            elif userInput == 2:  # teste - ok
                name: str = str(input("Qual nome deseja pesquisar?: "))
                try:
                    print(
                        f"O nome: {name} foi encontrado no índice: {nameManagement.search_name(name=name)}"
                    )
                except ValueError:
                    print("Nome não encontrado.")

            elif userInput == 3:  # teste - ok
                print(f"## Todos os nomes:", nameManagement.show_names())

            elif userInput == 4:  # teste - ok
                name: str = str(input("Qual nome deseja substituir?: "))
                new_name: str = str(input("Qual o novo nome?: "))
                print(nameManagement.update_name(name=name, new_name=new_name))

            elif userInput == 5:  # teste - ok
                name: str = str(input("Qual nome deseja deletar?: "))
                print(nameManagement.delete_name(name=name))

            elif userInput == 0:  # teste - ok
                break

        except ValueError:
            print("\nValor inválido.")


if __name__ == "__main__":
    main()
