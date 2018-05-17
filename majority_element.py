class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for item in nums:
            if item not in dic:
                dic[item] = 0
        for item in nums:
            dic[item] += 1
        
        max_count = 0
        tar = 0
        for key, val in dic.items():
            if val > max_count:
                max_count = val
                tar = key
        return tar