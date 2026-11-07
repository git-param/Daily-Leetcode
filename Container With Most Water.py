class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] > height[right]:
                max_vol = max((height[right] * (right-left)), max_vol)
                right -= 1
            else:
                max_vol = max((height[left] * (right-left)), max_vol)
                left += 1
        
        return max_vol