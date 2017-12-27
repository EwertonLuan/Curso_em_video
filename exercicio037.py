numero = int(input('Digite um numero: '))
escolha = int(input('\n\nBinário [1]\nOctal [2]\nHexadecimal [3]\n\nEscolhe uma das opções: '))
bina = bin(numero)[2:]
octal = oct(numero)[2:]
hexa = hex(numero)[2:]

if escolha == 1:
    escolha = bina
elif escolha == 2:
    escolha = octal
else:
    escolha = hexa

print(escolha)
