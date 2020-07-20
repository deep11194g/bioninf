import numpy as np

from levenshtein_dp import build_matrix

if __name__ == '__main__':
    sequences = [
        "ATCC",
        "ATGC",
        "TTAG",
        "TCGG"
    ]

    scores = np.zeros((4, 4))
    for idx_i, i in enumerate(sequences):
        for idx_j, j in enumerate(sequences):
            if i == j:
                continue
            _, score_matrix = build_matrix(i, j)
            scores[idx_i][idx_j] = score_matrix[4][4]

    print(scores)


