a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))
c = int(input('Digite o teceiro lado do triângulo: '))

triangulo = (a-b)<c<(a+b)

if triangulo == True:
    print('E possivel criar um triangulo com as medidas {}, {}, {}'.format(a,b,c))
else:
    print('Não e possivel criar um triângulo com essas medidas')
