def AtMost(nums, k):
        l = 0
        count = 0
        Odd_count = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                Odd_count += 1

            while Odd_count > k:
                if nums[l] % 2 != 0:
                    Odd_count -= 1
                l += 1
            
            count += (r - l + 1)
        return count
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        return AtMost(nums, k) - AtMost(nums, k-1)

        

        