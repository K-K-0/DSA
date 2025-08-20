class Solution:
    def maxDepth(self, s: str) -> int:

        result = 0
        current = 0
        for i in range(len(s)):
            if s[i] == '(':
                current += 1
            elif s[i] == ")": 
                current -= 1
            result = max(result, current)
        return result
        

        
        