# parameterised
def sumtoN(sum1, curr, N):
    if curr < 1:
        print(sum1)
        return
    sum1 += curr
    sumtoN(sum1, curr - 1, N)


sumtoN(0, 5, 5)


# functional
def sumToNFn(N):
    if N == 0:
        return 0
    return N + sumToNFn(N - 1)


def factorialNFn(N):
    if N == 0:
        return 1
    return N * factorialNFn(N - 1)


# check if palindrome


def palinRecurse(input, l, n):
    if l >= n // 2:
        return True
    if input[l] != input[n - l - 1]:
        return False
    return palinRecurse(input, l + 1, n)


# sumToNFn(5)
# print(sumToNFn(5))
# print(factorialNFn(3))
print(palinRecurse("MADAM12", 0, 7))
