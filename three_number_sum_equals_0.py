class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result = []
        single = {}
        temp = {}
        total = []
        for k in range(0, len(nums)):
            single[nums[k]] = k
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                two_sum = -nums[i]-nums[j]
                if two_sum in single:                    
                    if (single[two_sum] != i) and (single[two_sum] != j):
                    temp = {two_sum, nums[i], nums[j]}
                    if temp not in total:
                        result.append([two_sum, nums[i], nums[j]])
                        total.append(temp)
        return result