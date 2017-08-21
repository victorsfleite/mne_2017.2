value = float(input())

options = [float(item) for item in range(0, 101, 25)]

if (value == 0):
    print('Intervalo [{},{}]'.format(int(options[0]), int(options[1])))

elif (0 < value <= options[-1]):
    for i in range(len(options) - 1):
        if (options[i] < value <= options[i + 1]):
            print('Intervalo ({},{}]'.format(int(options[i]), int(options[i + 1])))
            break

else:
    print('Fora de intervalo')
