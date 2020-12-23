from turtle import Turtle

t = Turtle()
t.speed = 1

continua = True
while continua:
    direcao = input(
        'A tartaruga deve rotacionar para a direita(d) ou para a esquerda (e)? ').lower()
    rotacao = int(input('A rotação será de quantos graus? '))

    if direcao == 'r':
        t.right(rotacao)
    elif direcao == 'e':
        t.left(rotacao)
    else:
        continue

    sentido = input(
        'A tartaruga se moverá para frente(f) ou para trás(t)? ').lower()
    distancia = int(input('A tartaruga se morá por quantos pixels? '))

    if sentido == 'f':
        t.forward(distancia)
    elif sentido == 't':
        t.backward(distancia)
    else:
        continue

    novo_comando = input('Deseja inserir mais comandos? (s/n)').lower()
    if novo_comando == 'n':
        continua = False
