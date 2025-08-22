class Solution:
    def countHomogenous(self, s: str) -> int:

        ans = 0
        mod = 10 ** 9 + 7
        i = 0

        while i < len(s):
            count = 0
            j = i

            while j < len(s) and s[j] == s[i]:
                count += 1
                j += 1
            
            ans += count * (count + 1) // 2
            ans %= mod
            
            i = j
               
        return ans


        