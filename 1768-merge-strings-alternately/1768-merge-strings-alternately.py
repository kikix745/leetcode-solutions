class Solution(object):
    def mergeAlternately(self, word1, word2):
        res=""
        n=max(len(word1),len(word2))
        for i in range(n):
            if i<len(word1):
                res+=word1[i]
            if i<len(word2):
                res=res+word2[i]
        return res        





