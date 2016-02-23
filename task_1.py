#! -*- coding: utf-8 -*-
import sys

def factor(n):
    """
    Используем разложение на простые множители
    """
    factors = []
    begin = 2

    while begin * begin <= n:

        if n % begin == 0:
            factors.append(begin)
            n //= begin
        else:
            begin += 1

    if n > 1:
        factors.append(n)

    return factors


if __name__ == '__main__':
    n = int(input('Введите число N: '))
    result = [factor(number) for number in range(1, n+1)]

    for idx, elem in enumerate(result):
        print str(idx+1) + ' = ' + str(elem)
