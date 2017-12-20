print('\033[1;33m=-\033[m' * 20 + '\n Financiamento para compra de casas\n' + '\033[1;33m=-\033[m' * 20)

v_casa = float(input('Valor da casa: '))
sala = float(input('Renda: '))
anos = int(input('Em quantos anos deseja pagar: '))
empre = (sala*30)/100*12

if v_casa / anos > empre:
    print('''O valor da mensalidade ultrapassa 30% da sua renda
Você pode parcelar em {:.2f} anos com parcelas mensais de {:.2f}'''.format(v_casa / empre, empre / 12))
else:
    print('O valor a de {} será pago em {} anos com parcelas mensais de {:.2f}'.format(v_casa, anos, v_casa/anos/12))
