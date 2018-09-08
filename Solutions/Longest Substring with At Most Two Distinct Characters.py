class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = []
        start = 0
        end = 0
        maxCount = 0
        while end < len(s):
        	if len(chars) < 2:
        		if not s[end] in chars:
        			chars.append(s[end])
        		end+=1
        		maxCount = max(maxCount,end-start)
        		continue
        	if s[end] in chars:
        		end += 1
        		maxCount = max(maxCount,end-start)
        		continue
        	else:
        		chars = [s[end],s[end-1]]
        		start = end - 1
        		while s[start-1] == s[end-1]:
        			start -= 1
        		end += 1

        return maxCount

s = Solution()
print s.lengthOfLongestSubstringTwoDistinct("eceba")
print s.lengthOfLongestSubstringTwoDistinct("ccaabbb")

#Longest Substring with At Most Two Distinct Characters
#https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/