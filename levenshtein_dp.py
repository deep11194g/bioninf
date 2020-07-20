# Global alignment with binary reward and penalty

import numpy as np

np.set_printoptions(precision=3)


def build_matrix(s1, s2):
    num_rows = len(s1) + 1  # Parallel to column
    num_cols = len(s2) + 1  # Parallel to row

    matrix = np.zeros((num_rows, num_cols))
    matrix[0] = list(range(num_cols))  # 1st row
    matrix[:, 0] = list(range(num_rows))  # 1st column

    dir_matrix = np.empty([num_rows, num_cols], dtype=np.dtype('U10'))
    dir_matrix[0] = ['W'] * num_cols  # 1st row
    dir_matrix[:, 0] = ['N'] * num_rows  # 1st column
    dir_matrix[0][0] = ""

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            s = int(not (s1[i - 1] == s2[j - 1]))
            min_val = min(
                matrix[i][j - 1] + 1,
                matrix[i - 1][j] + 1,
                matrix[i - 1][j - 1] + s,
            )
            matrix[i][j] = min_val
            dirs = []
            if min_val == matrix[i][j - 1] + 1:
                dirs.append('W')
            if min_val == matrix[i - 1][j] + 1:
                dirs.append('N')
            if min_val == matrix[i - 1][j - 1] + s:
                dirs.append('NW')
            dir_matrix[i][j] = ','.join(dirs)
    return dir_matrix, matrix


def alignment(str1, str2, i, j, aligned1, aligned2, dir_matrix):
    dirs = dir_matrix[i][j].split(',')
    if 'N' in dirs:
        a1 = "{}{}".format(str1[i - 1], aligned1)
        a2 = "{}{}".format("-", aligned2)
        alignment(str1, str2, i - 1, j, a1, a2, dir_matrix)
    if 'W' in dirs:
        a1 = "{}{}".format("-", aligned1)
        a2 = "{}{}".format(str2[j - 1], aligned2)
        alignment(str1, str2, i, j - 1, a1, a2, dir_matrix)
    if 'NW' in dirs:
        a1 = "{}{}".format(str1[i - 1], aligned1)
        a2 = "{}{}".format(str2[j - 1], aligned2)
        alignment(str1, str2, i - 1, j - 1, a1, a2, dir_matrix)
    if not dir_matrix[i][j] or dirs == ['']:
        print()
        print(aligned1)
        print(aligned2)


if __name__ == '__main__':
    str1 = "PYTHON"
    str2 = "PYMOL"
    dir_matrix, matrix = build_matrix(str1, str2)
    print(matrix)
    # print(dir_matrix)
    alignment(str1, str2,len(str1), len(str2), "", "", dir_matrix)
