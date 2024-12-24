class Solution:
    def countFreq(self, arr, target):
        #code here
        map = {}
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] in map:
                map[arr[l]] += 1
            else:
                map[arr[l]] = 1
            if arr[r] in map:
                map[arr[r]] += 1
            else:
                map[arr[r]] = 1
            l += 1
            r -= 1
        if len(arr) % 2 != 0:
            if arr[(len(arr)//2)] in map:
                map[arr[(len(arr)//2)]] += 1
            else:
                map[arr[(len(arr)//2)]] = 1
        return map[target] if target in map else 0
