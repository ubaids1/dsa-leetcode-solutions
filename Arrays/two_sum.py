class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        numMap = {}

        for i in range(n):
            compliment = target - nums[i]
            if compliment in numMap:
                return [numMap[compliment],i]
            numMap[nums[i]] = i
            
        return []