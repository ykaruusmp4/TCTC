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
                print("Janela de Ajuda TCTC - Comandos:")
                print("ajuda -> mostra essa janela")
                print("ler   -> lê os bytes de um arquivo : TEP")
                print("comp  -> inicia a compactação : TEP")
                print("enc   -> inicia a encriptação : TEP")
                print("sair  -> finaliza o terminal interativo")
                continue  # apos o print ele retorna ao estado de leitura doq o usuario digitou

            exec(entrada, namespace)  # realmente executa o codigo

        except KeyboardInterrupt:
            # caso o usuario cancele com um Ctrl C, não acontece de ter um erro feio, nós tratamos isso.
            print("\n\n REPL encerrado pelo usuario.")
            break

        except Exception as erro:  # printa caso o comando não esteja entre nenhuma desses 3 casos
            nome_do_erro = type(erro).__name__  # pega a classe do erro
            print(f"Erro de Comando: [{nome_do_erro}] -> {erro}")
            # removi o traceback.print_exc() pq ele dava todo um diagnostico com a linha e tals, e pra tratamento de erro, é só poluição, é mais util em caso de debug
