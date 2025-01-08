def rotateby90(mat):
    # code here
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        l = 0
        r = n - 1
        while l <= r:
            mat[l][i], mat[r][i] = mat[r][i], mat[l][i]
            l += 1
            r -= 1
