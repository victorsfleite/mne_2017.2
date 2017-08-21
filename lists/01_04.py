string = input().replace(' ', '')
inverse = string[::-1]

if string == inverse:
    print('Palindromo encontrado')

else:
    print('Palindromo nao encontrado')
