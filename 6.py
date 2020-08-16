# n = (input('введите названия товаров: ')).split()
# p = (input('введите цены на товары: ')).split()
# c = (input('введите кол-во товара: ')).split()
# u = (input('введите ед. измерения кол-ва: ')).split()
n = 'компьютер принтер сканер'.split()
p = '20000 6000 2000'.split()
c = '5 2 7'.split()
u = 'шт. шт. шт.'.split()

product = []
for i in range(len(n)):
    dict_prod = {'название': n[i], 'цена': p[i], 'кол-во': c[i], 'ед.': u[i]}
    list_prod = [i+1, dict_prod]
    product.append(tuple(list_prod))
print(product)
dict_a = {'название': n, 'цена': p, 'кол-во': c, 'ед.': list(set(u))}
print(dict_a)
