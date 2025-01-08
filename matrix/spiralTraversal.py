def spiralTraversal(mat):
    n, m = len(mat), len(mat[0])
    dirs = {3: (-1, 0), 1: (1, 0), 2: (0, -1), 0: (0, 1)}
    visited = set()
    size = n * m
    res = []
    i = j = d = 0
    for _ in range(size):
        # print(d)
        res.append(mat[i][j])
        visited.add((i, j))
        ni, nj = i + dirs[d][0], j + dirs[d][1]
        if not (0 <= ni < n) or not (0 <= nj < m) or (ni, nj) in visited:
            d = (d + 1) % 4
        i, j = i + dirs[d][0], j + dirs[d][1]
    print(res)


def spirallyTraverseOptimal(mat):
    n, m = len(mat), len(mat[0])
    UP_LIM, DOWN_LIM, LEFT_LIM, RIGHT_LIM = -1, n, -1, m
    dirs = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
    cd = "RIGHT"
    cx = 0
    cy = 0
    size = n * m
    res = []
    while len(res) < size:
        if cd == "RIGHT":
            while cy < RIGHT_LIM:
                print(cx, cy)
                res.append(mat[cx][cy])
                cy += 1
            cd = "DOWN"
            RIGHT_LIM -= 1
        elif cd == "DOWN":
            while cx < DOWN_LIM:
                res.append(mat[cx][cy])
                cx += 1
            cd = "LEFT"
            DOWN_LIM -= 1
        elif cd == "LEFT":
            while cy > LEFT_LIM:
                res.append(mat[cx][cy])
                cy -= 1
            cd = "UP"
            LEFT_LIM += 1
        else:
            while cx > UP_LIM:
                res.append(mat[cx][cy])
                cx -= 1
            cd = "RIGHT"
            UP_LIM -= 1


spiralTraversal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
