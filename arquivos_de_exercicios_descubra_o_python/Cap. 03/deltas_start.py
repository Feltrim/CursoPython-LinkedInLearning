#
# Arquivo de exemplo para uso da classe timedeltas
#

from datetime import datetime, timedelta


def delta_tempo():
    delta = timedelta(days=86, hours=8532, minutes=7645)
    print(delta)

    hoje = datetime.now()
    print(f'Data no futuro: {hoje + delta}')
    print(f'Data no passado: {hoje - delta}')


delta_tempo()
