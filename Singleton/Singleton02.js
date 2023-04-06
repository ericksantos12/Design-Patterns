class Singleton{

    constructor(){
        if(!Singleton.instance){
            Singleton.instance = this;
            this.value = 0;
        }
        return Singleton.instance;
    }

    increment(){
        this.value += 1;
        console.log(`Value: ${this.value}`);
    }
}


const s1 = new Singleton()
const s2 = new Singleton()

console.log(s1 === s2);

s1.increment()
s2.increment()
s1.increment()
s2.increment()