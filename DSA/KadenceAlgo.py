import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        minn = -sys.maxsize-1

        ans = 0
        
        for i in range(len(nums)):
            ans += nums[i]

            if ans > minn:
                minn = ans

            if ans < 0:
                ans = 0

        return minn





















        # --- >Brute-Force Approach

        # res = []
        # ans = -99

        # if len(nums) == 1:
        #     return nums[0]

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         res.append(nums[i:j])
        
        # for i in res:
        #     if sum(i) > ans:
        #         ans = sum(i)
        # return ans
        