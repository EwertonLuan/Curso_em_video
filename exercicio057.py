nome = str(input('Digite um nome: ')).strip()
sexo = str(input('Digite M (masculino) ou F (feminino) pata escolha do sexo: ')).upper().strip()

while not sexo in 'MF':
    sexo = str(input('''O valor digitado estava errado,
digite M (masculino) ou F (feminino) para escolha do sexo: ''')).upper().strip()

print(sexo)
