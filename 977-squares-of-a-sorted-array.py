class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, len(nums)-1
        
        result = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            
            square = nums[p1]
            
            if abs(nums[p2]) > abs(nums[p1]):
                square = nums[p2]
                p2 -= 1
            else:
                p1 += 1
                
            result[i] = square * square
            
        return result
                
