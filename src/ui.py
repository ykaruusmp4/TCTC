from comandos import COMANDOS


def repl():
    print("TCTC - ferramenta de compressão e encriptação.")
    print("linha de comando interativa.")

    while True:
        try:
            entrada = input("> ").strip()
            if not entrada:
                continue

            nome, *args = entrada.split()
            comando = COMANDOS.get(nome)

            if comando is None:
                print(f"Comando desconhecido: '{nome}'. Digite 'ajuda'.")
                continue

            if comando(args) == "sair":
                break

        except KeyboardInterrupt:
            print("\n\n REPL encerrado pelo usuario.")
            break

        except Exception as erro:
            print(f"Erro de Comando: [{type(erro).__name__}] -> {erro}")
