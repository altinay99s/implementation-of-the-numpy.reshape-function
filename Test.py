import numpy as np
from reshape import reshape
import random


def test_1():
    lst = []

    for i in range(4):
        arr = []
        for j in range(6):
            arr.append(j + i * 6)
        lst.append(arr)

    arr = []
    arr.append(np.all(reshape(lst, (2, -1, 3), 'F') == np.reshape(lst, (2, -1, 3), 'F')))
    arr.append(np.all(reshape(lst, (2, 3, 4), 'C') == np.reshape(lst, (2, 3, 4), 'C')))
    arr.append(np.all(reshape(lst, (4, 2, 3)) == np.reshape(lst, (4, 2, 3))))
    arr.append(np.all(reshape(lst, 24, 'F') == np.reshape(lst, 24, 'F')))
    return np.all(arr)


def test_2():
    arr = []
    arr.append(np.all(np.reshape('(1,2)', 1, 'C') == reshape('(1,2)', 1, 'C')))
    arr.append(np.all(np.reshape('abc', 1, 'F') == reshape('abc', 1, 'F')))
    arr.append(np.all(np.reshape("123", -1) == reshape("123", -1)))

    d = {'dict': 1, 'dictionary': 2}
    arr.append(np.all(np.reshape(d, 1) == reshape(d, 1)))

    arr.append(np.all(reshape(2, 1, "C") == np.reshape(2, 1, "C")))
    arr.append(np.all(reshape((1, 2, 3, 4), (2, 2), 'F') == np.reshape((1, 2, 3, 4), (2, 2), 'F')))

    arr.append(np.all(reshape(True, 1) == np.reshape(True, 1)))

    return np.all(arr)


def test_3(order='C'):
    n = 100
    arr = [[random.randint(0, n) for i in range(10)] for j in range(10)]
    print('Original array:')
    print(arr)
    arr_1 = reshape(arr, (5, 2, 5, 2), order)
    arr_2 = np.reshape(arr, (5, 2, 5, 2), order)
    print('My array:')
    print(arr_1)
    print('Numpy array:')
    print(arr_2)
    return np.all(arr_1 == arr_2)


def test_4(order='C'):
    n = 99
    arr = [[[random.randint(0, n) for i in range(3)] for j in range(11)] for k in range(3)]
    print('Original array:')
    print(arr)
    arr_1 = reshape(arr, (11, 9), order)
    arr_2 = np.reshape(arr, (11, 9), order)
    print('My array:')
    print(arr_1)
    print('Numpy array:')
    print(arr_2)
    return np.all(arr_1 == arr_2)


def test_5(order='C'):
    n = 200
    arr = [[[[random.randint(0, n) for i in range(5)] for j in range(2)] for k in range(4)] for l in range(5)]
    print('Original array:')
    print(arr)
    arr_1 = reshape(arr, (4, 5, 10), order)
    arr_2 = np.reshape(arr, (4, 5, 10), order)
    print('My array:')
    print(arr_1)
    print('Numpy array:')
    print(arr_2)
    return np.all(arr_1 == arr_2)
