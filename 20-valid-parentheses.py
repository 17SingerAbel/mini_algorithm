class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbols = {'(': ')', '{': '}', '[': ']'}
        
        stack = []
        
        for char in s:
            if char in symbols:
                stack.append(symbols[char])
            else:
                if stack:
                    expect = stack.pop(-1)
                    if char != expect:
                        return False
                else:
                    return False
        
        return not stack
