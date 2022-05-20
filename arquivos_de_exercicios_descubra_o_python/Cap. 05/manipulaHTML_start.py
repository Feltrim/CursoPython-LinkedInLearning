#
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser


class MeuParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada.")
        if attrs.__len__() > 0:
            for a in attrs:
                print(f"  Valores encontrados: {a[0]} = {a[1]}")

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada.")

    def handle_comment(self, data):
        print("Comentário encontrado.")

    def handle_data(self, data):
        print("Valores encontrados.")
        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print(f"O valor encontrado é {data}")


def meu_objeto():
    meu_parser1 = MeuParser()
    arquivo = open("C:\\Users\\Feltrim\\OneDrive\\Documentos\\GitHub\\CursoPython-LinkedInLearning\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemplohtml.html")
    dados = arquivo.read()
    meu_parser1.feed(dados)


meu_objeto()
