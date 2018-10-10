class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        stack = [[]]
        scope = []
        p = 0
        start = 0
        def eval(exp):
        	if exp[0] in "-0123456789":
        		return int(exp)
        	else:
        		sp = len(scope)-1
        		while exp not in scope[sp]:
        			sp -= 1
        		return int(scope[sp][exp])

        while p < len(expression):
        	if expression[p] == "(":
        		stack.append([])
        		start = p+1
        	elif expression[p] == ")":
        		if expression[p-1] != ")":
        			word = expression[start:p]
        			stack[-1].append(word)
        		start = p+1
        		if stack[-1][0] == "add":
        			val = eval(stack[-1][-1]) + eval(stack[-1][-2])
        		elif stack[-1][0] == "mult":
        			val = eval(stack[-1][-1]) * eval(stack[-1][-2])
        		else:
        			val = eval(stack[-1][-1])
        			scope.pop()
        		stack.pop()
        		stack[-1].append(str(val))
        	elif expression[p] == " ":
        		if expression[p-1] != ")":
        			word = expression[start:p]
        			stack[-1].append(word)
        		start = p+1
        		if stack[-1][0] == "let":
        			if len(stack[-1]) == 1:
        				scope.append({})
        			elif len(stack[-1]) % 2:
        				scope[-1][stack[-1][-2]] = str(eval(stack[-1][-1]))
        	p+=1
        return int(stack[0][0])

s = Solution()
print s.evaluate("(add 1 2)")
print s.evaluate("(mult 3 (add 2 3))")
print s.evaluate("(let x 2 (mult x 5))")
print s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")
print s.evaluate("(let x 3 x 2 x)")
print s.evaluate("(let x 1 y 2 x (add x y) (add x y))")
print s.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))")
print s.evaluate("(let a1 3 b2 (add a1 1) b2) ")
print s.evaluate("(let x 7 -12)")
print s.evaluate("(let x -2 y x y)")


#Parse Lisp Expression
#https://leetcode.com/problems/parse-lisp-expression/description/