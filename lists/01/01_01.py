from math import sqrt


def calculateSquaredDifference(p_first_term, p_second_term):
    return (p_first_term - p_second_term) * (p_first_term - p_second_term)


def calculateDistance(p_x1, p_y1, p_x2, p_y2):
    return sqrt(calculateSquaredDifference(p_x2, p_x1) + calculateSquaredDifference(p_y2, p_y1))


if __name__ == '__main__':
    x1, y1 = [float(number) for number in input().split()]
    x2, y2 = [float(number) for number in input().split()]

    print('{0:.4f}'.format(calculateDistance(x1, y1, x2, y2)))


# import numpy as np
# from math import pow, sqrt


# def buildArray():
#     line1 = input()
#     line2 = input()

#     values1 = line1.split('')
#     values2 = line2.split('')

#     inputs = (np.array([values1]))
#     inputs = (np.append(inputs, [values2], axis=0)).astype(float)

#     return inputs


# def calculateSquaredDifference(p_first_term, p_second_term):
#     return pow(p_first_term, 2) - (2 * p_first_term * p_second_term) + pow(p_second_term, 2)


# def calculateDistance(p_x1, p_y1, p_x2, p_y2):
#     return sqrt(calculateSquaredDifference(p_x2, p_x1) + calculateSquaredDifference(p_y2, p_y1))


# if __name__ == '__main__':
#     values = buildArray()
#     print('{0:.4f}'.format(calculateDistance(values[0,0], values[0,1],
#                                              values[1,0], values[1,1])))
