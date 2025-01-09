def countTrianglesSlow(arr):
    # code here
    n = len(arr)
    # res = set()
    res = []
    arr.sort()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # print(i, j, k)
                if (
                    arr[i] + arr[j] > arr[k]
                    and arr[i] + arr[k] > arr[j]
                    and arr[j] + arr[k] > arr[i]
                ):
                    a = [arr[i], arr[j], arr[k]]
                    # a.sort()
                    # a = tuple(a)
                    # res.add(a)
                    res.append(a)
    print(len(res), res)


def countTrianglesFast(arr):
    # code here
    n = len(arr)
    # res = set()
    res = 0
    arr.sort()
    for i in range(2, n):
        l = 0
        r = i - 1
        while l < r:
            if arr[l] + arr[r] > arr[i]:
                res += r - l
                r -= 1
            else:
                l += 1

    print(res)


countTrianglesFast([1, 8, 26, 23, 8, 43, 32, 8, 47])
countTrianglesFast([10, 21, 22, 100, 101, 200, 300])
countTrianglesFast([1, 2, 3])
