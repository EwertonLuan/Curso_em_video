s = float(input('Digite o seu salario: '))
s_s = (s*10)/100 + s
s_i = (s*15)/100 + s

if s > 1250:
 print('O seu salario passara de R${} para R${}'.format(s, s_s))
else:
 print('O seu salario passara de R${} para R${}'.format(s, s_i))