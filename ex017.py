import math
from math import sqrt
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
#abaixo é a hipotenusa
hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
print('O comprimento da hipotenusa é: {:.4f}'.format(hipotenusa))