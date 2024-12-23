def mergeArrays(a, b):
        left = len(a) - 1
        right = 0
        while left >= 0 and right < len(b):
            if a[left] > b[right]:
                a[left], b[right] = b[right], a[left]
                left -= 1
                right += 1
            else:
                break
        a.sort()
        b.sort()
