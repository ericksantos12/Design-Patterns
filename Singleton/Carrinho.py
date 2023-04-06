class Carrinho:

    __instance = None

    def __init__(self):
        if Carrinho.__instance is None:
            Carrinho.__instance = self
            self.items = []
        else:
            raise Exception("Esta classe é um singleton")
    
    @staticmethod
    def get_instance():
        if not Carrinho.__instance:
            Carrinho()
        return Carrinho.__instance

    def add_item(self, item):
        self.items.append(item)

    def get_item(self):
        return self.items


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


if __name__ == '__main__':
    # Instanciando carrinho
    carrinho1 = Carrinho.get_instance()

    # Instanciando produtos
    produto1 = Produto("Banana", 4.00)
    produto2 = Produto("Maça", 7.99)
    produto3 = Produto("Melao", 3.89)
    produto4 = Produto("Repolho", 3.79)
    produto5 = Produto("Agua", 2.00)
    produto6 = Produto("Melancia", 1.99)

    # Adicionando no carrinho
    carrinho1.add_item(produto1)
    carrinho1.add_item(produto1)
    carrinho1.add_item(produto3)
    carrinho1.add_item(produto6)
    carrinho1.add_item(produto1)

    # Mostra na tela
    valorTotal = 0

    print("---------- Carrinho ----------")
    for item in carrinho1.get_item():
        print(f"{item.nome} - {item.preco}")
        valorTotal += item.preco

    print(f"{len(carrinho1.get_item())} items no carrinho")
    print(f"TOTAL: {round(valorTotal, 2)}")