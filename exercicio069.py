maior_18 = 0
homens = 0
mulheres_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo M/F: ')).strip().upper()[0]
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar S/N?')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''Tem {maior_18} pessoa(s) maior de idade
foram cadastrados {homens}
E {mulheres_20} mulheres com menos de 20 anos''')
