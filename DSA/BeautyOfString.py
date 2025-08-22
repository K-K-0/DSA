class Solution:

    # def min_freq(self, freq):
    #     min_count = float('inf')

    #     for i in freq:
    #         if i != 0:
    #             min_count = min(min_count, i)
    #     return min_count
    
    # def max_freq(self, freq):
    #     max_count = 0

    #     for i in freq:
    #         max_count = max(max_count, i)
    #     return max_count

    
    def beautySum(self, s: str) -> int:

        # beauty = 0

        # for i in range(len(s)):
        #     freq = [0] * 26
        #     for j in range(i,len(s)):
        #         freq[ord(s[j]) - ord('a')] += 1
        #         b = self.max_freq(freq) - self.min_freq(freq)
        #         beauty += b
        # return beauty


        ans = 0
        n = len(s)

        for i in range(n):
            freq = {}
            for j in range(i,n):
                freq[s[j]] = freq.get(s[j], 0) + 1

                min_val = min(freq.values())
                max_val = max(freq.values())

                ans += max_val - min_val
        return ans




        