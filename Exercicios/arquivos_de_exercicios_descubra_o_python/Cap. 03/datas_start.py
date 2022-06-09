#
# Arquivo com exemplos de manipulação de  datas
#

from datetime import date, time, datetime


def manipula_data_hora():
    hoje = date.today()
    print(f'Hoje é: {hoje}')
    print(f'Partes da data: {hoje.day} {hoje.month} {hoje.year}')
    print(f'Número do dia da semana: {hoje.weekday()}')
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    print(f'Nome abreviado do dia da semana: {dias[hoje.weekday()]}')

    data = datetime.now()
    print(f'Data e hora: {data}')

    tempo = datetime.time(data)
    print(f'Hora atual: {tempo}')


manipula_data_hora()
