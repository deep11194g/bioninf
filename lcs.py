# Longest Common Subsequence
import numpy as np

from levenshtein_dp import alignment

np.set_printoptions(precision=3)


def build_matrix(s1, s2):
    num_rows = len(s1) + 1  # Parallel to column
    num_cols = len(s2) + 1  # Parallel to row

    matrix = np.zeros((num_rows, num_cols))
    matrix[0] = [0] * num_cols  # 1st row
    matrix[:, 0] = [0] * num_rows  # 1st column

    dir_matrix = np.empty([num_rows, num_cols], dtype=np.dtype('U10'))
    dir_matrix[0] = ['W'] * num_cols  # 1st row
    dir_matrix[:, 0] = ['N'] * num_rows  # 1st column
    dir_matrix[0][0] = ""

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            s = int(s1[i - 1] == s2[j - 1])
            max_val = max(
                matrix[i][j - 1],
                matrix[i - 1][j],
                matrix[i - 1][j - 1] + s,
            )
            matrix[i][j] = max_val
            dirs = []
            if max_val == matrix[i][j - 1]:
                dirs.append('W')
            if max_val == matrix[i - 1][j]:
                dirs.append('N')
            if max_val == matrix[i - 1][j - 1] + s:
                dirs.append('NW')
            dir_matrix[i][j] = ','.join(dirs)
    return dir_matrix, matrix


if __name__ == '__main__':
    str1 = "LSFEKKQQFDAI"
    str2 = "LSSQEQAFY"
    dir_matrix, matrix = build_matrix(str1, str2)
    print(matrix)
    print(dir_matrix)
    alignment(str1, str2, len(str1), len(str2), "", "", dir_matrix)
