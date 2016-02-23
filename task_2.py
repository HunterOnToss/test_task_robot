#! -*- coding: utf-8 -*-

def divide_vector(n, m):
    intervals = []
    elem_count = n / m
    exclude_elem_part = n % m

    divide_begin = exclude_elem_part / 2
    divide_end = n - (exclude_elem_part - exclude_elem_part / 2)

    for elem in xrange(divide_begin, divide_end, elem_count):
        intervals.append([elem, elem + (elem_count-1)])

    return intervals

if __name__ == '__main__':
    n = int(input('Введите размер вектора N: '))
    m = int(input('Введите число частей M: '))

    if m >= n:
        raise ValueError('M должно быть меньше N!')

    result = divide_vector(n, m)
    print result
