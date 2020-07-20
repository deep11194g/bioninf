# Global alignment score with Substitution Matrix and Affine Gap Penalties

import numpy as np
from substitution_matrix import blosum62
from needleman_wunsch import alignment

np.set_printoptions(precision=3)


def build_matrix(s1, s2):
    num_rows = len(s1) + 1  # Parallel to column
    num_cols = len(s2) + 1  # Parallel to row

    score = np.zeros((num_rows, num_cols))
    d_del = np.zeros((num_rows, num_cols))
    d_ins = np.zeros((num_rows, num_cols))
    for i in range(1, num_rows):
        score[i][0] = s_o + i * s_e
        d_ins[i][0] = score[i][0] + s_o

    for j in range(1, num_cols):
        score[0][j] = s_o + j * s_e
        d_del[0][j] = score[0][j] + s_o

    directions = np.empty([num_rows, num_cols], dtype=np.dtype('U10'))
    directions[0] = ['W'] * num_cols  # 1st row
    directions[:, 0] = ['N'] * num_rows  # 1st column
    directions[0][0] = ''

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            s = s_m if s1[i - 1] == s2[j - 1] else s_r  # Using scoring scheme
            s = blosum62[tuple(sorted((s1[i - 1], s2[j - 1])))]
            d_del[i][j] = max(
                d_del[i - 1][j] + s_e,
                score[i - 1][j] + s_o + s_e
            )
            d_ins[i][j] = max(
                d_ins[i][j - 1] + s_e,
                score[i][j - 1] + s_o + s_e
            )
            max_val = max(
                d_del[i][j],
                d_ins[i][j],
                score[i - 1][j - 1] + s,
            )
            score[i][j] = max_val
            dirs = []
            if max_val == score[i][j - 1] + s_e:
                dirs.append('W')
            if max_val == score[i - 1][j] + s_e:
                dirs.append('N')
            if max_val == score[i - 1][j - 1] + s:
                dirs.append('NW')
            directions[i][j] = ','.join(dirs)

        print("Insertion Scores:\n{}\n\nDeletion Scores:\n{}\n".format(d_ins, d_del))
    return directions, score


np.set_printoptions(precision=3)

if __name__ == '__main__':
    s_m = 10  # Match Penalty
    s_r = -10  # Mismatch Penalty
    s_e = -1  # Gap Penalty
    s_o = -3  # Affine Gap Penalty

    str1 = "LSFEKKQQFDAI"
    str2 = "LSSQEQAFY"
    dir_matrix, matrix = build_matrix(str1, str2)
    print("Scoring Matrix: \n{}\n".format(matrix))
    alignment(str1, str2, len(str1), len(str2), "", "", dir_matrix)
