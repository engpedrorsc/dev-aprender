from datetime import datetime
import random

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
nascimento = datetime.strptime(
    input('Digite a sua data de nascimento (dd/mm/aaaa): '), '%d/%m/%Y')
data_cadastro = datetime.now()

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes)

str_data_cadastro = data_cadastro.strftime('%d/%m/%Y')

print(f'Olá {nome}, o seu registro foi conluído com sucesso no dia {str_data_cadastro}.')
print(
    f'Parabéns, houve um sorteio e você ganhou um cartão de comrpas no valor de {sorteio}!')
