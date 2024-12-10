class Solution:
	def addBinary(self, s1, s2):
		# code here
    	n1 = len(s1)
        n2 = len(s2)
        i1 = n1 - 1
        i2 = n2 - 1
        res = ""
        carry = 0
        while i1 >= 0 or i2 >= 0:
            dig1 = int(s1[i1]) if i1 >= 0 else 0
            dig2 = int(s2[i2]) if i2 >= 0 else 0
            value = (dig1 + dig2 + carry) % 2
            carry = (dig1 + dig2 + carry) // 2
            res = str(value) + res
            i1 -= 1
            i2 -= 1
        if carry:
            res = "1" + res
        i = 0
        while res[i] == "0":
            i += 1
        return res[i:]
