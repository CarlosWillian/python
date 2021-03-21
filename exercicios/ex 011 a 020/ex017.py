#a = float(input('Digite o valor do cateto a: '))
#b = float(input('Digite o valor do cateto b: '))
#print('O valor da hipotenusa h vale {}'.format(((a**2)+(b**2))**(1/2)))

import math
a = float(input('Digite o valor do cateto a: '))
b = float(input('Digite o valor do cateto b: '))
print('O valor da hipotenusa h vale {}'.format(math.sqrt(math.pow(a, 2)+math.pow(b, 2))))


