nome = str(input('Digite um nome: ')).strip()
sexo = str(input('Digite M (masculino) ou F (feminino) pata escolha do sexo: ')).upper().strip()[0] # passa para maisculo remove o espaçoe e pega somente a primeira letra

while sexo not in 'MF':
    sexo = str(input('''O valor digitado estava errado,
digite M (masculino) ou F (feminino) para escolha do sexo: ''')).upper().strip()

if sexo == 'M':
    print('sexo masculino')
else:
    print('sexo feminino')
