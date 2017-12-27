print('\033[1;34m=*=\033[m' * 10 + '\n Calcule o sei IMC\n' + '\033[1;34m=*=\033[m' * 10)
peso = float(input('Didite seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso/(altura * altura)

if imc < 18.5:
    print('Seu IMC é de {:.2f} você se encontra abaixo do peso'.format(imc))
elif 18.5 <= imc < 25.0:
    print('Seu IMC é de {:.2f} você se encontra no peso ideal'.format(imc))
elif 25.0 <= imc < 30.0:
    print('Seu IMC é de {:.2f} você esta com sobrepeso'.format(imc))
elif 30.0 <= imc < 40.0:
    print('Seu IMC é de {:.2f} você está com obsidade'.format(imc))
else:
    print('Seu IMC é de {:.2f} você esta com Obseidade mŕobida'.format(imc))
