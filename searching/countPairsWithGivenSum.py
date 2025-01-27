def countPairs(arr, target):
        #Your code here
        l = 0
        r = len(arr) - 1
        arr.sort()
        res = 0
        while l < r:
            if arr[l] + arr[r] < target:
                l += 1
            elif arr[l] + arr[r] > target:
                r -= 1
            else:
                cnt1 = 0
                cnt2 = 0
                elem1 = arr[l]
                elem2 = arr[r]
                while l <= r and arr[l] == elem1:
                    cnt1 += 1
                    l += 1
                while l <= r and arr[r] == elem2:
                    cnt2 += 1
                    r -= 1
                if elem1 == elem2:
                    res += (cnt1 * (cnt1 - 1)) // 2
                else:
                    res += cnt1 * cnt2
        return res
#can also be done with dictionary
