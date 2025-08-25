class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(len(nums)):
            complete = target - nums[i]
            if complete in hashMap:
                return [i,hashMap[complete]]
            hashMap[nums[i]] = i
        return []


        #     hashmap = {}
        # for i in range (0, len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap:
        #         return [i, hashmap[complement]]
        #     hashmap[nums[i]] = i
        # return []

        

        # # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
            