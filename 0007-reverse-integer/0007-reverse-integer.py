class Solution(object):
     def reverse(self, x):
        sign = -1 if x < 0 else 1
        num=0
        remainder=0
       
        xh = abs(x)
        while xh>0:
             remainder=xh%10
             xh=xh//10
             num=num*10+remainder
             
        if num > 2**31 - 1:
                return 0
                   
        return sign*num