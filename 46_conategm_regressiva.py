from time import sleep
import emoji

print('\033[1;34m{:=^40}\033[m'.format('Contagem Regressiva'))
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':sparkles:'*10+':fireworks:'*10,use_aliases=True))


