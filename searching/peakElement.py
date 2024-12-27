def peakElement(arr):
        # Code here
        if len(arr) == 1: 
            return True
        # if arr[0] > arr[1] or arr[-1] > arr[-2]: 
        #     return True
        res = []
        for i in range(1,len(arr)):
            if (i + 1 == len(arr)):
                if arr[i] > arr[i-1] and arr[i] > -1:
                    return i
            else:
                if arr[i] > arr[i-1] and arr[i] > arr[i + 1]:
                    return i
        return False
