def nestedListSum(nums):

    def recurse(element, depth):
        total = 0
        for num in element:
            if isinstance(num, list):
                total += recurse(num, depth + 1)
            else:
                total += num * depth
        return total

    return recurse(nums, 1)


print(nestedListSum([1, 2, 3, [1]]))
