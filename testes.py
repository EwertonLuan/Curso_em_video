h_nome = []
h_idade = []
m_nome = []
m_idade = []
h = 0  # quantidade de homens
m = 0  # Quantiades de mulher
id = 0  # idade dos dois somados
h_velho = 0  # idade do homem mais velho
h_vn = ''  # Nome do homem mais velho
m_20 = 0 # mulheres com 20 anos
for i in range(1, 3):
    sexo = str(input('Qual o sexo da {}ªpessoa (H/M): '.format(i))).upper().strip()
    if sexo == 'H':
        nome = str(input('Digite o nome {}ª pessoa: '.format(i)))
        h_nome.append(nome)
        idade = int(input('Dite idade {}ª pessoa: '.format(i)))
        h_idade.append(idade)
        h += 1
        if i == 1:
            h_velho = idade
            h_vn = nome
        else:
            if idade >= h_velho:
                h_velho = idade
                h_vn = nome
        id += idade
    elif sexo == 'M':
        nome2 = str(input('Digite o nome {}ª pessoa: '.format(i)))
        m_nome.append(nome2)
        idade2 = int(input('Dite idade {}ª pessoa: '.format(i)))
        if idade2 < 20:
            m_20 += 1
        id += idade2
        m_idade.append(idade2)
        m += 1
media = id / 2
print('Media {} quantidade de homes {} mulheres {}'.format(media, h, m))
print('O homem mais velho é o {} com {} anos de idade'.format(h_vn, h_velho))
print('{} mulheres com menos de 20 anos'.format(m_20))
