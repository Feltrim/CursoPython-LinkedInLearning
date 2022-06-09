#
# Exemplo de acesso a uma base de dados SQLite
#

import sqlite3


def manipula_dados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()


def seleciona_dados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)


def manipulacao_dados():
    comandoInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado Teste', 'XX', 'Teste Inclusão')"
    pathBD = "BancoDeDados.db"
    comandoSELECT = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    manipula_dados(pathBD, comandoInsert)
    seleciona_dados(pathBD, comandoSELECT)


manipulacao_dados()
