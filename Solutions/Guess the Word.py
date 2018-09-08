# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

# secret = "acckzz"
# wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
secret = "hbaczn"
wordlist =["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]

class Master(object):
    def __init__(self):
        self.secret = secret
        self.times = 0
    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        self.times += 1
        print "guess times:",self.times,word
        count = 0
        for i in xrange(len(word)):
            if word[i] == self.secret[i]:
                count += 1
        return count

def diff(w1,w2):
    count = 0
    for i in xrange(len(w1)):
        if w1[i] == w2[i]:
             count += 1
    return count

class Solution(object):
    def chooseWord(self,pool):
        minRetain = len(pool)
        word = None
        for w in pool:
            r = [0,0,0,0,0,0]
            for other in pool:
                if w == other:
                    continue
                r[diff(w,other)] += 1
            m = max(r)
            if m < minRetain:
                minRetain = m
                word = w
        return word

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        
        pool = list(wordlist)
        results = []
        while pool:
            candidate = self.chooseWord(pool)
            # print candidate
            pool.remove(candidate)
            matches = master.guess(candidate)
            newpool = []
            if matches == 6:
                #print "Found it!",candidate
                return
            results.append([candidate,matches])
            for w in pool:
                qualify = True
                for word,result in results:
                    if result != diff(word,w):
                        qualify = False
                        break
                if qualify:
                    newpool.append(w)
            pool = newpool

s = Solution()
master = Master()
s.findSecretWord(wordlist,master)
            
#Guess the Word
#https://leetcode.com/problems/guess-the-word/description/