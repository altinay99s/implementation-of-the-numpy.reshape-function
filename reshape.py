import numpy
import numpy as np


def line_style(array: list):
    lst = []
    for elem in array:
        if isinstance(elem, list):
            lst += line_style(elem)
        else:
            lst.append(elem)
    return lst


# def columnar_style_(array: list):
#     lst = []
#     if array:
#         elem = array[0]
#         if isinstance(elem[0], list):
#             lst_ = columnar_style(elem)
#             if lst_ is not False:
#                 lst += lst_
#
#         else:
#             lst.append(elem[0])
#             array.remove(elem)
#             del elem[0]
#             if elem:
#                 array.append(elem)
#             lst += columnar_style(array)
#
#     return lst


def depth_entrance(arr: list):
    if arr:
        elem = arr[0]
        if isinstance(elem, list):
            new_elem = depth_entrance(elem)
            arr.remove(elem)
            if elem:
                arr.append(elem)
        else:
            new_elem = elem
            arr.remove(elem)
        return new_elem


def columnar_style(array: list):
    lst = []
    while array:
        lst.append(depth_entrance(array))
    return lst


def decompose_line_style(array: list, shape: list):
    lst = []
    l = []
    for i in range(len(array)):
        if i % shape[-1] == 0 and l:
            lst.append(l)
            l = []
        l.append(array[i])
    lst.append(l)
    del shape[-1]
    if shape:
        return decompose_line_style(lst, shape)
    return lst


def decompose_columnar_style(array: list, shape: list):
    lst = []
    n = int(shape[0])
    size = int(len(array) / n)
    del shape[0]
    if not shape:
        return array

    for i in range(n):
        l = []
        for j in range(size):
            l.append(array[i + j * n])
        lst.append(decompose_columnar_style(l, shape.copy()))
    return lst


def copy_array(array):
    temp = []
    for i in array:
        if isinstance(i, list):
            temp.append(copy_array(i))

        else:
            temp.append(i)
    return temp


def reshape(array, new_shape, order='C'):
    size = 1
    unknown_dimension = 0

    if isinstance(array, (list, numpy.ndarray)) is False:
        if isinstance(array, tuple):
            arr_ = list(array)
        else:
            if new_shape == 1 or new_shape == -1:
                lst = []
                lst.append(array)
                return lst
            raise ValueError('You cannot reshape array of size', size, 'into shape', new_shape)
    else:
        arr_ = copy_array(array)

    if isinstance(new_shape, (tuple, int)) is False:
        raise TypeError('Shape is not a tuple or integer')

    if order != 'C' and order != 'F':
        raise ValueError("You can only enter: 'C' or 'F'")

    shape = list(np.shape(array))

    if isinstance(new_shape, tuple):
        for i in new_shape:
            if isinstance(i, int) is False:
                raise TypeError('Elements in shape is not integer')
            if i == -1:
                unknown_dimension += 1
                continue
            size *= i

        if unknown_dimension > 1:
            raise ValueError('You can only add one unknown dimension')

        size_original = 1
        for i in shape:
            size_original *= i

        shape_ = list(new_shape)

        if unknown_dimension == 1:
            if size_original % size != 0:
                raise ValueError('You cannot reshape array of size', size, 'into shape', new_shape)
            for i in range(len(shape_)):
                if shape_[i] == -1:
                    shape_.remove(-1)
                    shape_.insert(i, size_original / size)
                    size = size_original
                    break

        if size != size_original:
            raise ValueError('You cannot reshape array of size', size, 'into shape', new_shape)

        lst = array

        if order == 'F':
            if len(shape) != 1:
                lst = columnar_style(arr_)
            return decompose_columnar_style(lst, shape_)

        if len(shape) != 1:
            lst = line_style(arr_)
        return decompose_line_style(lst, shape_)

    else:
        if isinstance(new_shape, int) is False:
            raise TypeError('Elements in shape is not integer')

        size_original = 1
        for i in shape:
            size_original *= i

        if new_shape == -1:
            new_shape = size_original

        if new_shape != size_original:
            raise ValueError('You cannot reshape array of size', size, 'into shape', new_shape)

        if order == 'F':
            if len(shape) != 1:
                return columnar_style(arr_)
        if len(shape) != 1:
            return line_style(arr_)
        return array

#
# lst = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
# columnar_style1(lst)
