def get_lev_dist(i, j):
    if min(i, j) == 0:
        return max(i, j)
    return min([
        get_lev_dist(i - 1, j) + 1,
        get_lev_dist(i, j - 1) + 1,
        get_lev_dist(i - 1, j - 1) + (str1[i - 1] != str2[j - 1]),
    ])


if __name__ == "__main__":
    str1 = "Soumyadeep G"
    str2 = "S Deep G"
    print(get_lev_dist(len(str1), len(str2)))
