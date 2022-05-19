#
# Arquivo com exemplos de como trabalhar com paths
#

from os import path
import time


def dados_arquivo():
    arquivo_existe = path.exists("novo_arquivo.txt")
    e_diretorio = path.isdir("novo_arquivo.txt")
    path_arquivo = path.realpath("novo_arquivo.txt")
    path_relativo = path.relpath("novo_arquivo.txt")
    data_criacao = time.ctime(path.getctime("novo_arquivo.txt"))
    data_modificacao = time.ctime(path.getmtime("novo_arquivo.txt"))

    print(arquivo_existe)
    print(e_diretorio)
    print(path_arquivo)
    print(path_relativo)
    print(data_criacao)
    print(data_modificacao)


dados_arquivo()
