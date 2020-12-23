vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]


def filtro(vagas):
    if vagas[1] > 2500:
        return True
    else:
        return False


print(list(filter(filtro, vagas)))
