class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        tar = strs[0]
        common = tar
        i = 0
        j = len(tar)
        for s in strs:
            if s == "":
                return ""
            elif s != tar:
                while j > len(s):
                    common = tar[:j]
                    j -= 1
                if i == j:
                    pass
                while i < j:
                    if tar[i] == s[i]:
                        i += 1
                    else:
                        break
                j = i
                i = 0
        if j >= 0:
            return common[:j]
        else:
            return ""