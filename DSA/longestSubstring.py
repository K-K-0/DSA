class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # maxans = 0
        # for i in range(len(s)):
        #     seet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in seet:
        #             break
        #         seet.add(s[j])
        #         maxans = max(maxans, j - i+1)
             
        # return maxans

        seen = set()
        maxans = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            maxans = max(maxans, r - l + 1)
        return maxans
      
         