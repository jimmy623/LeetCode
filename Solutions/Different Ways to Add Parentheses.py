class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        numbers = []
        operators = []
        p = 0
        for i in range(len(input)):
        	if input[i] in "+-*":
        		operators.append(input[i])
        		numbers.append(int(input[p:i]))
        		p = i + 1
        numbers.append(int(input[p:len(input)]))
        result = self.compute(numbers,operators)
        return result

    def compute(self,numbers,operators):
    	if len(numbers) == 1:
    		return numbers
    	result = []
    	for i in range(len(operators)):
    		l = self.compute(numbers[:i+1],operators[:i])
    		r = self.compute(numbers[i+1:],operators[i+1:])
    		op = operators[i]
    		for j in l:
    			for k in r:
    				if op == "+":
    			 		result.append(j+k)
    				elif op == "-":
    					result.append(j-k)
    				elif op == "*":
    					result.append(j*k)
    	return result

    

s = Solution()
data = "2*3-4*5"
data = "2-1-1"
print s.diffWaysToCompute(data)


#Different Ways to Add Parentheses
#https://leetcode.com/problems/different-ways-to-add-parentheses/description/