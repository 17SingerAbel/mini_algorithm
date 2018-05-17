class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max_h = 0
        while i < j:
            if height[i] > height[j]:
                cur = height[j] * (j-i)
                j -= 1
            else:
                cur = height[i] * (j-i)
                i += 1
            if cur > max_h:
                max_h = cur
        return max_h