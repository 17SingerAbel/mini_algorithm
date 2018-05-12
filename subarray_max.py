class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        p = len(nums)-1
        if l == p:
            return nums[l]
        else:
            m = (len(nums)-1) // 2
            left = nums[:m+1]
            right = nums[m+1:]
            sm = 0
            left_sum = -100000
            right_sum = -100000
            for i in range(m, l-1, -1):
                sm += nums[i]
                if sm > left_sum:
                    left_sum = sm
            sm = 0
            for i in range(m+1, len(nums)):
                sm += nums[i]
                if sm > right_sum:
                    right_sum = sm
            return max(self.maxSubArray(left), self.maxSubArray(right), left_sum + right_sum)