class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        self.stack = []
     	max_length = 0
     	#longest = ""
     	stack_c_length = 0
        components = input.split("\n")
        for word in components:
        	i = 0
        	#print word
        	ts = 0
        	while i < len(word)-1:
        		if word[i] == "\t":
        			i+=1
        			ts += 1
        		else:
        			break
        	w = word[i:]
        	while len(self.stack) > ts:
        			removed = self.stack.pop()
        			stack_c_length -= len(removed)
        	if "." in w:
        		#print self.stack,w
        		if stack_c_length + len(w) + len(self.stack) > max_length:
        			max_length = stack_c_length + len(w) + len(self.stack)
        			#longest = "/".join(self.stack) + w
        	else:
        		self.stack.append(w)
        		stack_c_length += len(w)
        	#print w,self.stack
        #print max_length
        return max_length


s = Solution()
print s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
print s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print s.lengthLongestPath("dir\n    file.txt")
print s.lengthLongestPath("dir\n        file.txt")


#Longest Absolute File Path
#https://leetcode.com/problems/longest-absolute-file-path/description/