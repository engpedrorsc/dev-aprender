from datetime import datetime as dt


def estampa_tempo(funcao):
    def monitor():
        print(dt.now())
        funcao()
        print(dt.now())
    return monitor


@estampa_tempo
def funcao():
    print('Função')


funcao()
