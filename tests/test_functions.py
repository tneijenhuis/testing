import numpy as np
import mypackage.my_fuctions as mf


def test_make_array():
    numb_list = (1, 2, 3)
    array = mf.put_in_array(*numb_list)
    assert array[0] == 1
    assert array[1] == 2
    assert array[2] == 3


def test_transpose():
    matrix = np.matrix([[1, 2], [3, 4]])
    transposed = mf.transpose_matrix(matrix)
    assert transposed[0, 0] == matrix[0, 0]
    assert transposed[1, 0] == matrix[0, 1]
    assert transposed[0, 1] == matrix[1, 0]
    assert transposed[1, 1] == matrix[1, 1]
