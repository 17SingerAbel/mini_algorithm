class Solution:
        
    def isPalidrome(self, s):
        start, end = 0, len(s)-1
        
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        
        count = 0
        
        while start < end:
            
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.isPalidrome(s[0: start] + s[start+1: len(s)]) or self.isPalidrome(s[0: end] + s[end+1: len(s)])
                
        return True

