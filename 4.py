my_string = input('введите строку: ')

list_str = my_string.split()
n = 0
for item in list_str:
    print(n+1, item[:10])
    n += 1
