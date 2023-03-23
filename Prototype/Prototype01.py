import copy

# Classe Pessoa
# Método __str__: Retorna uma representação em string da instância
# Método Clone: Cria uma cópia da instância com os mesmos atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'
    
    def clone(self):
        return copy.copy(self)

# Classe PessoaManager
# Responsável por adicionar pessoas a um dicionário, e retornar o clone dessas instâncias
class PessoaManager:
    def __init__(self):
        self.pessoas = {}
        
    def add_pessoa(self, nome, idade, id):
        pessoa = Pessoa(nome, idade)
        self.pessoas[id] = pessoa
        
    def get_pessoa(self, id):
        return self.pessoas[id].clone() # Usa o método clone da classe Pessoa
  
def menu():
    return int(input('''
Sistema de Cadastro:
1 -- Cadastrar pessoa
2 -- Listar pessoa
0 -- Sair
> '''))
  
def main():
    manager = PessoaManager()
    
    while True:
        key = menu()
        match key:
            case 1:
                manager.add_pessoa(input('Nome: '), input('Idade: '), input('Id: '))
                input('Pressione qualquer tecla para continuar...')

            case 2:
                print(manager.get_pessoa(input('Id: ')))
                input('Pressione qualquer tecla para continuar...')

            case 0:
                print('Saindo...')
                break
            
            case _:
                print('Opção inválida')
                input('Pressione qualquer tecla para continuar...')

            
                
        

if __name__ == '__main__':
    main()
#     manager = PessoaManager()
#     manager.add_pessoa('João', 20, 1)
#     manager.add_pessoa('Maria', 25, 2)
    
#     pessoaClonada1 = manager.get_pessoa(1)
#     pessoaClonada2 = manager.get_pessoa(2)
    
#     print(manager.get_pessoa(1))
#     print(manager.get_pessoa(2))
    
#     print(pessoaClonada1)
#     print(pessoaClonada2)