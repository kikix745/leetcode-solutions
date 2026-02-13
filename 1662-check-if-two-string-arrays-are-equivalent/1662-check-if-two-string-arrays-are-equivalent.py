class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        wf=""
        wt=""
        for w1 in word1:
            wf=wf+w1
        for w2 in word2:
            wt=wt+w2

        if wt==wf:
            return True
        else:
            return False    