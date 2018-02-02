ida = 0  # idade dos dois somados
h_velho = 0  # idade do homem mais velho
h_vn = ''  # Nome do homem mais velho
m_20 = 0  # mulheres com 20 anos
for i in range(1, 5):
        nome = str(input('Digite o nome {}ª pessoa: '.format(i)))
        idade = int(input('Dite idade {}ª pessoa: '.format(i)))
        ida += idade
        sexo = str(input('Qual o sexo da {}ªpessoa (H/M): '.format(i))).upper().strip()
        if sexo == 'H' and i == 1:
                h_velho = idade
                h_vn = nome
        elif idade > h_velho:
                h_velho = idade
                h_vn = nome
        if sexo == 'M' and idade < 20:
                m_20 += 1
media = ida / 4
print('Media de idade entre homens e mulheres é de {}'.format(media))
print('O homem mais velho é o {} com {} anos de idade'.format(h_vn, h_velho))
print('{} mulheres com menos de 20 anos'.format(m_20))
