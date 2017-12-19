viagem = float(input('Qual a distancia da viagem em km?  '))
taxa_1 = viagem * 0.50
taxa_2 = viagem * 0.45
if viagem <= 200:
    print('O valor a ser pago para a viagem é de {:.2f}'.format(taxa_1))
else:
    print('o valor a ser pago é de R${:.2f}'.format(taxa_2))