def find_valley(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            r -= 1
        elif nums[mid] > nums[mid + 1]:
            l += 1
        elif nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
            return mid
    return l


print(find_valley([1, 2, 3, 1]))
print(find_valley([3, 2, 1]))
print(find_valley([4, 2, 7]))
