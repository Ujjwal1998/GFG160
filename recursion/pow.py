def power(b, e):
    # Code Here
    def recurse(idx, b, e, curr):
        print(curr, idx)
        if idx == e:
            if e < 0:
                return float(1 / curr)
            else:
                return float(curr)
        return recurse(idx + 1, b, e, curr * b)

    ans = recurse(0, b, e, 1)
    print(ans)
    return ans


power(3, 5)
