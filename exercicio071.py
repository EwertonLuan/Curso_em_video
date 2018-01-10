
a_50 = 0
b_20 = 0
c_10 = 0
d_1 = 0

while True:
    sacar = int(input('Quanto vc deseja sacar: R$'))
    while sacar >= 50:
        sacar = sacar - 50
        a_50 += 1

    while sacar >= 20:
        sacar = sacar - 20
        b_20 += 1

    while sacar >= 10:
        sacar = sacar - 10
        c_10 += 1

    while sacar >= 1:
        sacar = sacar - 1
        d_1 += 1
    break

if a_50 > 0:
    print(f'total de celulas de 50 {a_50}')
if b_20 >0:
    print(f'total de celulas de 20 {b_20}')
if c_10 >0:
    print(f'total de celulas de 10 {c_10}')
if d_1 >0:
    print(f'total de celulas de 1 {d_1}')

