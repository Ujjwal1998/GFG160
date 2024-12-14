class Solution:
    def minChar(self, s):
        #Write your code here
        def computeLPSArray(pat):
            n = len(pat)
            lps = [0] * n
        
            # lps[0] is always 0
            len_lps = 0
        
            # loop calculates lps[i] for i = 1 to n-1
            i = 1
            while i < n:
              
                # If the characters match, increment len
                # and set lps[i]
                if pat[i] == pat[len_lps]:
                    len_lps += 1
                    lps[i] = len_lps
                    i += 1
                
                # If there is a mismatch
                else:
                  
                    # If len is not zero, update len to 
                    # the last known prefix length
                    if len_lps != 0:
                        len_lps = lps[len_lps - 1]
                        
                    # No prefix matches, set lps[i] to 0
                    else:
                        lps[i] = 0
                        i += 1
            return lps
            
        n = len(s)
        rev = s[::-1]
        s = s + "$" + rev
        lps = computeLPSArray(s)
        return n - lps[-1]
