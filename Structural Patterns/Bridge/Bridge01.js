// Interface de Cores
class Color {
    constructor(color){
        this.color = color;
    }
    getColor(){
        return this.color;
    }
}

// Implementação Cores
class RedColor extends Color{
    constructor(){
        super("vermelho");
    }
}
class GreenColor extends Color{
    constructor(){
        super("verde");
    }
}
class BlueColor extends Color{
    constructor(){
        super("azul");
    }
}
class WhiteColor extends Color{
    constructor(){
        super("branco");
    }
}

// Implementação Forma
class Shape{
    constructor(color){
        this.color = color;
    }

    setColor(color){
        this.color = color;
    }

    draw(){
        throw new Error("Este método precisa ser implementado pela subclasse")
    }
}

// Abstrações Refinadas
class CircleShape extends Shape{
    draw(){
        console.log(`Desenhando um circulo ${this.color.getColor()}.`);
    }
}
class SquareShape extends Shape{
    draw(){
        console.log(`Desenhando um quadrado ${this.color.getColor()}.`);
    }
}
class TriangleShape extends Shape{
    draw(){
        console.log(`Desenhando um triangulo ${this.color.getColor()}.`);
    }
}

// CLiente

const red = new RedColor();
const green = new GreenColor();
const blue = new BlueColor();
const white = new WhiteColor();

const circle = new CircleShape(green);
const square = new SquareShape(red);
const triangle = new TriangleShape(white);

circle.draw()
square.draw()
triangle.draw()