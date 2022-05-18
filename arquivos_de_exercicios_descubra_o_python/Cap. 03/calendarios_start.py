#
# Arquivo com exemplos de uso de calendários
#

import calendar

# criando um calendário no formato texto
def calendario_texto():
    calendario_texto = calendar.TextCalendar(calendar.SUNDAY)
    txt_calendario = calendario_texto.formatmonth(2022, 5)
    print(txt_calendario)

# calendario_texto()
# Criando um calendário no formato HTML

def calendario_html():
    calendario_html = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendario = calendario_html.formatmonth(2022, 5)
    print(html_calendario)

calendario_html()


# loop ao longo dos dias de um mês
