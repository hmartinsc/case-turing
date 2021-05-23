class Estacionamento():
    """ Classe que representa o estacionamento Nelnelson, baseada na estrutura de pilha """

    def __init__(self):
        self.carros = []

    def vazio(self):
        return self.carros == []

    def entra_carro(self, item):
        self.carros.append(item)

    def sai_carro(self):
        return self.carros.pop()

    def tamanho(self):
        return len(self.carros)


def verificar_estacionamento(file_path):
    """ Verifica se existe algum problema nas entradas e saidas de carros no estacionamento Nelnelson

        :param - file_path (str): caminho do arquivo txt contendo as entradas e saidas dos carros

        :return - printa sim, caso esteja tudo certo; ou nao, caso haja algum problema
    """

    carros = open(file_path, "r")

    num_vagas = int(carros.readline().split(" ")[0])
    estacionamento = Estacionamento()
    tudo_certo = True

    for carro in carros:
        carro = int(carro)

        if carro > 0:

            if (estacionamento.tamanho() == num_vagas):
                tudo_certo = False
                break

            estacionamento.entra_carro(carro)
            
        else:

            proximo_carro = estacionamento.sai_carro()
            
            if(proximo_carro != -carro):
                tudo_certo = False
                break

    if (tudo_certo and estacionamento.vazio()):
        print("sim")
    else:
        print("nao")
