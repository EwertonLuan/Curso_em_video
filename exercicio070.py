total = mais_mil = barato_valo = 0
barato_nome = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    total += preco
    if total == 0 or preco < barato_valo:
        barato_nome = nome
        barato_valo = preco
    if preco > 1000:
        mais_mil += 1
    conti = ''
    while conti not in 'SN':
        conti = str(input('Deseja continuar S/N?')).strip().upper()
    if conti == 'N':
        break
print(f'''O valor total da compra R${total:.2f}
O produto mais barato foi {barato_nome} que custa R${barato_valo}
Tem {mais_mil} que custão mais de mil reias''')
