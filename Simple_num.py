n = int(input('Введите число: '))
s = [i for i in range(n + 1)]
s[1] = 0
i = 2
while i <= n:
    if s[i] != 0:
       j = i + i
       while j <= n:
           s[j] = 0
           j = j + i
    i += 1
s = [i for i in s if i != 0]
print(s)