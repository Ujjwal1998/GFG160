from collections import defaultdict

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1) != len(s2): return False
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for char in s1:
            map1[char] +=1 
        for char in s2:
            map2[char] +=1 
        # print(map1, map2)
        for char in map1.keys():
            if char not in map2.keys():
                return False
            else:
                if map2[char] != map1[char]:
                    return False
        return True
