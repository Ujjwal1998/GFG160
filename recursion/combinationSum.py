def combinationSum(candidates, target):
    def recurse(arr, N, i, c_sum, target, curr_res, res):
        # print(curr_res, c_sum, target)
        if c_sum > target:
            return
        if c_sum == target:
            print("here")
            res.append(curr_res)
            return
        if i >= N:
            return
        # if (arr[i]<= target):
        curr_res.append(arr[i])
        c_sum += arr[i]
        recurse(arr, N, i, c_sum, target, curr_res, res)
        c_sum -= arr[i]
        curr_res.pop()
        recurse(arr, N, i + 1, c_sum, target, curr_res, res)

    res = []
    curr_res = []
    recurse(candidates, len(candidates), 0, 0, target, curr_res, res)
    return res


print(combinationSum([2, 3, 6, 7], 7))
