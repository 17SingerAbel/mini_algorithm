class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = [1]
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                group[-1] += 1
            else:
                group.append(1)
        
        result = 0
        for i in range(1, len(group)):
            result += min(group[i-1], group[i])
        return result
            
