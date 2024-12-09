class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        sign = 1
        index = 0
        while index < n and s[index] == " ":
            index += 1
        if index == n:
            return 0
        if s[index] == "-" or s[index] == "+":
            if s[index] == "-":
                sign = sign * -1
            index += 1
        if index == n:
            return 0
        res = 0
        while index < n and s[index].isdigit():
            if int(s[index]) == 0 and res == 0:
                index += 1
                continue
            res = res * 10 + int(s[index])
            index += 1
        if res * sign >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res * sign < -1 * 2 **31:
            return -2 **31
        else:
            return res * sign