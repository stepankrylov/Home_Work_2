list_el = [1234, 12.34, '1234', [1, 2, 3, 4], (1, 2, 3, 4), {1, 2, 3, 4}, {1: 2, 3: 4}]
list_type = []

for item in list_el:
    list_type.append([item, type(item)])

print(list_type)
