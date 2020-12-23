from itertools import zip_longest

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1.500,00', 'R$2.700,00', 'R$5.000,00']

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrato no valor de {preco}')
