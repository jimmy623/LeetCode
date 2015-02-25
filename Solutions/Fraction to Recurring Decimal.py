class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        flag = True
        
        if numerator * denominator >= 0:
            falg = True
        else:
            flag = False
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        fraction = numerator/denominator
        remain = numerator % denominator
        if remain == 0:
            if flag:
                return str(fraction)
            else:
                return "-" + str(fraction)
        
        after = ""
        record = [remain]
        i = remain*10
        while True:            
            if i < denominator:
                after += "0"
            else:
                d = i / denominator
                i = i % denominator
                after += str(d)
    
            if i == 0:
                break
                
            if i in record:
                index = record.index(i)
                result = str(fraction) + "." + after[0:index] + "(" + after[index:len(after)] + ")"
                if flag:
                    return result
                else:
                    return "-"+result
            else:
                record.append(i)
                i *= 10

        result = str(fraction) + "." + after
        if flag:
            return result
        else:
            return "-"+result
            
s = Solution()
print s.fractionToDecimal(1,6)

#Fraction to Recurring Decimal
#https://oj.leetcode.com/problems/fraction-to-recurring-decimal/