class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        comps = []
        self.d = {
    		1 : "One",
    		2 : "Two",
    		3 : "Three",
    		4 : "Four",
    		5 : "Five",
    		6 : "Six",
    		7 : "Seven",
    		8 : "Eight",
    		9 : "Nine",
    		10: "Ten",
    		11: "Eleven",
    		12: "Twelve",
    		13: "Thirteen",
    		14: "Fourteen",
    		15: "Fifteen",
    		16: "Sixteen",
    		17: "Seventeen",
    		18: "Eighteen",
    		19: "Nineteen",
    		20: "Twenty",
    		30: "Thirty",
    		40: "Forty",
    		50: "Fifty",
    		60: "Sixty",
    		70: "Seventy",
    		80: "Eighty",
    		90: "Ninety"
    	}
        if num >= 10**9:
        	part = num / 10**9
        	num = num - part * 10**9
        	comps += self.lessThan1000(part)
        	comps.append("Billion")

        if num >= 10 ** 6:
        	part = num / 10**6
        	num = num - part * 10**6
        	comps += self.lessThan1000(part)
        	comps.append("Million")
        if num >= 10 ** 3:
        	part = num / 10**3
        	num = num - part * 10**3
        	comps += self.lessThan1000(part)
        	comps.append("Thousand")
        # print comps

        comps += self.lessThan1000(num)
        return " ".join(comps)

    def lessThan1000(self,num):
    	comps = []
    	if num >= 100:
    		part = num / 100
    		num = num % 100
    		comps.append(self.d[part])
    		comps.append("Hundred")
    	if num != 0:
    		if num <= 20:
    			comps.append(self.d[num])
    		else:
    			part = num / 10
    			num = num % 10
    			comps.append(self.d[part*10])
    			if num != 0:
    				comps.append(self.d[num])
    	return comps


s = Solution()
print s.numberToWords(123)
print s.numberToWords(12345)
print s.numberToWords(1234567)
print s.numberToWords(1234567891)

#Integer to English Words
#https://leetcode.com/problems/integer-to-english-words/description/