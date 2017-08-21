qtde = int(input())
values = {}

for i in range(qtde):
    value = int(input())
    values[i + 1] = value

highest = max(values, key=values.get)
print('{}\n{}'.format(values[highest], highest))
