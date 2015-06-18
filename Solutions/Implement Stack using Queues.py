class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.data = []
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)

    # @return nothing
    def pop(self):
        temp = []
        x = None
        while len(self.data):
            x = self.data.pop(0)
            if len(self.data) != 0:
                temp.append(x)
        self.data = temp
        return x

    # @return an integer
    def top(self):
        temp = []
        x = None
        while len(self.data):
            x = self.data.pop(0)
            temp.append(x)
        self.data = temp
        return x
        

    # @return an boolean
    def empty(self):
        if len(self.data):
            return False
        else:
            return True
        
#Implement Stack using Queues
#https://leetcode.com/problems/implement-stack-using-queues/