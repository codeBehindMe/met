""" Function to calculate determinant of a matrix """

import numpy as np


def det(m: np.ndarray) -> float:
    """
    Calculates the determinant of a matrix.

    :param: m: numpy.ndarray guaranteed to be a valid matrix shape.

    :return: Determinant of the matrix
    """

    if m.shape == (2, 2):
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])

    # iterate across top column
    # for each element in top column multiply by inner matrix determinant
    determinant  = 0

    for index, element in enumerate(m[0]):
        innerMatrix = np.delete(m, index, 1)[1:, :]
        if (index % 2) == 0:
            determinant += element * det(innerMatrix)
        else:
            determinant -= element * det(innerMatrix)


    return determinant
