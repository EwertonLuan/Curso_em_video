velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80)* 7
if velocidade > 80:
    print('Você estava a {}km/h ultrapassando o limite de velocidade de 80km'.format(velocidade))
    print('Valor da multa a ser pago R${:.2f}'.format(multa))
else:
    print('O veiculo estava a {}km/h, que se encontra dentro do limite de 80km/h'.format(velocidade))
