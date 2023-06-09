from abc import ABC, abstractmethod

# Interface abstrata par produtos A e B:
class AbstractProductA(ABC):
    
    @abstractmethod
    def operation_a(self) -> str:
        pass
    
class AbstractProductB(ABC):
    
    @abstractmethod
    def operation_b(self) -> str:
        pass
    
# Classes concretas de produtos A1 e A2
class ConcreteProductA1(AbstractProductA):
    
    def operation_a(self) -> str:
        return "Result of ConcreteProductA1"
    
class ConcreteProductA2(AbstractProductA):
    
    def operation_a(self) -> str:
        return "Result of ConcreteProductA2"
    
# Classes concretas de produtos B1 e B2
class ConcreteProductB1(AbstractProductB):
    
    def operation_b(self) -> str:
        return "Result of ConcreteProductB1"
    
class ConcreteProductB2(AbstractProductB):
    
    def operation_b(self) -> str:
        return "Result of ConcreteProductB2"
    
# Interface abstrata:
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Classe concreta das fabricas abstratas
class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

###############
# CLiente

class Client:
    def __init__(self, factory: AbstractFactory) -> None:
        self.product_a = factory.create_product_a()
        self.product_b = factory.create_product_b()
        
    def run(self) -> None:
        print(self.product_a.operation_a())
        print(self.product_b.operation_b())
        

if __name__ == "__main__":
    client1 = Client(ConcreteFactory1())
    client1.run()

    client2 = Client(ConcreteFactory2())
    client2.run()
