def economiza_letras(file_path):
    """ Conta quantos caracteres sao economizados suprimindo caracteres repetidos em linhas consecutivas

        :param - file_path (str): caminho do arquivo txt contendo a lista de emails

        :return - numero de caracteres economizados
    """

    emails = open(file_path, "r")
    qte_emails = emails.readline()

    caracteres_economizados = 0
    linha_superior = emails.readline()

    for linha_inferior in emails:
        
        i = 0

        while(linha_inferior[i] == linha_superior[i]):
            caracteres_economizados += 1
            i += 1
        
        linha_superior = linha_inferior

    print(caracteres_economizados)
