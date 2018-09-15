from collections import defaultdict
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """

        count = len(hand)

        if count == 0 or count % W != 0:
        	return False
        if W == 1:
        	return True

        d = defaultdict(int)
        for n in hand:
        	d[n] += 1
        cards = d.keys()
        cards.sort()
        index = 0
        
        while W <= count:
        	while d[cards[index]] == 0:
        		index += 1
        	n = cards[index]
        	d[n] -= 1
        	for i in xrange(1,W):
        		if d[n+i]:
        			d[n+i] -= 1
        		else:
        			return False
        	count -= W
        return True


#Hand of Straights
#https://leetcode.com/problems/hand-of-straights/description/