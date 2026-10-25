# $ YkaruusMP4 - Comandos $ #
import hashlib

from versoes import versoes


def versao_total():
    maiores = ".".join(v.split(".")[0] for v in versoes.values())
    resto = ".".join(v.split(".", 1)[1] for v in versoes.values())
    hash_estetico = hashlib.sha256(resto.encode()).hexdigest()[:8]
    return f"{maiores}+{hash_estetico}"


def cmd_sair(args):
    return "sair"


def cmd_ajuda(args):
    print("Janela de Ajuda TCTC - Comandos:")
    print("ajuda  -> mostra essa janela")
    print("versao -> mostra as versões")
    print("ler    -> lê os bytes de um arquivo : TEP")
    print("comp   -> inicia a compactação : TEP")
    print("enc    -> inicia a encriptação : TEP")
    print("sair   -> finaliza o terminal interativo")


def cmd_versao(args):
    print(f"TCTC v{versao_total()}")
    for modulo, v in versoes.items():
        print(f"  {modulo:<12} {v}")


def cmd_ler(args):
    print("TEP - Trabalho em Progresso!")


def cmd_comp(args):
    print("TEP - Trabalho em Progresso!")


def cmd_enc(args):
    print("TEP - Trabalho em Progresso!")


COMANDOS = {
    "sair": cmd_sair,
    "ajuda": cmd_ajuda,
    "versao": cmd_versao,
    "ler": cmd_ler,
    "comp": cmd_comp,
    "enc": cmd_enc,
}
