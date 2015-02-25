class MinStack:
    # @param x, an integer
    # @return an integer

    
    def __init__(self):
        self.vals = []
        self.min = None
        
    def push(self, x):
        self.vals.append(x)
        if self.min:
            if x < self.min:
                self.min = x
        else:
            self.min = x

    def pop(self):
        x = self.vals.pop()
        if x == self.min:
            if len(self.vals):
                self.min = min(self.vals)
            else:
                self.min = None
        return x

    # @return an integer
    def top(self):
        return self.vals[-1]

    # @return an integer
    def getMin(self):
        return self.min
#Min Stack
#https://oj.leetcode.com/problems/min-stack/