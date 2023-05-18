// Folha
class Componente{
    constructor(nome){
        this.nome = nome;
    }

    adicionar(){}

    remover(){}

    obterNome(){}
}

class Folha extends Componente{
    constructor(nome, preco){
        super(nome);
        this.preco = preco;
    }

    obterNome(){
        return this.nome;
    }
    obterPreco(){
        return this.preco;
    }
}

// Container
class Container extends Componente{
    constructor(nome){
        super(nome);
        this.componentes = []
    }

    adicionar(componente){
        this.componentes.push(componente)
    }

    remover(componente){
        const index = this.componentes.indexOf(componente);
        this.componentes.splice(index, 1);
    }

    obterNome(){
        return this.nome;
    }

    obterPreco(){
        let preco = 0;
        this.componentes.forEach(componente => {
            preco += componente.obterPreco();
        })
        return preco;
    }
}


// Cliente
const uva = new Folha("Uva", 2.50);
const melancia = new Folha("Melancia", 3.50);
const jaca = new Folha("Jaca", 5.99);
const laranja = new Folha("Laranja", 2.00);

const frutas = new Container('Pedido 14167');
frutas.adicionar(melancia);
frutas.adicionar(uva);
frutas.adicionar(jaca);
frutas.adicionar(melancia);
frutas.adicionar(laranja);

const caixa = new Container("Caixa do Pedido");
caixa.adicionar(frutas)
caixa.adicionar(new Folha("Embalagem", 1.00))

console.log(`Preco Total: R$${caixa.obterPreco()}`);