from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # A = 0
        # B = 0
        # missedGuessed = []
        # missedSecret = defaultdict(int)
        # for i in xrange(len(secret)):
        #   if secret[i] == guess[i]:
        #       A += 1
        #   else:
        #       missedGuessed.append(guess[i])
        #       missedSecret[secret[i]] += 1
        # for c in missedGuessed:
        #   if missedSecret[c]:
        #       missedSecret[c]-=1
        #       B += 1
        # return str(A) + "A" + str(B) + "B"

        A = 0
        B = 0
        missedGuessed = defaultdict(int)
        missedSecret = defaultdict(int)
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                missedGuessed[guess[i]] += 1
                missedSecret[secret[i]] += 1
        for c in missedGuessed:
            B += min(missedGuessed[c],missedSecret[c])
        return str(A) + "A" + str(B) + "B"
#Bulls and Cows
#https://leetcode.com/problems/bulls-and-cows/description/