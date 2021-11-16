class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers)-1
        
        while start < end:
            value = numbers[start] + numbers[end] 
            if value == target:
                return [start + 1, end + 1]
            elif value > target:
                end -= 1
            else:
                start += 1
                
