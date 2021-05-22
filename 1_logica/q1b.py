def arrumar_palavras(file_path):
    """ Corrige emails invertidos ou retorna erro caso dominio esteja errado

        :param - file_path (str): caminho do arquivo txt contendo a lista de emails errados

        :return - email corrigido ou mensagem de erro
    """

    emails = open(file_path, "r")
    qte_emails = emails.readline()

    for email in emails:
        
        email = email.strip()
        metade  = len(email) // 2

        email_corrigido = email[metade-1::-1] + email[:metade-1:-1]

        if(email_corrigido.split("@")[1] == "usp.br"):
            print(email_corrigido)
        else:
            print("ERRO")
