class Stack:
    """ Classe que representa uma fila """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def verificar_estacionamento(file_path):
    """ Verifica se as entradas e saidas de carros no estacionamento do Nelnelson sao possiveis
    """

    carros = open(file_path, "r")

    num_vagas = int(carros.readline().split(" ")[0])
    estacionamento = Stack()
    tudo_certo = True

    for carro in carros:
        carro = int(carro)

        if carro > 0:

            if (estacionamento.size() == num_vagas):
                tudo_certo = False
                break

            estacionamento.push(carro)
            
        else:

            proximo_carro = estacionamento.pop()
            
            if(proximo_carro != -carro):
                tudo_certo = False
                break

    if (tudo_certo and estacionamento.isEmpty()):
        print("sim")
    else:
        print("nao")

verificar_estacionamento("estacionamento3.txt")