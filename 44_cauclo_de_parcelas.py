print('\033[1;35m###\033[m' * 20 + "\n{:=^50}\n".format('Calculo de pagamento') + '\033[1;35m###\033[m' * 20)
# {:^} Centraliza
produto = float(input('Qual o valor do prouto: '))

print("""\n[1] À vista no dinheiro/cheque
[2] À vista no cartão 
[3] Em até 2x no catão
[4] 3x ou mais no cartão\n""")

pagamento = int(input('Qual a Forma de pagamento: '))

if pagamento == 1:
    total = produto - (produto * 10) / 100
elif pagamento == 2:
    total = produto - (produto * 5) / 100
elif pagamento == 3:
    total = produto
else:
    total = (produto * 20) / 100 + produto
print('Você escolheu a opção {}, o valor a ser pago é de R${:.2f}'.format(pagamento,total))
