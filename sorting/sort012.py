def sort012(arr):
    # code here
    low, med, high = 0, 0, len(arr) - 1
    while med <= high:
        if arr[med] == 0:
            arr[low], arr[med] = arr[med], arr[low]
            low += 1
            med += 1
        elif arr[med] == 1:
            med += 1
        else:
            arr[med], arr[high] = arr[high], arr[med]
            high -= 1
    return arr


print(sort012([0, 1, 2, 0, 1, 2]))
