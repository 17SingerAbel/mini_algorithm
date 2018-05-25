class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.lst.append([x, cur_min])

    def pop(self):
        """
        :rtype: void
        """
        self.lst.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.lst) == 0:
            return None
        return self.lst[-1][1]