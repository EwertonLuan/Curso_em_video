import math

an = float(input('Digite um angulo: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan= math.tan(math.radians(an))
print('O angdo de {} tem o seno {:.2f} o coseno {:.2f} e a tangente {:.2f}'.format(an,se,co,tan))