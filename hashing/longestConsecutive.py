def longestConsecutive(arr):
    # code here
    arr = list(set(arr))
    arr.sort()
    res = 0
    curr = 1
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == 1:
            curr += 1
        else:
            curr = 1
        if curr > res:
            res = curr
    return res


def longestConsecutiveFast(arr):
    st = set()
    res = 0
    for elem in arr:
        st.add(elem)
    for elem in arr:
        if elem in st and (elem - 1) not in st:
            curr = elem
            curr_count = 0
            while curr in st:
                curr_count += 1
                st.remove(curr)
                curr += 1
            res = max(res, curr_count)
    return res


# longestConsecutive(
#     [
#         53,
#         57,
#         77,
#         15,
#         78,
#         58,
#         17,
#         63,
#         90,
#         73,
#         68,
#         82,
#         40,
#         68,
#         22,
#         52,
#         81,
#         92,
#         80,
#         37,
#         62,
#         17,
#         76,
#         67,
#         55,
#         56,
#         20,
#         22,
#         37,
#         71,
#         65,
#         7,
#         30,
#         93,
#         1,
#         1,
#         90,
#         46,
#         36,
#         74,
#         0,
#         37,
#         76,
#         69,
#         39,
#         97,
#         39,
#         30,
#         14,
#         89,
#         74,
#         71,
#         27,
#         79,
#         51,
#         45,
#         51,
#         54,
#         90,
#         35,
#         68,
#         38,
#         7,
#         82,
#         55,
#         65,
#         14,
#         40,
#         20,
#         64,
#         89,
#         95,
#         8,
#         43,
#         14,
#         88,
#         5,
#         24,
#         72,
#         9,
#         56,
#         17,
#         60,
#         91,
#         16,
#         94,
#         47,
#         15,
#         33,
#     ]
# )

print(
    longestConsecutive(
        [
            130,
            46,
            107,
            270,
            467,
            83,
            289,
            34,
            44,
            361,
            2,
            271,
            50,
            456,
            22,
            344,
            32,
            1,
            71,
            463,
            491,
            280,
            372,
            281,
            197,
            142,
            103,
            480,
            417,
            211,
            396,
            128,
            74,
            223,
            181,
            431,
            10,
            217,
            327,
            326,
            281,
            297,
            264,
            1,
            130,
            486,
            391,
            5,
            465,
            391,
            25,
            103,
            382,
            480,
            74,
            111,
            109,
            391,
            279,
            295,
            363,
            260,
        ]
    )
    == longestConsecutiveFast(
        [
            130,
            46,
            107,
            270,
            467,
            83,
            289,
            34,
            44,
            361,
            2,
            271,
            50,
            456,
            22,
            344,
            32,
            1,
            71,
            463,
            491,
            280,
            372,
            281,
            197,
            142,
            103,
            480,
            417,
            211,
            396,
            128,
            74,
            223,
            181,
            431,
            10,
            217,
            327,
            326,
            281,
            297,
            264,
            1,
            130,
            486,
            391,
            5,
            465,
            391,
            25,
            103,
            382,
            480,
            74,
            111,
            109,
            391,
            279,
            295,
            363,
            260,
        ]
    )
)
