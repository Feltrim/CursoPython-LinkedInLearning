#
#  Arquivo com exemplos de como formatar uma data
#

from datetime import datetime


# Datas e horas podem ser formatados usando um conjunto de strings predefinidas
def formata_data_hora():
    hoje = datetime.now()
#### Date Formatting ####

# %y/%Y - Ano, %a/%A - Dia da semana, %b/%B - Mês, %d - dia do mês
    print(hoje.strftime('O ano é: %Y'))
#% c - data e hora da localidade,% x - data da localidade,% X - hora da localidade
    print(hoje.strftime('Data e hora local: %c'))

#### Time Formatting ####
# %I/%H - 12/24 horas, %M - minuto, %S - segundo, %p -  AM/PM
    print(hoje.strftime('A hora atual é: %H:%M:%S'))


formata_data_hora()
