my_list = [7, 5, 3, 3, 2]
num_input = int(input('введите число: '))

n = 0
m = 0
for item in my_list:
    if item >= num_input:
        m = n
    n += 1
if m == 0 and num_input > my_list[m]:
    my_list.insert(m, num_input)
elif m != 0 or m == 0 and num_input == my_list[m]:
    my_list.insert(m+1, num_input)

print(my_list)
