def circularSubarraySum(arr):
    ##Your code here
    f1 = arr[0];
    f2 = arr[0];
    s1 = arr[0];
    s2 = arr[0];
    
    for num in arr[1:]:
        f1 = max(0,f1) + num
        f2 = min(0,f2) + num
        s1 = max(s1,f1)
        s2 = min(s2,f2)
        
    if s1 <= 0:
        return s1
    else:
        total_sum = sum(arr)
        return max(s1, total_sum - s2)
