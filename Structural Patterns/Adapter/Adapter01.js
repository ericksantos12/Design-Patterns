// Interface do Cliente
class ITarget{
    request(){

    }
}

class Client{
    constructor(target){
        this.target = target;
    }

    makeRequest(){
        console.log("Fazendo uma requisição");
        this.target.request();
    }
}

class Adaptee {
    specificRequest(){
        console.log("Requisição especifica do Adaptee");
    }
}

// Adaptador

class Adapter{
    constructor(Adaptee){
        this.Adaptee = Adaptee;
    }
    request(){
        this.Adaptee.specificRequest();
    }
}

// Uitlização do Adaptador
const adaptee = new Adaptee();
const adapter = new Adapter(adaptee);
const client = new Client(adapter);

client.makeRequest();