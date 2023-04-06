# 🤖 Prototype

<div align=center>
    <img src="https://refactoring.guru/images/patterns/content/prototype/prototype.png" width=500>
</div>

## 🧐 Sobre

O padrão de projeto Prototype é usado quando precisamos criar objetos sem conhecer todos os detalhes da sua criação. Ele permite a criação de novos objetos através da clonagem de um objeto existente, evitando a necessidade de criar um novo objeto do zero. Isso é útil quando queremos criar objetos com características semelhantes, mas que diferem em alguns detalhes. Para implementar este padrão, a classe deve implementar a interface Cloneable e sobrescrever o método clone() para criar uma cópia do objeto.

## 📂 Exemplos
- [Prototype01.py](./Prototype/)
