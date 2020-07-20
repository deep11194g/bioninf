# Local alignment score with scoring scheme and/or substitution matrix

import numpy as np
from substitution_matrix import sample1

np.set_printoptions(precision=3)


def build_matrix(s1, s2):
    num_rows = len(s1) + 1  # Parallel to column
    num_cols = len(s2) + 1  # Parallel to row

    matrix = np.zeros((num_rows, num_cols))
    max_val = 100000

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            s = s_m if s1[i - 1] == s2[j - 1] else s_r
            # s = sample1[tuple(sorted((s1[i - 1], s2[j - 1])))]
            matrix[i][j] = max(
                0,
                matrix[i][j - 1] + s_g,
                matrix[i - 1][j] + s_g,
                matrix[i - 1][j - 1] + s
            )
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]

    return matrix


if __name__ == '__main__':
    s_m = 0.5
    s_r = -0.3
    s_g = -0.5

    str1 = "ACEDECADE"
    str2 = "REDCEDKL"
    matrix = build_matrix(str1, str2)
    print(matrix)
