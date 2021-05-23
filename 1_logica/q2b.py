def instante_estacionamento(file_path):
    """ Informa a configuracao do estacionamento em um dado instante

        :param - file_path (str): caminho do arquivo txt contendo informacoes sobre as entradas e saidas dos carros

        :return - printa a configuracao do estacionamento no instante de interesse
    """

    arquivo = open(file_path, "r")

    cabecalho = arquivo.readline().split(" ")
    total_vagas = int(cabecalho[0])
    total_carros = int(cabecalho[1])
    carros = []

    for n in range(0, total_carros):
        carros.append(int(arquivo.readline()))

    instante_de_interesse = int(arquivo.readline())
    instante_limite = instante_de_interesse - total_vagas
    
    for instante_atual in range(instante_de_interesse, instante_limite, -1):
        
        try:
            carro_n = carros.index(instante_atual) + 1
        except:
            carro_n = 0

        if instante_atual == instante_limite + 1:
            print(carro_n)
        else:
            print(carro_n, end=" ")
