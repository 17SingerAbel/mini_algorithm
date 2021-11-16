class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        
        while n not in visited and n != 1:
            
            visited.add(n)
            
            new_n = 0
            for char in str(n):
                new_n += int(char) ** 2
                
            n = new_n
        
        return n == 1
