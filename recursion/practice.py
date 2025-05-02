def myPrint(num):
    if num <= 0:
        return
    print("ujjwal")
    myPrint(num - 1)


def myPrintLinear(curr, num):
    if curr > num:
        return
    print(curr)
    myPrintLinear(curr + 1, num)


def myPrintLinearBacktrack(curr, num):
    if curr < 1:
        return
    myPrintLinearBacktrack(curr - 1, num)
    print(curr)


def myPrintLinearReverseBacktrack(curr, num):
    if curr > num:
        return
    myPrintLinearReverseBacktrack(curr + 1, num)
    print(curr)


myPrint(2)
myPrintLinear(1, 5)
myPrintLinearBacktrack(5, 5)
myPrintLinearReverseBacktrack(1, 7)
