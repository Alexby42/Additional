print('--------------------version 1.0--------------------')
list1 = [14, 56, 8, 25, 37]
list2 = [5, 47, 85, 31, 42]
def summa():
    list = [sum(i) for i in zip(list1, list2)]
    print(list)
summa()
print('--------------------version 2.0--------------------')
list_ = []
def summa(args1, args2):
    for i in range(len(args1)):
        list_.append(args1[i] + args2[i])
summa([14, 56, 8, 25, 37], [5, 47, 85, 31, 42])
print(list_)