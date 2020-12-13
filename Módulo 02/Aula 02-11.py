# DESAFIO
# Calcule quantos dias faltam até o seu aniversário

from datetime import datetime

niver = datetime.strptime('10/07/2021', '%d/%m/%Y')
hoje = datetime.now()
tempo = niver - hoje


print(f'Faltam {tempo.days} para o seu aniversário.')
