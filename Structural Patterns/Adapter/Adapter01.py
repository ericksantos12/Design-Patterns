# Interface do Cliente
class ITarget:
    def request(self):
        pass

    


class Client:
    def __init__(self, target):
        self.target = target
    

    def makeRequest(self):
        print("Fazendo uma requisição")
        self.target.request()

class Adaptee:
    def specificRequest(self):
        print("Requisição especifica do Adaptee")
    


# Adaptador

class Adapter:
    def __init__(self, Adaptee):
        self.Adaptee = Adaptee
    
    def request(self):
        self.Adaptee.specificRequest()


# Uitlização do Adaptador
adaptee = Adaptee()
adapter = Adapter(adaptee)
client = Client(adapter)

client.makeRequest()