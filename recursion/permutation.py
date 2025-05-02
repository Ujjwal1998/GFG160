# "ABC"
def permutation(word):
    def recurse(ds, N, seen, ans):
        if len(ds) == N:
            ans.append("".join(list(ds)))
            return
        for i in range(N):
            char = word[i]
            if char not in seen:
                ds.append(char)
                seen.add(char)
                recurse(ds, N, seen, ans)
                ds.pop()
                seen.remove(char)

    seen = set()
    ans = []
    recurse([], len(word), seen, ans)


def permutationOptimal(arr):
    ans = []

    def recurse(idx, arr):
        if idx == len(arr):
            ans.append(list(arr))
            return
        for i in range(idx, len(arr)):
            [arr[idx], arr[i]] = [arr[i], arr[idx]]
            recurse(idx + 1, arr)
            [arr[idx], arr[i]] = [arr[i], arr[idx]]

    recurse(0, arr)
    print(ans)


permutationOptimal([1, 2, 3])
