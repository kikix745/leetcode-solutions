class Solution(object):
    def maxArea(self, height):
      left=0
      right=len(height)-1
      max_area=0
      while left<=right:
        w=right-left
        h=min(height[left],height[right])
        a=w*h
        max_area=max(max_area,a)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1    
 
      return max_area