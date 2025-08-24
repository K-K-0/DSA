class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        idx = -1

        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                idx = i
                break
        
        if idx == -1:
            nums.reverse()
            return nums

        for i in reversed(range(idx+1, n)):
            if nums[i] > nums[idx]:
                nums[i],nums[idx] = nums[idx], nums[i]
                break
        nums[idx+1:] = reversed(nums[idx+1:])

        return nums