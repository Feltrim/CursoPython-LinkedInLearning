#
# Arquivo com exemplos de Loops
#

# Definindo um LOOP FOR
def loop_for():
    for x in range(5, 10):
        print(x)


loop_for()

# Usando um LOOP FOR em uma coleção


def loop_array():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for d in dias:
        print(d)


loop_array()


# Usando BREAK e CONTINUE


# Usando a função enumerate, paara buscar valoeres e seus índices
def loop_enum():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i, d in enumerate(dias):
        print(i, d)


loop_enum()
