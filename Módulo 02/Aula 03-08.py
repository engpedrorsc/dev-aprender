comprimento_cabelo = 25

if comprimento_cabelo <= 20:
    print('O preço do seu corte é R$50,00')
elif 20 < comprimento_cabelo <= 30:
    print('O preço do seu corte é R$70,00')
elif 30 < comprimento_cabelo <= 50:
    print('O preço do seu corte é R$100,00')
elif comprimento_cabelo > 50:
    print('Por favor, consulte a recepção para saber o preço do corte.')
