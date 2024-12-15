def areRotations(s1, s2):
    def build_lps(s):
        lps = [0]
        i, j = 1, 0
        while i < len(s):
            if s[i] == s[j]:
                j += 1
                lps.append(j)
                i += 1
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    lps.append(0)
                    i += 1
        return lps

    def kmp(s1, s2, lps):
        n, m = len(s1), len(s2)
        if m > n:
            return False
        if m == n:
            return True if s1 == s2 else False
        if s2 == "":
            return True
        i, j = 0, 0
        while i < n and j < m:
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False if j < m else True

    s1 += s1
    lps = build_lps(s2)
    return kmp(s1, s2, lps)


# print(
#     areRotations(
#         "ncwuvtaxcygwghcvrfpwfdlhyrszzcqxkdfmcvwscytvdnmmmdnkranafryefhhuoccpcukyfesucuanxjtupwsluadxrmujbgdmkyvmjcbpcgfhpcrwrqkeoryrdivyxvjzhxwjvrbrlgipoyxhgzjamrvhqzhguuwuapqi",
#         "mmdnkranafryefhhuoccpcukyfesucuanxjtupwsluadxrmujbgdmkyvmjcbpcgfhpcrwrqkeoryrdivyxvjzhxwjvrbrlgipoyxhgzjamrvhqzhguuwuapqincwuvtaxcygwghcvrfpwfdlhyrszzcqxkdfmcvwscytvdnm",
#     )
# )
