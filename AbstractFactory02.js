// Interface de Fabrica ABSTRATA
class AnimalFactory{
    createAnimal(){
        throw new Error("Method not implemented.");
    }
}

// Fabrica CONCRETA
class DogFactory extends AnimalFactory{
    createAnimal(){
        return new Dog();
    }
}

class CatFactory extends AnimalFactory{
    createAnimal(){
        return new Cat();
    }
}

// Interface de Produto ABSTRATO
class Animal{
    makeSound(){
        throw new Error("Method not implemented.");
    }
}

// Produto CONCRETO
class Dog extends Animal{
    makeSound(){
        return "Woof!";
    }
}

class Cat extends Animal{
    makeSound(){
        return "Meow!";
    }
}

const dogFactory = new DogFactory();
const catFactory = new CatFactory();

const dog = dogFactory.createAnimal();
const cat = catFactory.createAnimal();

console.log(dog.makeSound());
console.log(cat.makeSound());