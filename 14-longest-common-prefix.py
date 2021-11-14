class Solution(object):

    def getCommon(self, common_prefix, inputString):

        length = min(len(common_prefix), len(inputString))

        ptr = 0

        for i in range(0, length):
            if common_prefix[i] == inputString[i]:
                ptr += 1
            else:
                break
        return common_prefix[0: ptr]
        
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            common_prefix = self.getCommon(common_prefix, strs[i])
            print(common_prefix)
        return common_prefix
            
        
        
        
        
            

