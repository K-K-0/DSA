from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)
        dic = defaultdict(int)
        presum = 0
        count = 0

        dic[0] = 1

        for i in range(len(nums)):
            presum += nums[i]
            remove = presum - goal
            count += dic[remove]
            dic[presum] += 1
        return count
        