# 🏭 Abstract Factory

<div align=center>
    <img src="https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-en.png" width=500>
</div>

## 🧐 Sobre
O padrão de projeto Abstract Factory é usado quando precisamos criar famílias de objetos relacionados sem conhecer todos os detalhes da sua criação. Ele fornece uma interface para criar objetos de várias classes relacionadas sem especificar suas classes concretas. Isso é útil quando queremos criar objetos relacionados que sejam compatíveis entre si. Para implementar este padrão, é preciso criar uma interface ou classe abstrata que defina a fábrica e suas operações de criação, e então criar classes concretas que implementem essas operações para criar objetos específicos.

## 👩‍💻 Exemplo em YAML

```yaml
VeiculoFactory:
  - criar_veiculo: ~

LuxoFactory:
  herda_de: VeiculoFactory
  - criar_veiculo:
      tipo: ~
      marca: ~
      modelo: ~

EconomicoFactory:
  herda_de: VeiculoFactory
  - criar_veiculo:
      tipo: ~
      marca: ~
      modelo: ~

FabricaDeVeiculos:
  - produzir_veiculo:
      factory: VeiculoFactory
      tipo: ~
```

Neste exemplo, a classe abstrata `VeiculoFactory` possui apenas um método chamado `criar_veiculo`. As classes concretas `LuxoFactory` e `EconomicoFactory` herdam de `VeiculoFactory` e implementam o método `criar_veiculo`.

A classe `FabricaDeVeiculos` possui um método chamado `produzir_veiculo`, que recebe a `factory` e o `tipo` de veículo a ser produzido. O método usa a implementação concreta da `VeiculoFactory` para criar o veículo.

## 📂 Exemplos
- [AbstractFactory01.py](./AbstractFactory01.py)
- [AbstractFactory02.js](./AbstractFactory02.js)