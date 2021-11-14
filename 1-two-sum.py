class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pool = {}

        for i in range(len(nums)):
            num = nums[i]
            res = target - num
    
            if res in pool.keys():
                return [pool[res], i]
            
            pool[num] = i
