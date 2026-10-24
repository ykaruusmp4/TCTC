#começando o arquivi de leitura
from pathlib import Path


def ler_arquivo(caminho):
    caminho = Path(caminho)

    if not caminho.exists():
        print("Arquivo não encontrado.")
        return None

    if not caminho.is_file():
        print("O caminho informado não é um arquivo.")
        return None

    if caminho.suffix == "":
        print("O arquivo não possui extensão.")
        return None

    with open(caminho, "rb") as arquivo:
        dados = arquivo.read()

    return dados