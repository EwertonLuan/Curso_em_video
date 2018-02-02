
lado_1 = int(input('Digite o primeiro lado: '))
lado_2 = int(input('Digite o segundo lado: '))
lado_3 = int(input('Digite o terceiro lado: '))

triangulo = teste = lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_2 +lado_1 #(lado_1<lado_2) < lado_3 < (lado_1+lado_2)

if triangulo == True:
    print('E possivel criar um triangulo com as medidas {}, {}, {}'.format(lado_1, lado_2, lado_3))
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('Triangulho equilátero ')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_3 == lado_2:
        print('Triangulho isósceles ')
    else:
        print('Triangulo escaleno')
else:
    print('Não e possivel criar um triângulo com essas medidas')