class Solution(object):
    def isPalindrome(self, x):
        number=0
        remainder=0
        original=x
        if x < 0:
            return False
        while x>0:
             remainder=x%10
             x=x//10
             number = number * 10 + remainder
        return number==original