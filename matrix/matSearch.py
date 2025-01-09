def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        l = 0
        r = m - 1
        if x > mat[i][r]:
            continue
        if mat[i][l] <= x <= mat[i][r]:
            for j in range(m):
                if x == mat[i][j]:
                    return True
    return False
