# 🌳 Composite

<div align=center>
    <img src="https://refactoring.guru/images/patterns/content/composite/composite.png" width=500>
</div>

## 🧐 Sobre
O padrão de projeto Composite é como uma árvore em que um objeto pode conter outros objetos, formando uma estrutura hierárquica. É como ter uma pasta em um computador que pode conter arquivos e outras pastas dentro dela. O objeto composto é chamado de "nó" e os objetos contidos são chamados de "folhas". Isso permite tratar tanto os objetos individuais quanto as estruturas complexas de forma uniforme, já que todos seguem uma interface comum. Por exemplo, é possível chamar um método em um nó pai que percorrerá recursivamente todos os seus filhos, realizando uma operação em cada um. O padrão Composite é útil quando se precisa representar uma hierarquia de objetos de forma simples e genérica, permitindo a composição de estruturas complexas de forma flexível e transparente.


## 📂 Exemplos
- [Composite.js](Composite.js)