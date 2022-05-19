#
# Exemplos de como trabalhar com arquivos
#
import os
import shutil
from zipfile import ZipFile


def cria_zip_modo1():
    shutil.make_archive("arquivo_compactado", "zip",
                        "C:\\Users\\Feltrim\\OneDrive\\Documentos\\GitHub\\CursoPython-LinkedInLearning\\arquivos_de_exercicios_descubra_o_python\\Cap. 03")


cria_zip_modo1()


def cria_zip_modo2():
    with ZipFile("arquivo_zip_modo2.zip", "w") as novoZip:
        novoZip.write("arquivo_alterado.txt")
        novoZip.write("novo_arquivo.txt")
        novoZip.write("arquivo_compactado.zip")


cria_zip_modo2()


def deleta_arquivo():
    os.remove("arquivo_zip_modo2.zip")


deleta_arquivo()
