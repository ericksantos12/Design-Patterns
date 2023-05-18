from abc import ABC, abstractmethod

# Interface de Cores

class Color(ABC):
    
    @abstractmethod
    def getColor(self):
        pass
    


# Implementação Cores
class RedColor (Color):
    def getColor(self):
        return "vermelho"
    

class GreenColor (Color):
    def getColor(self):
        return "verde"
    

class BlueColor (Color):
    def getColor(self):
        return "azul"
    

class WhiteColor (Color):
    def getColor(self):
        return "branco"
    


# Implementação Forma
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    

    def setColor(self, color):
        self.color = color
    
    @abstractmethod
    def draw(self):
        pass
    


# Abstrações Refinadas
class CircleShape (Shape):
    def draw(self):
        print(f'Desenhando um circulo {self.color.getColor()}.')
    

class SquareShape (Shape):
    def draw(self):
        print(f'Desenhando um quadrado {self.color.getColor()}.')
    

class TriangleShape (Shape):
    def draw(self):
        print(f'Desenhando um triangulo {self.color.getColor()}.')
    


# CLiente

red = RedColor()
green = GreenColor()
blue = BlueColor()
white = WhiteColor()

circle = CircleShape(green)
square = SquareShape(red)
triangle = TriangleShape(white)

circle.draw()
square.draw()
triangle.draw()