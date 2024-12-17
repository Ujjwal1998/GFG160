# import itertools import C


def hIndex(citations):
    citations.sort(reverse=True)
    idx = 0
    while idx < len(citations) and citations[idx] >= idx + 1:
        idx += 1
    return idx
    # return max


print(hIndex([8, 10, 12, 12, 9, 12]))
