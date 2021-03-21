num = [8, 5, 9, 1]
num[2] = 3
# as listas são mutáveis
num.append(7)
#num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o valor 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')




