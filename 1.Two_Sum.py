class Solution:
    def twoSum(self, nums, target):
        
        if not nums:
            return
        seen = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [i,seen[diff]]
            else:
                seen[n]=i