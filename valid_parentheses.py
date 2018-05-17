class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        dic = {'(':')', '{':'}', '[':']'}

        for i in range(len(s)):
            if s[i] in dic:
                lst.append(dic[s[i]])
            else:
                if not lst:
                    return False
                a = lst.pop()
                if a != s[i]:
                    return False
        if lst:
            return False
        return True