def searchRowMatrix(mat, x):
    # code here
    def bs(arr, target):
        l = 0
        r = len(arr)
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        l = 0
        r = m - 1
        if mat[i][l] <= x <= mat[i][r]:
            if bs(mat[i], x):
                return True
    return False
