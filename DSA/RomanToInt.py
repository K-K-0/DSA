class Solution:
    def romanToInt(self, s: str) -> int:

        hm = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

        res = 0      
        for i in range(len(s)):
            cval = hm[s[i]]
            nval = hm[s[i+1]] if i+1 < len(s) else 0
            if cval < nval:
                res -= cval
            else:
                res += cval
            
        return res