class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        seen = set()
        min = 99999999999
        for num in arr:
            seen.add(num)
        res = 1
        # print(res)
        while True:
            if res not in seen:
                break
            res+=1
        return res
