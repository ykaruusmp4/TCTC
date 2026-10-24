import traceback


def repl():  # define o que é o repl - ou seja, toda a interatividade pelo terminal.
    print("TCTC - ferramenta de compressão e encriptação.")
    print("linha de comando interativa.")

    namespace = {}  # é tipo um dicionario que faz com que as variaveis não se percam entre as execuções

    while True:
        try:
            entrada = input("> ")  # lê o que o usario digitou e armazena

            if entrada.strip() == "sair":
                break  # se a entrada, digitada pelo usuario for 'sair' ele finaliza o processo

            if not entrada.strip():
                continue  # se o usuario não tiver digitado nada, ele pede a entrada denovo

            if entrada.strip() == "ajuda":
                print("TEP - Trabalho em Progresso!")
                continue  # apos o print ele retorna ao estado de leitura doq o usuario digitou

            exec(entrada, namespace)  # realmente executa o codigo

        except Exception:  # printa caso o comando não esteja entre nenhuma desses 3 casos
            print("Erro no comando digital")
            traceback.print_exc()
