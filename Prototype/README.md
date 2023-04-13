# 🤖 Prototype

<div align=center>
    <img src="https://refactoring.guru/images/patterns/content/prototype/prototype.png" width=500>
</div>

## 🧐 Sobre

O padrão de projeto Prototype é usado quando precisamos criar objetos sem conhecer todos os detalhes da sua criação. Ele permite a criação de novos objetos através da clonagem de um objeto existente, evitando a necessidade de criar um novo objeto do zero. Isso é útil quando queremos criar objetos com características semelhantes, mas que diferem em alguns detalhes. Para implementar este padrão, a classe deve implementar a interface Cloneable e sobrescrever o método clone() para criar uma cópia do objeto.

## 👩‍💻 Exemplo em YAML

```yaml
Prototype:
  - clonar: ~

Carro:
  herda_de: Prototype
  - marca: ~
  - modelo: ~
  - ano: ~
  - cor: ~
  - clonar: ~

Frota:
  - carros: []
  - adicionar_carro:
      carro: Prototype
  - criar_novo_carro:
      modelo: ~
```

Neste exemplo, temos a classe abstrata `Prototype`, que define um método chamado `clonar`. A classe concreta `Carro` herda de `Prototype` e implementa o método `clonar`.

A classe Frota possui uma lista de carros e dois métodos: `adicionar_carro`, que adiciona um carro à lista, e `criar_novo_carro`, que cria um novo carro a partir de um carro existente na lista, utilizando o método `clonar`.

## 📂 Exemplos
- [Prototype01.py](./Prototype01.py)
