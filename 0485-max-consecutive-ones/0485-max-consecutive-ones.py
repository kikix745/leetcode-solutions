class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res=0
        best =0
        for i in range (len(nums)):
            if nums[i]==1:
                res+=1
                best=max(best,res)
            else:
                res=0    

        return best