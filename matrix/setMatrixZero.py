def setMatrixZeroes(mat):
    n = len(mat)
    m = len(mat[0])
    rows = set()
    cols = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(n):
        for j in range(m):
            if i in rows or j in cols:
                mat[i][j] = 0
