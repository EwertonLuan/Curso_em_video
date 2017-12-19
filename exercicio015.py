kp = int(input('Qual a quantidade de km pecorridos: '))
da = int(input('Quantos dias o carro foi alugado: '))
pagar = (kp*0.15)+(da*60)
print('O valor a se pago por {} dias e {}km rodados é {}'.format(da,kp,pagar))