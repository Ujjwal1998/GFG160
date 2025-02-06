def countTriplets(arr, target):
    # code here
    # l = 0
    # m = l + 1
    res = set()
    # while l < r:
    for l in range(len(arr) - 2):
        m = l + 1
        r = len(arr) - 1
        while m < r:
            csum = arr[l] + arr[m] + arr[r]
            # print(csum)
            if csum == target:
                print(l, m, r)
                res.add(str(l) + "_" + str(m) + "_" + str(r))
                m += 1
                # here is the problem how do you know m, ko badao ya right ko badao
                # break
            else:
                if csum > target:
                    r -= 1
                else:
                    m += 1
    print(res)
    return len(res)


def countTripletsOpt(arr, target):
    n = len(arr)
    res = 0

    # Iterate through each element as the first element of the triplet
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        # Use two-pointer approach to find triplets
        while left < right:

            # Calculate the sum of the triplet
            sum = arr[i] + arr[left] + arr[right]

            # If sum is smaller, move to bigger values
            if sum < target:
                left += 1

            # If sum is greater, move to smaller values
            elif sum > target:
                right -= 1

            # If sum is equal to target
            else:
                ele1 = arr[left]
                ele2 = arr[right]
                print(i, left, right, ele1, ele2)
                cnt1 = 0
                cnt2 = 0

                # Count frequency of the current value at 'left'
                while left <= right and arr[left] == ele1:
                    left += 1
                    cnt1 += 1

                # Count frequency of the current value at 'right'
                while left <= right and arr[right] == ele2:
                    right -= 1
                    cnt2 += 1

                # If both the elements are the same, then count of pairs
                # = the number of ways to choose 2 elements among cnt1 elements
                if ele1 == ele2:
                    res += (cnt1 * (cnt1 - 1)) // 2

                # If the elements are different, then count of pairs
                # = product of the count of both elements
                else:
                    res += cnt1 * cnt2

    return res


def countTripletsSlow(arr, target):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                csum = arr[i] + arr[j] + arr[k]
                if csum == target:
                    print(i, j, k)


# countTriplets([-15, -7, -5, -4, 0, 1, 5, 7, 8, 20, 20], 1)
# countTripletsOpt([-15, -7, -5, -4, 0, 1, 5, 7, 8, 20, 20], 1)
# print(countTripletsOpt([-15, -7, -5, -4, 0, 1, 5, 7, 8, 20, 20], 1))
countTripletsSlow([-15, -7, -5, -4, 0, 1, 5, 7, 8, 20, 20], 1)
