# 🥺 Singleton

<div align=center>
    <img src="https://refactoring.guru/images/patterns/content/singleton/singleton.png" width=500>
</div>

## 🧐 Sobre

O padrão Singleton é um padrão de projeto que garante que uma classe só possa ter uma única instância durante a execução de um programa. Isso é útil quando precisamos ter apenas uma única instância de uma classe em todo o código. Para implementar este padrão, a classe deve ter um construtor privado que impeça a criação de novas instâncias externamente e um método estático para retornar a única instância da classe.

## 👩‍💻 Exemplo em YAML

```yaml
Singleton:
  description: Singleton pattern ensures a class has only one instance and provides a global point of access to it.
  instance: 
    created: false
    object: null
  methods:
    getInstance:
      description: If an instance of the class exists, return it. Else, create a new instance and return it.
      pseudocode: |
        if not instance.created:
          instance.object = new SingletonClass()
          instance.created = true
        return instance.object

```

## 📂 Exemplos
- [Singleton01.py](./Singleton01.py)
- [Singleton02.js](./Singleton02.js)
- [Carrinho.py](./Carrinho.py)
- [Carrinho.js](./Carrinho.js)