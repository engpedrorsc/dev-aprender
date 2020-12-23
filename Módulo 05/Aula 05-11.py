from operator import eq, itemgetter

produtos = [
    {'nome': 'Celular',
     'preco': 1500
     },
    {'nome': 'Monitor',
     'preco': 500
     },
    {'nome': 'Microfone',
     'preco': 300
     }
]

produtos.sort(key=itemgetter('preco'))
print(produtos)


equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200)
]


equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
