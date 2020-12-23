def gerar_nome_completo(nome, sobrenome):
    print(f'Seja bem-vindo, {nome} {sobrenome}!')


def calcular_valores(preco, quantidade=1):
    print(f'O valor total é de {preco * quantidade}')


gerar_nome_completo('Pedro', 'Costa')

calcular_valores(20, 2)
