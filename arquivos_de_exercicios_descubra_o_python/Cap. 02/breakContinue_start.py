#
# Exemplo de como usar os comando Break e Continue
#

def loop_break():
    for x in range(5, 10):
        if x == 7:
            break
        print("O valor de x é: ", x)


loop_break()


def loop_continue():
    for x in range(5, 10):
        if x == 7:
            continue
        print("O valor de x é: ", x)


loop_continue()
