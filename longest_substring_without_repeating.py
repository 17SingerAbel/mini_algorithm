class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        count = 0
        maximun = 0
        i,j = 0,0
        while(i < len(s) and j < len(s)):
            if s[j] in dict:
                i = max(dict[s[j]], i)
                
            maximun = max(maximun, j-i+1)
            dict[s[j]] = j+1
 
            j = j+1         
        return maximun