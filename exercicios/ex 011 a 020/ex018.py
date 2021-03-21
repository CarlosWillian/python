from math import radians, sin, cos, tan
n = float(input('Digite o valor de um ângulo: '))
#print('O valor do sen{0}° = {1:.3f} \no valor do cos{0}° = {2:.3f} \no valor da tg{0}° = {3:.3f}'.format(n, sin(radians(n)), cos(radians(n)), tan(radians(n))))

sin = sin(radians(n))
cos = cos(radians(n))
tg = tan(radians(n))

print('O valor do sen{0}° = {1:.3f} \no valor do cos{0}° = {2:.3f} \no valor da tg{0}° = {3:.3f}'.format(n, sin, cos, tg))
