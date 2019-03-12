class Stack:
    def __init__(self):
        self.container = []
        self.size = 0
    def push(self, obj):
        self.container.append(obj)
        self.size +=1

    def pop(self):
        last = self.container[self.size-1]
        self.container = self.container[:self.size-1]
        self.size -= 1
        return last
        

    def isEmpty(self):
        return self.container == []
    
    def getSize(self):
        return self.size


s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
s.push(True)
print(s.getSize())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.getSize())
