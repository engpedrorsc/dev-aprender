frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        promocao = ' EM PROMOÇÃO'
    else:
        promocao = ''

    print(f'{fruta}{promocao}')
