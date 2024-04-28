my_string = input('Введите любую последовательность целых чисел через пробел:')
my_list = my_string.split()
for i, item in enumerate(my_list):
    my_list[i] = int(item)
def max(*args):
    if not args:
        return 0
    value = args[0]
    for i in args[1:]:
        if i > value:
            value = i
    return value
print(max(*my_list))