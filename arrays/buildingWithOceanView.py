def oceanview(heights):
    ans = []
    mx = 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > mx:
            mx = heights[i]
            ans.append(i)

    return ans


print(oceanview([4, 2, 3, 1]))
print(oceanview([4, 3, 2, 1]))
print(oceanview([1, 3, 2, 4]))
