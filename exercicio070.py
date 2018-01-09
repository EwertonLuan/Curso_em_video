total = 0
mais_mil = 0
barato_nome = ''
barato_valo = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    if total == 0:
        barato_nome = nome
        barato_valo = preco
    else:
        if preco < barato_valo:
            barato_valo = preco
            barato_nome = nome
    total += preco
    if preco > 1000:
        mais_mil += 1
    conti = str(input('Deseja continuar S/N?')).strip().upper()
    while conti not in 'SN':
        conti = str(input('Deseja continuar S/N?')).strip().upper()
    if conti == 'N':
        break
print(f'''O valor total e de R${total:.2f}
O produto mais barato foi {barato_nome} que custa R${barato_valo}
Tem {mais_mil} que custão mais de mil reias''')
