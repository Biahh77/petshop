#Biana Andrade, Julia Rodrigues e Susana Nort.

class Animal:
    def __init__(self, nome, idade, especie):
        self._nome = nome
        self._idade = idade
        self._especie = especie

    def calcular_preco_servico(self):
        pass

class Cachorro(Animal):
    def calcular_preco_servico(self):
        return 50

class Gato(Animal):
    def calcular_preco_servico(self):
        return 40

class Passaro(Animal):
    def calcular_preco_servico(self):
        return 30

class PetShop:
    def __init__(self):
        self.animais = []

    def cadastrar_animal(self, nome, idade, especie):
        if especie.lower() == "cachorro":
            animal = Cachorro(nome, idade, especie)
        elif especie.lower() == "gato":
            animal = Gato(nome, idade, especie)
        elif especie.lower() == "passaro":
            animal = Passaro(nome, idade, especie)
        else:
            print("Apenas cachorros, gatos ou pássaros são aceitos.")
            return
        self.animais.append(animal)
        print(f"{nome} cadastrado com sucesso.")

    def consultar_animal(self, nome):
        for animal in self.animais:
            if animal._nome == nome:
                print(f"Nome: {animal._nome}, Idade: {animal._idade}, Espécie: {animal._especie}")
                return
        print("Não encontrado.")

    def calcular_preco_servico(self, nome):
        for animal in self.animais:
            if animal._nome == nome:
                preco = animal.calcular_preco_servico()
                print(f"O preço do serviço para {animal._nome} é R${preco:.2f}.")
                return
        print("Não encontrado.")

def menu():
    petshop = PetShop()
    while True:
        print("\nMenu:")
        print("1. Cadastrar animal")
        print("2. Consultar animal")
        print("3. Calcular preço de serviço")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do animal: ")
            idade = input("Idade do animal: ")
            especie = input("Espécie do animal (cachorro, gato, pássaro): ")
            petshop.cadastrar_animal(nome, idade, especie)
        elif opcao == "2":
            nome = input("Nome do animal: ")
            petshop.consultar_animal(nome)
        elif opcao == "3":
            nome = input("Nome do animal: ")
            petshop.calcular_preco_servico(nome)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Inválido. Tente novamente.")

if __name__ == "__main__":
    menu()