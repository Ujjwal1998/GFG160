def merge_sort(arr):
    if len(arr) == 1:
        return
    left_arr = arr[: len(arr) // 2]
    right_arr = arr[len(arr) // 2 :]
    merge_sort(left_arr)
    merge_sort(right_arr)
    i, j, k = 0, 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr1 = [1, 2, 3, 45, 54, 3]
# print(mergeSort())
merge_sort(arr1)
print(arr1)
