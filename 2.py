list_in = list(map(int, input('Введите числа через пробел ').split()))
list_out = []

for i in range(0, len(list_in), 2):
    a = list_in[i:i + 2]
    a.reverse()
    for itm in a:
        list_out.append(itm)

print(list_out)
