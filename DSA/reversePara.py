class Solution:
    def reverseWords(self, s: str) -> str:

        res = ''

        for i in s.split():
            res  = i + ' ' + res
        
        return res[:-1]
    
        # return ' '.join(reversed(s.split()))
            

        