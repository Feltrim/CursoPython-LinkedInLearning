#
# Exemplo de como criar classes
#

class MinhaClasse():
    def __init__(self):
        self.meuAtributo = "Passou pelo construtor!"

    def meu_metodo(self):
        print("Passou pelo meu método")

    def meu_metodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)


def cria_objeto():
    meuObj = MinhaClasse()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meu_metodo()

    meuObj.meu_metodo2("Executando um método")


cria_objeto()
