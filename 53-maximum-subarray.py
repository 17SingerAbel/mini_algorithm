class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_sum = 0
        max_sum = nums[0]
        
        for i in range(0, len(nums)):
            current_sum += nums[i]
    
            if current_sum < nums[i]:
                current_sum = nums[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum
