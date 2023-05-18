const Carrinho = (function() {
    let instance;

    function createInstance() {
        let produtos = [];
        
        function addProduto(produto){
            produtos.push(produto);
        }

        function getProduto() {
            return produtos;
        }

        function clearCarrinho(){
            produtos = [];
        }

        return {
            addProduto, getProduto, clearCarrinho
        }
    }

    return {
        getInstance: () => {
            if(!instance){
                instance = createInstance();
            }
            return instance;
        }
    }
})()

const carrinho = Carrinho.getInstance();

carrinho.addProduto({nome: "Produto 1", preco: 10})
carrinho.addProduto({nome: "Produto 2", preco: 20})
carrinho.addProduto({nome: "Produto 3", preco: 30})
carrinho.addProduto({nome: "Produto 4", preco: 40})

console.log(carrinho.getProduto());

carrinho.clearCarrinho();

console.log(carrinho.getProduto());

carrinho.addProduto({nome: "Produto 5", preco: 15})
carrinho.addProduto({nome: "Produto 6", preco: 25})
carrinho.addProduto({nome: "Produto 7", preco: 35})
carrinho.addProduto({nome: "Produto 8", preco: 45})
console.log(carrinho.getProduto());