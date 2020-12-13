possui_passaporte = True
passagem_comprada = True
menor_de_idade = False

pode_viajar01 = ((possui_passaporte and passagem_comprada)
                 and not menor_de_idade)
pode_viajar02 = ((possui_passaporte or passagem_comprada)
                 and not menor_de_idade)
pode_viajar03 = ((not possui_passaporte or passagem_comprada)
                 and not menor_de_idade)
pode_viajar04 = ((not possui_passaporte or not passagem_comprada)
                 and menor_de_idade)

print(pode_viajar01)
print(pode_viajar02)
print(pode_viajar03)
print(pode_viajar04)
