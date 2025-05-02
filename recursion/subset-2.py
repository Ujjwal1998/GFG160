def printUniqueSubsets(inputArr, res, curr, N):
    ans = []
    unique = []

    def printAllSubsets(inputArr, res, curr, N):
        if curr >= N:
            print(res)
            ans.append(list(res))
            return
        res.append(inputArr[curr])
        printAllSubsets(inputArr, res, curr + 1, N)
        res.pop()
        printAllSubsets(inputArr, res, curr + 1, N)

    printAllSubsets(inputArr, res, curr, N)
    print(ans)
    ans.sort()
    for i in range(len(ans)):
        if ans[i] == ans[i - 1]:
            continue
        unique.append(ans[i])
    print(unique)


printUniqueSubsets([1, 2, 2], [], 0, len([1, 2, 2]))

ans = []


def printUniqueSubsetsOptimal(arr, idx, ds):
    # if idx == len(arr):
    ans.append(list(ds))
    # return
    for i in range(idx, len(arr)):
        if arr[i] == arr[i - 1] and i > idx:
            continue
        ds.append(arr[i])
        printUniqueSubsetsOptimal(arr, i + 1, ds)
        ds.pop()


printUniqueSubsetsOptimal([1, 2, 2, 2, 3, 3], 0, [])
print(ans)
