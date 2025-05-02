# [3,1,2]
def printSubsequences(inputArr, res, curr, N):
    if curr >= N:
        print(res)
        return
    res.append(inputArr[curr])
    printSubsequences(inputArr, res, curr + 1, N)
    res.pop()
    printSubsequences(inputArr, res, curr + 1, N)


# subsequence where sum is K
def printSubsequencesSumK(inputArr, res, c_sum, i, N, K):

    # return
    if i >= N:
        if c_sum == K:
            print(res)
        return
    c_sum += inputArr[i]
    res.append(inputArr[i])
    printSubsequencesSumK(inputArr, res, c_sum, i + 1, N, K)
    c_sum -= inputArr[i]
    res.pop()
    printSubsequencesSumK(inputArr, res, c_sum, i + 1, N, K)


# the variation is to return true/false or 1/0 to get count
printSubsequencesSumK([3, 1, 2], [], 0, 0, 3, 3)
