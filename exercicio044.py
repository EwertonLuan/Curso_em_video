print('\033[1;35m###\033[m' * 10 + "\nCalculo de pagamento\n" + '\033[1;35m###\033[m' * 10)

produto = float(input('Qual o valor do prouto: '))
a_vista = produto - (produto * 10) / 100
cartao = produto - (produto * 5) / 100
cartao_2 = produto
cartao_3 = (produto * 20) / 100 + produto

print("""\nÀ vista no dinheiro/cheque [1]
À vista no cartão [2]
Em até 2x no catão [3]
3x ou mais no cartão  [4]\n""")

pagamento = int(input('Qual a Forma de pagamento: '))

if pagamento == 1:
    print('Você escolheu a opção 1, o valor a ser pago é de R${:.2f}'.format(a_vista))
elif pagamento == 2:
    print('Você escolheu a opção 2, o valor a ser pago é de R${:.2f}'.format(cartao))
elif pagamento == 3:
    print('Você escolheu a opção 2, o valor a ser pago é de R${:.2f}'.format(cartao_2))
else:
    print('Você escolheu a opção 1, o valor a ser pago é de R${:.2f}'.format(cartao_3))
