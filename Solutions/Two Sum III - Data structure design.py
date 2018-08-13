class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        # p = len(self.q)
        # for i in range(len(self.q)):
        #     if self.q[i] >= number:
        #         p =  i
        #         break
        # self.q.insert(p,number)
        # print self.q
        self.q.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        self.q.sort()
        start = 0
        end = len(self.q)-1
        while start < end:
            v = self.q[start] + self.q[end] 
            
            if v == value:
                return True
            elif v > value:
                end -= 1
            else:
                start += 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(1)
# obj.add(3)
# obj.add(5)
# print obj.find(4)
# print obj.find(7)
# param_2 = obj.find(value)
#Two Sum III - Data structure design
#https://leetcode.com/problems/two-sum-iii-data-structure-design/description/