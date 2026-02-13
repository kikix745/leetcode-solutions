class Solution(object):
    def findWordsContaining(self, words, x):
        list1=[]
        for w_index in range(len(words)) :
            word=words[ w_index]
            for i in range(len(word)):
                if x==word[i]:
                    list1.append(w_index)
                    break
        return list1