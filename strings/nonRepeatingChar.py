class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        map = [0] * 26
        for char in s:
            map[ord(char) - ord("a")] += 1
        for char in s:
            if map[ord(char) - ord("a")] == 1:
                return char
        return "$"
